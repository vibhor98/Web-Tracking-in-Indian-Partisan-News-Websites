'''

This is the primary code for computing cookie-synchronization across different pairs of websites within each crawl

'''

import extract_cookie_ids
import extract_id_knowledge
import census_util
import find_site_leaning
import classify_domains
from collections import defaultdict
import sqlite3 as lite
import queue
import re
import os
import numpy
import csv

# Global Aggregation Variables
global_known_ids = {}
global_id_to_domain_map = defaultdict(list)
global_id_to_cookie_map = defaultdict(list)

# Path of the OpenWPM Dara
DATA_DIR = os.path.join(os.path.abspath(os.pardir),'OpenWPM Crawls')

# BFS HOP ANALYSIS
# for a given domain, returns a sorted list of sites within <hops> steps away in the sync graph
def build_hop_neighborhood(seed_domain, hop, domain_to_id, id_to_domain):
    domains_explored = set()  # list of domains we've visited
    search_queue = queue.Queue()  # list of the sites that we'll be visiting
    search_queue.put((seed_domain, 0))  # seeds the search with the initial domain

    # performs the BFS neighborhood search
    while not search_queue.empty():
        curr_domain, curr_depth = search_queue.get()

        # break the search if the nodes are too far away
        if curr_depth > hop:
            break

        # don't explore the node if we've already seen it
        if curr_domain in domains_explored:
            continue

        domains_explored.add(curr_domain)

        # don't expand out to neighbors if we are at the edge of the neighborhood
        if curr_depth == hop:
            continue

        # update the search queue
        for cookie_id in domain_to_id[curr_domain]:
            for domain in id_to_domain[cookie_id]:
                search_queue.put((domain, curr_depth + 1))

    neighborhood = list(domains_explored)
    neighborhood.sort()
    return neighborhood

