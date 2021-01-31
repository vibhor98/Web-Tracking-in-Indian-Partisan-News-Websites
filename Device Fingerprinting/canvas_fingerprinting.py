import sqlite3
import operator
import requests
import numpy as np
import pandas as pd
import seaborn as sns

def check_false_positive(script_url):
    script = requests.get(script_url).text
    if not ('toDataURL' in script or 'getImageData' in script):
        return True
    if script.find('fillText') >= 0:
        indx = script.find('fillText')
        print('\n', script[indx : indx+50])
    return False

homepages = list(pd.read_csv('news_homepage_urls.csv')['news_url'])
#print(homepages)

conn = sqlite3.connect('./topics_url_crawls/topics_url_crawl4/crawl-data_all_topics4.sqlite')
c = conn.cursor()

domain_sites_dict = {}
total_scripts = 0
sites_with_fingerprint = []
script_list = []
homepage_visit_ids = []

for row in c.execute('SELECT visit_id, site_url FROM site_visits'):
    if row[1] in homepages:
        homepage_visit_ids.append(row[0])
#print(homepage_visit_ids)

for row in c.execute('SELECT visit_id, script_url, top_level_url, symbol FROM javascript'):
    if row[0] in homepage_visit_ids:
        if row[3].startswith('HTMLCanvasElement') or row[3].startswith('CanvasRenderingContext2D'):
            #print(row[1], row[2], row[3])
            total_scripts += 1
            sites_with_fingerprint.append(row[2])
            script_list.append(row[1])
conn.close()

unique_scripts = list(set(script_list))
false_positives = []

print('Total scripts:', total_scripts)
print('Total unique scripts:', len(unique_scripts))
print('Total sites in which fingerprinting is present:', len(set(sites_with_fingerprint)))

print('\nFingerprinting Scripts:')
for script_url in unique_scripts:
    if not check_false_positive(script_url):
        print(script_url)
    else:
        false_positives.append(script_url)

print('False positive count:', len(false_positives), '\n')
print(false_positives)
# for site in list(set(script_list)):
#     print(site)

# domain_sites_count = {}
# for host in domain_sites_dict:
#     domain_sites_count[host] = len(set(domain_sites_dict[host]))

# Sort dict in descending order of #cookies from each unique domain.
# sorted_dom_dict = sorted(domain_sites_count.items(), key=operator.itemgetter(1), reverse=True)
