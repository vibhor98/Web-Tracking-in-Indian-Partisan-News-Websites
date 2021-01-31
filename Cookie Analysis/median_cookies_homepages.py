'''
This script computes the median no. of cookies using sqlite DBs after 5 stateless crawls.
Also, finds the top 15 news websites with the highest no. of cookies and plots a barplot.  
'''

import sqlite3
import matplotlib.pyplot as plt
import operator
import statistics
import numpy as np
import pandas as pd
import seaborn as sns

homepages = list(pd.read_csv('news_homepage_urls.csv')['news_url'])
#print(homepages)
results = {}

for i in range(1, 6):
    conn = sqlite3.connect('./topics_url_crawls/topics_url_crawl' + str(i) + '/crawl-data_all_topics' + str(i) + '.sqlite')
    c = conn.cursor()

    visitid_homepage_dict = {}

    for row in c.execute('SELECT visit_id, site_url FROM site_visits'):
        if row[1] in homepages:
            visitid_homepage_dict[row[0]] = row[1]
    #print(homepage_visit_ids)

    for row in c.execute('SELECT visit_id, count(*) FROM javascript_cookies GROUP BY visit_id'):
        if row[0] in visitid_homepage_dict:
            if visitid_homepage_dict[row[0]] not in results:
                results[visitid_homepage_dict[row[0]]] = [row[1]]
            else:
                results[visitid_homepage_dict[row[0]]].append(row[1])
    conn.close()

url_median_cookies = {}
res_list = []
for url in results:
    url_median_cookies[url] = statistics.median(results[url])
    # if len(results[url]) < 5:
    #     results[url].append(statistics.median(results[url]))
    #     print(url, results[url])
    # res_list.append([url, results[url][0], results[url][1], results[url][2], results[url][3], results[url][4], '', '', '', '', '', ''])

#Sort dict in descending order of median cookies for each unique news homepage.
sorted_dom_dict = sorted(url_median_cookies.items(), key=operator.itemgetter(1), reverse=True)
df = pd.DataFrame(sorted_dom_dict)
df.to_csv('dsk_home_median_cookies.csv', index=False)

# df = pd.DataFrame(res_list, columns=['homepage', 'dsk_cookies_crawl1', 'dsk_cookies_crawl2', 'dsk_cookies_crawl3', 'dsk_cookies_crawl4', 'dsk_cookies_crawl5',
#                                         'mob_cookies_crawl1', 'mob_cookies_crawl2', 'mob_cookies_crawl3', 'mob_cookies_crawl4', 'mob_cookies_crawl5', 'leaning'])
# df.to_csv('dsk_mob_crawl_wise_cookies.csv', index=False)

count = 0
top_15 = {}
for k, v in sorted_dom_dict:
    k = k.split('/')[2]
    top_15[k] = v
    count += 1
    if count == 15:
        break

print(top_15)

indx = np.arange(15)
plt.bar(indx, top_15.values(), edgecolor='black')
#sns.barplot(x=indx, y=list(top_15.values()), palette='rocket', edgecolor='black')

keys_list = list(top_15.keys())

plt.xticks(indx, keys_list, rotation=90, size=12)
plt.xlabel('Top 15 news websites', size=12)
plt.ylabel('Median number of cookies', size=12)
plt.show()
