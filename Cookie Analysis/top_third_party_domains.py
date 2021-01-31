'''
This script finds the top third-party domains (TPs) setting cookies in the news websites.
Also, finds top 10 TPs and plots a barplot.
'''

import sqlite3
import matplotlib.pyplot as plt
import operator
import numpy as np
import pandas as pd
import seaborn as sns

# LEFT_TO_LEFTCENTRE
left = ["ndtv24x7","indianexpress","hindustantimes","punjabkesari","thehindu","anandabazar","scoopwhoop","ndtv","sandesh","dinamalar","mathrubhumi",
		"lokmat","greaterkashmir","scroll","siasat","andhrajyothy","kashmirlife","outlookindia","eenadu","huffingtonpost","thenewsminute","thewire",
		"youthkiawaaz","thehindubusinessline","risingkashmir","milligazette","mumbaimirror","thestatesman","telegraphindia","deshabhimani","newslaundry",
		"bangaloremirror","altnews","kashmirreader","countercurrents","ahmedabadmirror","punemirror","timesheadline","greatandhra"]

# RIGHT_TO_RIGHTCENTRE
right = ["aajtak","intoday","jagran","bhaskar","zeenews","indiatvnews","abplive","amarujala","indiatimes","navbharattimes","patrika","news18","timesnownews","newsonair", "nic",
		 "newindianexpress","india","firstpost","republicworld","newslivetv","deccanchronicle","fakingnews","dnaindia","gujaratsamachar","dailyhunt",
		 "newdelhitimes","webdunia","moneycontrol","newsnation","newsnationtv","swarajyamag","aninews","dailyo","forbesindia","dailyexcelsior","oneindia","opindia",
		 "starofmysore","dailypioneer","ians"]

# CENTRE_AND_LEASTBIASED
centre = ["timesofindia","indiatoday","news24","news24online","bbc","thequint","jansatta","economictimes","mid-day","dailythanthi","manoramaonline",
		  "livehindustan","financialexpress","cnbctv18","businesstoday","livemint","catchnews","businessinsider","deccanherald","theprint","wionews",
		  "ptinews","business-standard","tribuneindia","headlinesoftoday","nagpurtoday","asianage","freepressjournal"]

# UNKNOWN
unknown = ["rvcj","thelogicalindian","brutindia","brut","thebetterindia","pinkvilla","topyaps","telanganatoday","wisden","statetimes","sentinelassam","assamtribune",
		   "socialsamosa","newstracklive","leagueofindia","prabhatkhabar","thesangaiexpress","news4masses","sinceindependence","5abnow","factchecker"]


def find_website_leaning(host, sites_list):
	domain_sites_count[host] = [0, 0, 0, 0]
	for url in sites_list:
		url = url.split('/')[2]
		url_list = url.split('.')
		if len(url_list) == 2:
			url = url_list[0]
		elif len(url_list) >= 3:
			url = url_list[1]

		if url in left:
			domain_sites_count[host][0] += 1
		elif url in right:
			domain_sites_count[host][1] += 1
		elif url in centre:
			domain_sites_count[host][2] += 1
		elif url in unknown:
			domain_sites_count[host][3] += 1
		else:
			print('%s is not present in any leaning.' % url)


homepages = list(pd.read_csv('news_homepage_urls.csv')['news_url'])
#print(homepages)

conn = sqlite3.connect('./topics_url_crawls/topics_url_crawl4/crawl-data_all_topics4.sqlite')
c = conn.cursor()

domain_sites_dict = {}
domain_sites_dict_multiple = {}
total_cookies = 0
homepage_visit_ids = {}

for row in c.execute('SELECT visit_id, site_url FROM site_visits'):
	if row[1] in homepages:
		#homepage_visit_ids.append(row[0])
		#homepage_visit_ids[row[0]] = homepages.index(row[1]) + 1
		homepage_visit_ids[row[0]] = row[1]
#print(homepage_visit_ids)

for row in c.execute('SELECT visit_id, host FROM javascript_cookies'):
	if row[0] in homepage_visit_ids:
		if row[1].startswith('.'):
			host = row[1][1:]
		else:
			host = row[1]

		if host in domain_sites_dict_multiple:
			domain_sites_dict_multiple[host].append(homepage_visit_ids[row[0]])
		else:
			domain_sites_dict_multiple[host] = [homepage_visit_ids[row[0]]]
		total_cookies += 1
conn.close()

domain_sites_count = {}
for host in domain_sites_dict_multiple:
	#domain_sites_count[host] = len(set(domain_sites_dict[host]))

	# For calculating Prominence.
	# domain_sites_dict[host] = list(set(domain_sites_dict[host]))
	# for site_id in domain_sites_dict[host]:
	#     if host not in domain_sites_count:
	#         domain_sites_count[host] = 1.0 / homepage_visit_ids[site_id]
	#     else:
	#         domain_sites_count[host] += 1.0 / homepage_visit_ids[site_id]

	# For calculating leaning-wise % websites.
	if host == 'economictimes.indiatimes.com':
		domain_sites_dict['economictimes.com'] = list(set(domain_sites_dict_multiple[host]))
		host = 'economictimes.com'
	else:
		domain_sites_dict[host] = list(set(domain_sites_dict_multiple[host]))
	find_website_leaning(host, domain_sites_dict[host])

# Sort dict in descending order of #cookies from each unique domain.
sorted_dom_dict = sorted(domain_sites_count.items(), key=lambda e: sum(e[1]), reverse=True)
print('Total cookies:', total_cookies)
print('Total unique third-party domains:', len(sorted_dom_dict))

count = 0
cookies_by_top10 = 0
top_15 = {}
# 40 37 26
for k, v in sorted_dom_dict:
	cookies_by_top10 += len(domain_sites_dict_multiple[k])
	top_15[k] = [ (v[0]/39.0)*100, (v[1]/38.0)*100, (v[2]/28.0)*100 ]
	count += 1
	if count == 10:
		break

print('Total cookies by top 10 third-parties:', cookies_by_top10)

indx = np.arange(10)
keys_list = list(top_15.keys())

values = list(top_15.values())
values[0][1] = values[0][1] - (2/38.0)*100
left_vals = [x[0] for x in values]
right_vals = [x[1] for x in values]
center_vals = [x[2] for x in values]
general_web = [21, 8.2, 3.9, 1.3, 1.3, 3.6, 2.7, 0.4, 2, 2.3]


bar1 = plt.bar(indx-0.3, left_vals, align='center', color='red', edgecolor='black', width=0.2)
bar2 = plt.bar(indx-0.1, center_vals, align='center', color='yellow', edgecolor='black', width=0.2)
bar3 = plt.bar(indx+0.1, right_vals, align='center', color='blue', edgecolor='black', width=0.2)
bar4 = plt.bar(indx+0.3, general_web, align='center', color='black', edgecolor='black', width=0.2)

plt.xticks(indx, keys_list, rotation=90, size=12)
plt.xlabel('Top 10 Third-Party Domains (setting cookies)', size=12)
plt.ylabel('% of Websites', size=12)
plt.legend((bar1[0], bar2[0], bar3[0], bar4[0]), ('Left', 'Centre', 'Right', 'General Web'))
plt.show()
