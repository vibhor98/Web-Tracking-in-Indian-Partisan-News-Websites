import pandas as pd

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


df = pd.read_csv('./dsk_home_median_cookies.csv')

for i in range(len(df)):
	row = df.iloc[i]
	url = row['homepage']
	url = url.split('/')[2]
	url_list = url.split('.')
	if len(url_list) == 2:
		url = url_list[0]
	elif len(url_list) >= 3:
		url = url_list[1]

	if url in left:
		df.at[i, 'leaning'] = 'left'
	elif url in right:
		df.at[i, 'leaning'] = 'right'
	elif url in centre:
		df.at[i, 'leaning'] = 'centre'
	elif url in unknown:
		df.at[i, 'leaning'] = 'unknown'
	else:
		print('%s is not present in any leaning.' % url)

#df.to_csv('./dsk_mob_crawl_wise_cookies.csv', index=False)
df.to_csv('./dsk_home_median_cookies.csv', index=False)
