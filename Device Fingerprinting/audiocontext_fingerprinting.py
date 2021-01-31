import sqlite3
import operator
import requests
import numpy as np
import pandas as pd
import seaborn as sns

homepages = list(pd.read_csv('news_homepage_urls.csv')['news_url'])

conn = sqlite3.connect('./topics_url_crawls/topics_url_crawl4/crawl-data_all_topics4.sqlite')
c = conn.cursor()

fp_script_sites_dict = {}
total_scripts = 0
sites_with_fingerprint = []
script_list = []
homepage_visit_ids = []

for row in c.execute('SELECT visit_id, site_url FROM site_visits'):
    if row[1] in homepages:
        homepage_visit_ids.append(row[0])

for row in c.execute('SELECT visit_id, script_url, top_level_url, symbol FROM javascript'):
    if row[0] in homepage_visit_ids:
        if row[3].startswith('OfflineAudioContext') or row[3].startswith('OscillatorNode') or row[3].startswith('AudioContext'):
            #print(row[1], row[2], row[3])
            total_scripts += 1
            sites_with_fingerprint.append(row[2])
            script_list.append(row[1])
            if row[1] not in fp_script_sites_dict:
                fp_script_sites_dict[row[1]] = [row[2]]
            else:
                fp_script_sites_dict[row[1]].append(row[2])
conn.close()

unique_scripts = list(set(script_list))
false_positives = []

print('Total scripts:', total_scripts)
print('Total unique scripts:', len(unique_scripts))
print('Total sites in which fingerprinting is present:', len(set(sites_with_fingerprint)))
print(unique_scripts)
for fp_script in fp_script_sites_dict:
    fp_script_sites_dict[fp_script] = set(fp_script_sites_dict[fp_script])
print(fp_script_sites_dict)
