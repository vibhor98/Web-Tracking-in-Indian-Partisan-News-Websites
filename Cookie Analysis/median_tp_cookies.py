import sqlite3
import operator
import statistics
import numpy as np
import pandas as pd

homepages = list(pd.read_csv('news_homepage_urls.csv')['news_url'])
#print(homepages)

total_cookies = 0
domain_sites_dict = {}

for i in range(1, 6):
    conn = sqlite3.connect('./topics_url_crawls/topics_url_crawl' + str(i) + '/crawl-data_all_topics' + str(i) + '.sqlite')
    c = conn.cursor()

    visitid_homepage_dict = {}

    for row in c.execute('SELECT visit_id, site_url FROM site_visits'):
        if row[1] in homepages:
            visitid_homepage_dict[row[0]] = row[1]
    #print(homepage_visit_ids)

    for row in c.execute('SELECT visit_id, host FROM javascript_cookies'):
        if row[0] in visitid_homepage_dict:
            if row[1].startswith('.'):
                host = row[1][1:]
            else:
                host = row[1]

            if host.startswith('www'):
                host = '.'.join(host.split('.')[1:])

            if len(host.split('.')) >= 3 and host[-5:]!='co.in' and host[-5:]!='co.uk':
                host = '.'.join(host.split('.')[-2:])

            if host in domain_sites_dict:
                domain_sites_dict[host][i-1] += 1
            else:
                domain_sites_dict[host] = [0,0,0,0,0]
                domain_sites_dict[host][i-1] = 1
            total_cookies += 1
    conn.close()

tp_median_cookies = {}
for dom in domain_sites_dict:
    tp_median_cookies[dom] = statistics.median(domain_sites_dict[dom])

tp_not_found_df = []

df_agg = pd.read_csv('./agg_inv_px.csv')
tp_to_indx_dict = {}
for i in range(len(df_agg)):
    tp_to_indx_dict[df_agg.iloc[i]['Domains']] = i

for dom in tp_median_cookies:
    if dom in tp_to_indx_dict:
        indx = tp_to_indx_dict[dom]
        df_agg.at[indx, 'CB_extent'] = tp_median_cookies[dom]
    else:
        print(dom, 'not found.')
        tp_not_found_df.append([dom,'','', tp_median_cookies[dom],'','','','','','','','','','',''])

tp_not_found_df = pd.DataFrame(tp_not_found_df, columns=['Domains','FP_flag','CB_flag','CB_extent','CS_flag','CS_extent','FP_flag','FP_extent','IP_flag','IP_extent','Diversity_Score','Wt_Diversity_Score','','',''])
#df_agg.append(tp_not_found_df, ignore_index=True)
df_agg.to_csv('agg_cookie_based_results.csv', index=False)
tp_not_found_df.to_csv('agg_cb_not_found.csv', index=False)

print('Total cookies:', total_cookies)
