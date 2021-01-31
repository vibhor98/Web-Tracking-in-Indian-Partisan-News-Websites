import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Barplot of top 10 websites vs. their invisible pixels
indx = np.arange(20)

top10 = {'sandesh.com': 261, 'dailythanthi.com': 143, 'anandabazar.com': 138,
'freepressjournal.in': 122, 'india.com': 101, 'oneindia.com': 78, 'telegraphindia.com': 71,
'zeenews.india.com': 70, 'timesnownews.com': 69, 'news18.com': 58, 'economictimes.com': 49,
'dinamalar.com': 46, 'deccanherald.com': 44, 'jagran.com': 43, 'thehindu.com': 38,
'punjabkesari.in': 37, 'huffingtonpost.in': 35, 'ndtv.com': 33, 'khabar.ndtv.com': 30, 'news24online.com': 29}

leaning = ['left', 'centre', 'left', 'centre', 'right', 'right',
            'left', 'right', 'right', 'right', 'right', 'left', 'centre',
            'right', 'left', 'left', 'left', 'left', 'left', 'centre']

color_list = []
for l in leaning:
    if l == 'left':
        color_list.append('red')
    elif l == 'right':
        color_list.append('blue')
    elif l == 'centre':
        color_list.append('yellow')

values = list(top10.values())
values = [i/2513.0 for i in values]

bar = plt.bar(indx, values, color=color_list, edgecolor='black', width=0.5)
#plt.plot(indx, list(top10.values()))

keys_list = list(top10.keys())

plt.xticks(indx, keys_list, rotation=90, size=12)
plt.xlabel('Top 20 News Websites', size=12)
plt.ylabel('Median Number of\nInvisible Pixels (normalized)', size=12)
plt.legend((bar[0], bar[1], bar[4]), ['Left', 'Centre', 'Right'])
plt.show()

############## (Code for Fig 11 -- TP plot for Inv Px)

# top10 = {'googlesyndication.com': ([23, 30, 17, 9], [73, 92, 57, 20]),
#             'casalemedia.com': ([12, 14, 8, 5], [96, 65, 45, 10]),
#             'rtb.gumgum.com': ([2, 1, 3, 0], [113, 17, 62, 0]),
#             'simage2.pubmatic.com': ([14, 13, 10, 3], [52, 61, 34, 12]),
#             'google-analytics.com': ([22, 15, 11, 7], [59, 29, 29, 18]),
#             'image2.pubmatic.com': ([10, 10, 7, 2], [41, 43, 30, 9]),
#             'rubiconproject.com': ([8, 11, 5, 1], [34, 54, 23, 5]),
#             'google.co.in': ([23, 26, 19, 11], [33, 33, 27, 17]),
#             'us-u.openx.net': ([7, 9, 5, 2], [26, 24, 14, 5]),
#             'ib.adnxs.com': ([11, 13, 7, 6], [21, 21, 10, 7])}
#
# left_px = []
# right_px = []
# centre_px = []
# left_sites = []
# right_sites = []
# centre_sites = []
# keys_list = []
# px_list = []
#
# for k in top10:
#     keys_list.append(k)
#     v = top10[k]
#
#     left_sites.append(v[0][0] / 39.0 * 100)
#     right_sites.append(v[0][1] / 38.0 * 100)
#     centre_sites.append(v[0][2] / 28.0 * 100)
#     px_list.extend([v[1][0], v[1][2], v[1][1]])
#     # left_px.append(v[1][0])
#     # right_px.append(v[1][1])
#     # centre_px.append(v[1][2])
#
# px_indx = []
# for i in indx:
#     px_indx.extend([i-0.2, i, i+0.2])
#
# fig, ax = plt.subplots(nrows=2, ncols=1)
# bar1 = ax[1].bar(indx-0.2, left_sites, align='center', color='red', edgecolor='black', width=0.2)
# bar2 = ax[1].bar(indx, centre_sites, align='center', color='yellow', edgecolor='black', width=0.2)
# bar3 = ax[1].bar(indx+0.2, right_sites, align='center', color='blue', edgecolor='black', width=0.2)
#
# #ax2 = ax1.twinx()
# ax[0].plot(px_indx, px_list, marker='o')
#
# ax[1].set_xticks(indx)
# ax[1].set_xticklabels(keys_list, rotation=90, size=12)
#
# ax[0].set_xticklabels([])
#
# ax[1].set_xlabel('Top 10 Third-Party Domains (setting invisible pixels)', size=12)
# ax[1].set_ylabel('% of News Websites', size=12)
# ax[0].set_ylabel('Number of Invisible Pixels', size=12)
#
# ax[1].legend((bar1[0], bar2[0], bar3[0]), ('Left', 'Centre', 'Right'))
# plt.show()
