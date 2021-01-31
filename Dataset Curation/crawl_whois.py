'''

This Code crawls the Whois Registration data for 123 news websites in our Dataset
Date: 06 May 2020

'''

# Necessary Imports
from bs4 import BeautifulSoup
import urllib.request

# List of 123 news website urls
url_list = ["https://aajtak.intoday.in/","https://www.jagran.com/","https://www.rvcj.com/category/news/","bhaskar.com","https://zeenews.india.com/","indiatvnews.com",
"timesofindia.indiatimes.com","indiatoday.in","https://hindi.news24online.com/","https://news.abplive.com/","https://www.bbc.com/hindi","ndtv.com","amarujala.com",
"Indiatimes.com","http://www.independent24.com/","https://navbharattimes.indiatimes.com/","indianexpress.com","https://www.news24.com/","thequint.com",
"https://www.patrika.com/","https://www.news18.com/","https://thelogicalindian.com/","Hindustantimes.com","https://www.timesnownews.com/","https://www.punjabkesari.in/",
"thehindu.com","https://www.anandabazar.com/","https://www.scoopwhoop.com","https://www.jansatta.com/","Economictimes.indiatimes.com","https://khabar.ndtv.com/","www.mid-day.com","https://www.dailythanthi.com/","http://www.newsonair.nic.in/","sandesh.com","https://www.dinamalar.com/","https://www.mathrubhumi.com/","Newindianexpress.com",
"https://www.brut.media/in","https://www.india.com/","firstpost.com","https://www.manoramaonline.com/","https://www.lokmat.com/","https://www.livehindustan.com/",
"www.thebetterindia.com","http://tribune.com.pk/","Greaterkashmir.com","https://www.republicworld.com/","https://www.financialexpress.com/","https://www.newslivetv.com/",
"https://bharat.republicworld.com/","https://www.pinkvilla.com/","https://www.cnbctv18.com/","scroll.in","https://www.businesstoday.in/","deccanchronicle.com",
"Siasat.com","http://www.fakingnews.com/","https://www.dnaindia.com/", "https://andhrajyothy.com/","https://www.gujaratsamachar.com/","https://m.dailyhunt.in/news/",
"www.newdelhitimes.com","https://kashmirlife.net/","https://www.outlookindia.com/","Livemint.com","http://www.catchnews.com","https://www.eenadu.net/",
"https://www.huffingtonpost.in/","https://hindi.webdunia.com/","www.thenewsminute.com","https://www.moneycontrol.com/","www.businessinsider.in","topyaps.com",
"https://www.newsnation.in/","https://thewire.in/","Deccanherald.com","www.youthkiawaaz.com","thehindubusinessline.com","https://swarajyamag.com/","https://theprint.in/",
"https://www.wionews.com/","risingkashmir.com","https://www.aninews.in","telanganatoday.com","https://www.dailyo.in","http://www.ptinews.com/","forbesindia.com",
"Milligazette.com","dailyexcelsior.com","business-standard.com","https://www.wisden.com/","https://mumbaimirror.indiatimes.com/","https://www.thestatesman.com/",
"news.statetimes.in","Sentinelassam.com","http://www.telegraphindia.com/","Tribuneindia.com","oneindia.com","Assamtribune.com","https://www.deshabhimani.com/",
"https://www.newslaundry.com/","Bangaloremirror.indiatimes.com","https://www.opindia.com/","socialsamosa.com","Newstracklive.com","https://www.altnews.in",
"leagueofindia.com","prabhatkhabar.com","https://www.thesangaiexpress.com","http://kashmirreader.com","starofmysore.com","news4masses.com","headlinesoftoday.com",
"https://dainikexpressnews.blogspot.com","https://www.countercurrents.org/","Ahmedabadmirror.indiatimes.com","Punemirror.indiatimes.com","nagpurtoday.in",
"sinceindependence.com","https://www.dailypioneer.com/","http://www.timesheadline.com","http://www.asianage.com/","freepressjournal.in","https://5abnow.com",
"https://www.greatandhra.com/","http://www.ians.in/","https://www.factchecker.in/"]

# Count to keep track of number of websites covered
cnt = 0

for item in url_list:

	# Increment the website count
	cnt+=1

	# Generate resultant whois wrl for each news website in our list
	url = 'https://www.whois.com/whois/' + str(item)
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, features='html.parser')

	# Ttemp stores extracted Website Registrar, Registration Date, and Expiration Date from Whois using BeautifulSoup
	temp = []
	try:
		for a in soup.find('div', {'class' : 'df-block'}).find_all('div', {'class' : 'df-row'}):
			temp.append(a.find('div', {'class' : 'df-value'}).get_text().split('\n')[0])
			# print(a.find('div', {'class' : 'df-label'}).get_text().split())
		
		print(cnt, temp[0], cnt, temp[1:2], ",", temp[2], ",", temp[3])
	# Note: For all the URLs Skipped in this run, you may have to repeat or find manually
	except:
		print(temp[0])
	finally:
		continue