# OVERALL COOKIE SYNC SCRIPT
# prints off the relevant statistics for the cookie syncing studies, given two crawl databases
# <db_to_analyze> specifies whether to extract from db1 or db2
def output_sync_measurements(db1, visit_id1, db2, visit_id2, db_to_analyze=1):

    global global_known_ids
    global global_id_to_domain_map
    global global_id_to_cookie_map
    
    print("Extracting persistent identifiers from each crawl...")
    # extract the cookie ids on a per-database basis
    cookies_db1 = extract_cookie_ids.extract_persistent_ids_from_dbs([db1], visit_id1)
    cookies_db2 = extract_cookie_ids.extract_persistent_ids_from_dbs([db2], visit_id2)
    
    print("Grabbing cookies...")

    # get the cookies that appear to be consistent ids and extract their values from db1
    id_cookies = extract_cookie_ids.extract_common_id_cookies([cookies_db1, cookies_db2])
    
    if db_to_analyze == 1:
        domain_to_fp_map = census_util.build_domain_map(db1, visit_id1)
        known_ids = extract_cookie_ids.extract_known_cookies_from_db(db1, id_cookies, visit_id1)
    else:
        domain_to_fp_map = census_util.build_domain_map(db2, visit_id2)
        known_ids = extract_cookie_ids.extract_known_cookies_from_db(db2, id_cookies, visit_id2)

    # remove known opt-out cookie strings
    for key in known_ids.keys():
        if (known_ids[key] == '0' \
            or known_ids[key] == '00000000-0000-0000-0000-000000000000' \
            or known_ids[key] == '0000000000000000' \
            or known_ids[key] == 'AAAAAAAAAAAAAAAAAAAAAA'):
            del known_ids[key]

    # Creating Global version for known_ids
    for key in known_ids.keys():
        if key not in global_known_ids.keys():
            global_known_ids[key] = []
            global_known_ids[key].append(known_ids[key])
        else:
            if known_ids[key] not in global_known_ids[key]:
                global_known_ids[key].append(known_ids[key])
        
    global_id_to_cookie_map = extract_cookie_ids.map_list_of_ids_to_cookies(global_known_ids)

    print("Build mapping between cookies, domains, and first parties...")

    # build the three maps that are most fundamental to the analysis
    id_to_cookie_map = extract_cookie_ids.map_ids_to_cookies(known_ids)
    id_to_cookie_map_pruned = census_util.prune_list_dict(id_to_cookie_map)

    if db_to_analyze == 1:
        id_to_domain_map = extract_id_knowledge.build_id_knowledge_dictionary(defaultdict(list), id_to_cookie_map, db1, visit_id1)
        global_id_to_domain_map = extract_id_knowledge.build_id_knowledge_dictionary(global_id_to_domain_map, global_id_to_cookie_map, db1, visit_id1)
    else:
        id_to_domain_map = extract_id_knowledge.build_id_knowledge_dictionary(defaultdict(list), id_to_cookie_map, db2, visit_id2)
        global_id_to_domain_map = extract_id_knowledge.build_id_knowledge_dictionary(global_id_to_domain_map, global_id_to_cookie_map, db2, visit_id2)
    id_to_domain_map = census_util.prune_list_dict(id_to_domain_map)
    
    domain_to_id_map = extract_id_knowledge.map_domains_to_known_ids(id_to_domain_map)
    domain_to_id_map_pruned = census_util.prune_list_dict(domain_to_id_map)

    print("Dumping results...")
    # ID and # of domains with knowledge of it
    
    id_to_domain_counts = census_util.sort_tuples([(key, len(id_to_domain_map[key])) for key in id_to_domain_map])
    # print(id_to_domain_counts)
    id_to_dm = list()
    for x in id_to_domain_counts:
        id_to_dm.append(x[1])
        # print(str(x[0]) + "\t" + str(x[1]))

    # Domain and IDs that it has knowledge of:")
    domain_to_id_counts = census_util.sort_tuples([(key, len(domain_to_id_map[key])) for key in domain_to_id_map])
    # print(domain_to_id_counts)

    dm_to_id = list()
    for domain, count in domain_to_id_counts:
        neigh1 = build_hop_neighborhood(domain, 1, domain_to_id_map, id_to_domain_map)
        depth1 = len(neigh1)
        num_doms1 = len(census_util.get_values_from_keys(neigh1, domain_to_fp_map))

        neigh2 = build_hop_neighborhood(domain, 2, domain_to_id_map, id_to_domain_map)
        depth2 = len(neigh2)
        num_doms2 = len(census_util.get_values_from_keys(neigh2, domain_to_fp_map))

        dm_to_id.append(count)
        # print(str(domain) + "\t" + str(count) + "\t" + str(depth1) + "\t" + str(num_doms1) + "\t" + str(depth2) + "\t" + str(num_doms2))

    a = str(len(id_to_cookie_map))
    b = str(len(known_ids))
    c = str(len(id_to_domain_map))
    id_cookies_in_sync = [cookie for key in id_to_domain_map for cookie in id_to_cookie_map[key]]
    d = str(len(list(set(id_cookies_in_sync))))
    e = str(len(domain_to_id_map))
    if len(dm_to_id) == 0:
        f = "0 | 0 | 0 | 0 "
    else:
        f = str(min(dm_to_id)) + " | "  + str(round(numpy.mean(dm_to_id), 2)) + ' | ' + str(round(numpy.median(dm_to_id), 2)) + " | " + str(max(dm_to_id))
    if len(id_to_dm) == 0:
        g = "0 | 0 | 0 | 0 "
    else:
    	g = str(min(id_to_dm)) + " | "  + str(round(numpy.mean(id_to_dm), 2)) + ' | ' + str(round(numpy.median(id_to_dm), 2)) + " | " + str(max(id_to_dm))

    return a, b, c, d, e, f, g



