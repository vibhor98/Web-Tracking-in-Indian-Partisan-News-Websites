# Finds #invisible images for each news website along with its leaning.
import pandas as pd
import numpy as np
import statistics as stats

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

def find_website_leaning(url):
    url = url.split('/')[2]
    url_list = url.split('.')
    if len(url_list) == 2:
        url = url_list[0]
    elif len(url_list) >= 3:
        url = url_list[1]

    if url in left:
        return 'left'
    elif url in right:
        return 'right'
    elif url in centre:
        return 'centre'
    elif url in unknown:
        return 'unknown'
    else:
        print('%s is not present in any leaning.' % url)
        return None

df = pd.read_csv('./inv_pixel_imgs_1x1.csv')

site_imgurl_dict = {}
size = len(df)

for i in range(size):
    row = df.iloc[i]
    if row['news_site'] not in site_imgurl_dict:
        site_imgurl_dict[row['news_site']] = 1
    else:
        site_imgurl_dict[row['news_site']] += 1

res = []
for k in site_imgurl_dict:
    leaning = find_website_leaning(k)
    if leaning:
        res.append([k, site_imgurl_dict[k], leaning])

df_res = pd.DataFrame(res, columns=['news_site', '#inv_imgs', 'leaning'])
df_res.sort_values(by=['#inv_imgs'], inplace=True, ascending=False)
df_res.to_csv('inv_px_site_dom.csv', index=False)

# df = pd.read_csv('inv_px_site_dom.csv')
#
# num_left = 0
# num_right = 0
# num_centre = 0
# num_unk = 0
# left_imgs = []
# right_imgs = []
# centre_imgs = []
# unk_imgs = []
#
# for i in range(len(df)):
#     row = df.iloc[i]
#     if row['leaning'] == 'left':
#         num_left += 1
#         left_imgs.append(row['#inv_imgs'])
#     elif row['leaning'] == 'right':
#         num_right += 1
#         right_imgs.append(row['#inv_imgs'])
#     elif row['leaning'] == 'centre':
#         num_centre += 1
#         centre_imgs.append(row['#inv_imgs'])
#     elif row['leaning'] == 'unknown':
#         num_unk += 1
#         unk_imgs.append(row['#inv_imgs'])
#     else:
#         print(row)
#
# print('No. of left sites:', num_left)
# print('Median imgs in left sites:', stats.median(left_imgs))
#
# print('No. of right sites:', num_right)
# print('Median imgs in right sites:', stats.median(right_imgs))
#
# print('No. of centre sites:', num_centre)
# print('Median imgs in centre sites:', stats.median(centre_imgs))
#
# print('No. of unknown sites:', num_unk)
# print('Median imgs in unknown sites:', stats.median(unk_imgs))

#RESULTS ####################################################
# No. of left sites: 35
# Median imgs in left sites: 12
# No. of right sites: 40
# Median imgs in right sites: 10.0
# No. of centre sites: 25
# Median imgs in centre sites: 15
# No. of unknown sites: 18
# Median imgs in unknown sites: 4.5
