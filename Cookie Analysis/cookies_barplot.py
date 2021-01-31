'''
Bar Plot for #cookies in desktop sites
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# sites = ['sandesh.com', 'huffingtonpost.in', 'dinamalar.com', 'deccanherald.com', 'dnaindia.com', 'zeenews.india.com', 'jagran.com',
#             'hindi.news24online.com', 'timesnownews.com', 'deccanherald.com']
# num_cookies = [1557, 999, 877, 655, 634, 612, 584, 472, 454, 418]
#
# plt.bar(sites, num_cookies)
# plt.xlabel('News desktop sites')
# plt.ylabel('Median number of cookies')
# plt.xticks(rotation=70)
# plt.show()


# Bar Plot for #cookies in mobile sites
# mob_sites = ['m.economictimes.com', 'm.timesofindia.com', 'm.aajtak.in', 'm.punjabkesari.in', 'm.businesstoday.in', 'm.jagran.com',
#             'm.mid-day.com', 'm.hindustantimes.com', 'm.livemint.com', 'm.republicworld.com']
# num_cookies = [253, 209, 199, 173, 88, 76, 63, 59, 49, 41]
#
# plt.bar(mob_sites, num_cookies)
# plt.xlabel('News mobile sites')
# plt.ylabel('Number of cookies')
# plt.xticks(rotation=70)
# plt.show()


# Combined #cookies analysis for desktop and mobile sites
sites = ['Aajtak', 'Economic Times', 'Telegraph India', 'Mid-day', 'Times of India', 'Punjab Kesari', 'Business Today',
            'Lokmat', 'Live Hindustan', 'Webdunia', 'Hindustan Times', 'Livemint', 'Jagran', 'The Wire', 'Daily Hunt',
            'Andhra Jyothy', 'Patrika', 'Republic World', 'Business Standard', 'Great Andhra', 'Eenadu',
            'Tribune India', 'Deshabhimani']
mob_num_cookies = [140, 130, 121, 119, 107, 100, 89, 45, 42, 42, 42, 36, 34, 31,
                    29, 28, 22, 21, 17, 10, 8, 7, 5]
dsk_num_cookies = [174, 345, 255, 199, 49, 86, 155, 97, 130, 172, 151, 60, 387, 103,
                    16, 39, 124, 51, 167, 86, 80, 43, 30]

# world_cookies = [0, 382, 0, 79, 0, 522, 0, 427, 0, 29, 0, 141, 13, 264,
#                 75, 34, 21, 0, 119, 14, 213]
# india_cookies = [392, 349, 284, 73, 0, 479, 280, 420, 0, 28, 35, 137, 13, 310,
#                 300, 56, 20, 0, 119, 72, 231]
# entertainment_cookies = [0, 455, 266, 84, 0, 533, 282, 402, 0, 27, 0, 227, 13,
#                         145, 55, 172, 19, 9, 151, 31, 208]
# sports_cookies = [0, 114, 196, 57, 0, 535, 300, 454, 0, 29, 20, 230, 13, 284,
#                     359, 60, 21, 0, 176, 32, 225]

leaning = ['R', 'C', 'L', 'C', 'C', 'L', 'C',
            'L', 'C', 'R', 'L', 'C', 'R', 'L', 'R',
            'L', 'R', 'R', 'C', 'L', 'L', 'C', 'L']

dsk_color_list = []
for l in leaning:
    if l == 'L':
        dsk_color_list.append('red')
    elif l == 'R':
        dsk_color_list.append('blue')
    elif l == 'C':
        dsk_color_list.append('yellow')

mob_color_list = []
for l in leaning:
    if l == 'L':
        mob_color_list.append('pink')
    elif l == 'R':
        mob_color_list.append('lightblue')
    elif l == 'C':
        mob_color_list.append('lightyellow')


indx = np.arange(23)

bar1 = plt.bar(indx-0.3/2, mob_num_cookies, color=dsk_color_list, width=0.3, align='center', linestyle='--', edgecolor='black')
bar2 = plt.bar(indx+0.3/2, dsk_num_cookies, color=dsk_color_list, width=0.3, align='center', edgecolor='black')
#bar3 = plt.bar(indx-0.1/2, world_cookies, width=0.1, color='g', align='center')
# bar4 = plt.bar(indx+0.1/2, india_cookies, width=0.1, color='y', align='center')
# bar5 = plt.bar(indx+0.1/2+0.1, entertainment_cookies, width=0.1, color='orange', align='center')
# bar6 = plt.bar(indx+0.1/2+0.2, sports_cookies, width=0.1, color='grey', align='center')

plt.xticks(indx, sites, rotation=90, size=12)
plt.xlabel('News Websites', size=12)
plt.ylabel('Median Number of Cookies', size=12)
plt.legend((bar2[2], bar2[1], bar2[0], bar1[2], bar1[1], bar1[0]),
            ('Left (Desktop)', 'Centre (Desktop)', 'Right (Desktop)', 'Left (Mobile)', 'Centre (Mobile)', 'Right (Mobile)')) #, 'Subdomain: World', 'Subdomain: India', 'Subdomain: Entertainment', 'Subdomain: Sports'))
plt.show()

# res = [[mob_num_cookies[i], dsk_num_cookies[i]] for i in range(len(mob_num_cookies))]
# df = pd.DataFrame(res)
# print(df.head(5))
# print('Correlation b/w #cookies in mobile and desktop sites:', df.corr())
