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
        if row[3].startswith('RTCPeerConnection') or row[3].startswith('localDescription'):
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
print(unique_scripts)
print(sites_with_fingerprint)

# print('\nFingerprinting Scripts:')
# for script_url in unique_scripts:
#     if not check_false_positive(script_url):
#         print(script_url)
#     else:
#         false_positives.append(script_url)
#
# print('False positive count:', len(false_positives), '\n')
# print(false_positives)

#Results: ##############################################################

# Total scripts: 22
# Total unique scripts: 1
# Total sites in which fingerprinting is present: 2
# Unique Script: ['https://static.adsafeprotected.com/sca.17.4.114.js']
# Sites with WebRTCFP: ['https://www.huffingtonpost.in/', 'https://www.firstpost.com/']
