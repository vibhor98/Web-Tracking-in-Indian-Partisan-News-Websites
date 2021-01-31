# This script finds top third-party domains setting invisible pixels.
import pandas as pd
from collections import Counter

# LEFT_TO_LEFTCENTRE (39)
left = ["ndtv24x7","indianexpress","hindustantimes","punjabkesari","thehindu","anandabazar","scoopwhoop","ndtv","sandesh","dinamalar","mathrubhumi",
		"lokmat","greaterkashmir","scroll","siasat","andhrajyothy","kashmirlife","outlookindia","eenadu","huffingtonpost","thenewsminute","thewire",
		"youthkiawaaz","thehindubusinessline","risingkashmir","milligazette","mumbaimirror","thestatesman","telegraphindia","deshabhimani","newslaundry",
		"bangaloremirror","altnews","kashmirreader","countercurrents","ahmedabadmirror","punemirror","timesheadline","greatandhra"]

# RIGHT_TO_RIGHTCENTRE (38)
right = ["aajtak","intoday","jagran","bhaskar","zeenews","indiatvnews","abplive","amarujala","indiatimes","navbharattimes","patrika","news18","timesnownews","newsonair", "nic",
		 "newindianexpress","india","firstpost","republicworld","newslivetv","deccanchronicle","fakingnews","dnaindia","gujaratsamachar","dailyhunt",
		 "newdelhitimes","webdunia","moneycontrol","newsnation","newsnationtv","swarajyamag","aninews","dailyo","forbesindia","dailyexcelsior","oneindia","opindia",
		 "starofmysore","dailypioneer","ians"]

# CENTRE_AND_LEASTBIASED (28)
centre = ["timesofindia","indiatoday","news24","news24online","bbc","thequint","jansatta","economictimes","mid-day","dailythanthi","manoramaonline",
		  "livehindustan","financialexpress","cnbctv18","businesstoday","livemint","catchnews","businessinsider","deccanherald","theprint","wionews",
		  "ptinews","business-standard","tribuneindia","headlinesoftoday","nagpurtoday","asianage","freepressjournal"]

# N/A (20)
unknown = ["rvcj","thelogicalindian","brutindia","brut","thebetterindia","pinkvilla","topyaps","telanganatoday","wisden","statetimes","sentinelassam","assamtribune",
		   "socialsamosa","newstracklive","leagueofindia","prabhatkhabar","thesangaiexpress","news4masses","sinceindependence","5abnow","factchecker"]


def find_website_leaning(host, sites_list):
    sites_dict = dict(Counter(sites_list))
    domain_img_count[host] = ([0, 0, 0, 0], [0, 0, 0, 0])
    for url in sites_dict:
        orig_url = url
        url = url.split('/')[2]
        url_list = url.split('.')
        if len(url_list) == 2:
            url = url_list[0]
        elif len(url_list) >= 3:
            url = url_list[1]

        if url in left:
            domain_img_count[host][0][0] += 1
            domain_img_count[host][1][0] += sites_dict[orig_url]
        elif url in right:
            domain_img_count[host][0][1] += 1
            domain_img_count[host][1][1] += sites_dict[orig_url]
        elif url in centre:
            domain_img_count[host][0][2] += 1
            domain_img_count[host][1][2] += sites_dict[orig_url]
        elif url in unknown:
            domain_img_count[host][0][3] += 1
            domain_img_count[host][1][3] += sites_dict[orig_url]
        else:
            print('%s is not present in any leaning.' % url)

df = pd.read_csv('./inv_pixel_imgs_1x1.csv')
domain_site_map = {}

for i in range(len(df)):
    row = df.iloc[i]
    img_url = row['image_url']
    tp_domain = img_url.split('/')[2]
    if tp_domain.startswith('www'):
        tp_domain  = '.'.join(tp_domain.split('.')[1:])

    # if len(tp_domain.split('.')) >= 3 and tp_domain[-5:]!='co.in' and tp_domain[-5:]!='co.uk':
    #     tp_domain  = '.'.join(tp_domain.split('.')[-2:])

    if tp_domain not in domain_site_map:
        domain_site_map[tp_domain] = [row['news_site']]
    else:
        domain_site_map[tp_domain].append(row['news_site'])

domain_img_count = {}
for key in domain_site_map:
    find_website_leaning(key, domain_site_map[key])
    #domain_img_count[key] = (len(domain_site_map[key]), len(set(domain_site_map[key])))

sorted_dom_img_count = sorted(domain_img_count.items(), key=lambda e: sum(e[1][1]), reverse=True)

print('#third-party domains:', len(sorted_dom_img_count))

count = 0
for tup in sorted_dom_img_count:
    print(tup)
    count += 1
    if count > 10:
        break
# tp_not_found_df = []
#
# for key in domain_site_map:
#     domain_img_count[key] = len(domain_site_map[key])
#
# df_agg = pd.read_csv('./aggregated_tp_dom.csv')
# tp_to_indx_dict = {}
# for i in range(len(df_agg)):
#     tp_to_indx_dict[df_agg.iloc[i]['Domains']] = i
#
# for dom in domain_img_count:
#     if dom in tp_to_indx_dict:
#         indx = tp_to_indx_dict[dom]
#         df_agg.at[indx, 'IP_extent'] = domain_img_count[dom]
#     else:
#         print(dom, 'not found.')
#         tp_not_found_df.append([dom,'','','','','','','','', domain_img_count[dom],'','','','',''])
#
# tp_not_found_df = pd.DataFrame(tp_not_found_df, columns=['Domains','FP_flag','CB_flag','CB_extent','CS_flag','CS_extent','FP_flag','FP_extent','IP_flag','IP_extent','Diversity_Score','Wt_Diversity_Score','','',''])
# #df_agg.append(tp_not_found_df, ignore_index=True)
# df_agg.to_csv('agg_inv_px.csv', index=False)
# tp_not_found_df.to_csv('add_ip_not_found.csv', index=False)
