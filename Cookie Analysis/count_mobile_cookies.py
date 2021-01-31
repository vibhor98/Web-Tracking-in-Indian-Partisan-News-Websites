'''
Counts median cookies for mobile websites.
'''

import csv
import os
import pandas as pd
import statistics as stats
import operator

folders = ['/', '/mobile_crawl2_29.08.2020/', '/mobile_crawl3_29.08.2020/', '/mobile_crawl4_27.08.2020/', '/mobile_crawl5_27.08.2020/']

site_cookies_dict = {}

for folder in folders:
    files = [fi for fi in os.listdir('./mobilesite_cookies' + folder) if os.path.isfile('./mobilesite_cookies' + folder + fi)]
    for file in files:
        if not file.startswith('.'):
            #print('./mobilesite_cookies'+folder+file)
            f = list(csv.reader(open('./mobilesite_cookies'+folder+file, 'r'), delimiter='\t'))
            if f[0][0].startswith('# '):
                f = f[4:]

            if file not in site_cookies_dict:
                site_cookies_dict[file] = [len(f)]
            else:
                site_cookies_dict[file].append(len(f))

#print(site_cookies_dict)
for site in site_cookies_dict:
    #site_cookies_dict[site] = stats.median(site_cookies_dict[site])
    print(site, site_cookies_dict[site])

# site_cookies_dict = sorted(site_cookies_dict.items(), key=operator.itemgetter(1), reverse=True)
# print(site_cookies_dict)
#
# print([val[1] for val in site_cookies_dict])

#{'m.jagran.com.txt': 34, 'm.businesstoday.in.txt': 89, 'm.tribuneindia.com.txt': 7, 'm.timesofindia.com.txt': 107, 'm.andhrajyothy.com.txt': 28, 'm.aajtak.in.txt': 140, 'm.republicworld.com.txt': 21, 'm.thewire.in.txt': 31, 'm.greatandhra.com.txt': 10, 'm.punjabkesari.in.txt': 100, 'm.livehindustan.com.txt': 42, 'm.mid-day.com.txt': 119, 'm.patrika.com.txt': 22, 'm.lokmat.com.txt': 45, 'm-hindi.webdunia.com.txt': 42, 'm.livemint.com.txt': 36, 'm.deshabhimani.com.txt': 5, 'm.dailyhunt.in.txt': 29, 'm.economictimes.com.txt': 130, 'm.hindustantimes.com.txt': 42, 'm.eenadu.net.txt': 8, 'm.telegraphindia.com.txt': 121.0, 'wap.business-standard.com.txt': 17.0}