# The below codes does the same things as done by output_sync_measurements() function 
# and produces an aggregate value for all website pairs
if __name__ == "__main__":
    # Enter location of the file (crawl_file.sqlite) currently being run
    Stateful_Crawl = os.path.join(DATA_DIR, 'crawl-data_stateful_homepage1.sqlite')

    data_folder_path = os.path.join(os.path.abspath(os.pardir))
    # Enter name of the political groups being studied currently (Eg. LEFT-RIGHT)
    file_path = os.path.join(os.path.join(data_folder_path, 'Cookie Synchronization Analysis'), 'CS RIGHT-RIGHT Analysis.csv')

    writer = csv.writer(open(file_path, 'w', newline=''))
    writer.writerow(['Website1', 'Leaning_of_Website1', 'Website2', 'Leaning_of_Website2', 'No_of_IDs', 'No_of_ID_Cookies', 'No_of_IDs_in_Sync', 
                     'No_of_ID_Cookies_in_Sync', 'No_of_Domains_in_Sync', 'IDs_known_per_Party (Min | Mean | Median | Max)',
                     'Parties_knowing_an_ID (Min | Mean | Median | Max)'])
    
    conn = lite.connect(Stateful_Crawl)
    cur = conn.cursor()
    
    # Choosing website pairs to dtudy once-by-onne
    for site1 in range(1, 123):
        for res in cur.execute('SELECT arguments FROM crawl_history'+' WHERE visit_id = '+str(site1)):
            site1_url = str(res[0]).split(',')[0][9:-1]
        site1_leaning = find_site_leaning.get_leaning(site1_url)
        if site1_leaning not in ['RIGHT']: # ['RIGHT', 'LEFT', 'CENTRE']:
            continue
        
        for site2 in range(site1+1, 124):
            print(site1)

            for res in cur.execute('SELECT arguments FROM crawl_history'+' WHERE visit_id = '+str(site2)):
                site2_url = str(res[0]).split(',')[0][9:-1]
            site2_leaning = find_site_leaning.get_leaning(site2_url)
            if site2_leaning not in ['RIGHT']: # ['RIGHT', 'LEFT', 'CENTRE']:
                continue

            # print(site1, site1_url, site2, site2_url)
            a, b, c, d, e, f, g = output_sync_measurements(Stateful_Crawl, site1, Stateful_Crawl, site2)

            writer.writerow([site1_url, site1_leaning, site2_url, site2_leaning, a, b, c, d, e, f, g])
    
    # Compute same things as above but this time for global variables
    global_id_to_domain_map = census_util.prune_list_dict(global_id_to_domain_map)
    global_domain_to_id_map = extract_id_knowledge.map_domains_to_known_ids(global_id_to_domain_map)
    
    global_id_to_domain_counts = census_util.sort_tuples([(key, len(global_id_to_domain_map[key])) for key in global_id_to_domain_map])
    print(global_id_to_domain_counts)
    global_id_to_dm = list()
    for x in global_id_to_domain_counts:
        global_id_to_dm.append(x[1])
        print(str(x[0]) + ", " + str(x[1]))

    global_domain_to_id_counts = census_util.sort_tuples([(key, len(global_domain_to_id_map[key])) for key in global_domain_to_id_map])
    global_dm_to_id = list()
    for domain, count in global_domain_to_id_counts:
        global_dm_to_id.append(count)

    global_id_cookies_in_sync = [cookie for key in global_id_to_domain_map for cookie in global_id_to_cookie_map[key]]
    fp, tp = classify_domains.get_fp_tp_counts(global_domain_to_id_map)

    print("\n===========================================================================================\n")
    print("\n################################## ID TO COOKIE MAP #######################################\n")
    print(global_id_to_cookie_map)
    print("\n===========================================================================================\n")
    print("\n===========================================================================================\n")
    print("\n###################################### KNOWN IDs ##########################################\n")
    print(global_known_ids)
    print("\n===========================================================================================\n")
    print("\n===========================================================================================\n")
    print("\n################################## ID TO DOMAIN MAP #######################################\n")
    print(global_id_to_domain_map)
    print("\n===========================================================================================\n")
    print("\n===========================================================================================\n")
    print("\n################################## DOMAIN TO ID MAP #######################################\n")
    print(global_domain_to_id_map)
    print("\n===========================================================================================\n")

    # AGGREGATED STATS
    print("\n\n\n===========================================================================================")
    print("\nAggregated Summary statistics:")
    print("NUMBER OF IDs: " + str(len(global_id_to_cookie_map)))
    print("NUMBER OF ID COOKIES: " + str(len(global_known_ids)))
    print("NUMBER OF IDs IN SYNCS: " + str(len(global_id_to_domain_map)))
    print("NUMBER OF ID COOKIES IN SYNC: " + str(len(list(set(global_id_cookies_in_sync)))))
    print("NUMBER OF DOMAINS IN SYNC: " + str(len(global_domain_to_id_map)))
    print("NUMBER OF FP DOMAINS IN SYNC: " + str(fp))
    print("NUMBER OF TP DOMAINS IN SYNC: " + str(tp))
    print("                         Min | Mean | Median | Max")
    print("IDs KNOWN PER PARTY    :  " + str(min(global_dm_to_id)) + " | "  + str(round(numpy.mean(global_dm_to_id), 2)) + " | " + str(round(numpy.median(global_dm_to_id), 2)) + " | " + str(max(global_dm_to_id)))
    print("PARTIES KNOWING AN ID  :  " + str(min(global_id_to_dm)) + " | "  + str(round(numpy.mean(global_id_to_dm), 2)) + " | " + str(round(numpy.median(global_id_to_dm), 2)) + " | " + str(max(global_id_to_dm)))
    print("\n===========================================================================================\n\n\n")
