'''

This Code crawls the Top News Sites from Alexa
Date: 29 April 2020

'''

from bs4 import BeautifulSoup


'''

Sample html for TOI, so you can dive in -

<div class="td">3</div>
  <div class="td DescriptionCell">
    <p class="">
        <a href="https://www.alexa.com/siteinfo/timesofindia.indiatimes.com">Timesofindia.indiatimes.com</a>                
    </p>
  </div>

'''

# Unzip the "Alexa - Top 49 News Sites.zip" present in Websites Dataset folder and use the obtained html file's path here
soup = BeautifulSoup(open("Alexa - HTML based Crawl/Alexa - Top Sites by Category_ Top_News_Newspapers_Regional_India.html"), 'html.parser')

for script in soup(["script", "style"]):
	script.extract()

site_list = []
for website in soup.find_all('div', {'class' : 'td DescriptionCell'}):
	site_name = website.get_text()
	site_list.append(site_name.split()[0])

print(len(site_list))
print(site_list)

'''

Output:
49
['Indiatimes.com', 'Economictimes.indiatimes.com', 'Timesofindia.indiatimes.com', 'Livemint.com', 'Hindustantimes.com', 'Thehindu.com', 'Indianexpress.com', 
'Business-standard.com', 'Mathrubhumi.com', 'Financialexpress.com', 'Deccanherald.com', 'Thehindubusinessline.com', 'Newindianexpress.com', 'Tribuneindia.com', 
'Siasat.com', 'Deccanchronicle.com', 'Bangaloremirror.indiatimes.com', 'Mumbaimirror.indiatimes.com', 'Telegraphindia.com', 'Dnaindia.com', 'Freepressjournal.in', 
'Mid-day.com', 'Punemirror.indiatimes.com', 'Newstracklive.com', 'Thestatesman.com', 'Sentinelassam.com', 'Dailypioneer.com', 'Asianage.com', 
'Ahmedabadmirror.indiatimes.com', 'Assamtribune.com', 'Greaterkashmir.com', 'Dailyexcelsior.com', 'Starofmysore.com', 'Newstodaynet.com', 'Morungexpress.com', 
'Andhrabhoomi.net', 'Navhindtimes.in', 'Chakranews.com', 'Milligazette.com', 'Mydigitalfc.com', 'Kashmirtimes.com', 'Thenorthlines.com', 'Thesangaiexpress.com', 
'Centralchronicle.com', 'Eprahaar.in', 'Kashmirherald.com', 'Newspapersinfo.com', 'Onlinenewsind.com', 'Timesofbhatkal.com']

'''