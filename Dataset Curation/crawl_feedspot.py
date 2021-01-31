'''

This Code crawls the Top 141 Indian news websites and associated metadata from FEEDSPOT as available on the following date.
Date: 04 May 2020

'''

# Necessary Imports
from bs4 import BeautifulSoup 
from splinter import Browser
from time import sleep
import re, urllib.request, csv

# Feedspot URL
url = 'https://blog.feedspot.com/indian_news_websites/'

# Chrome Driver required (download from internet) so that dynamically loaded/extended page data can be extracted
# An executable driver has been added in Zipped Alexa websites folder in the "Websites Dataset" directory
# State the location of your driver
executable_path = {"executable_path": "C:/Desktop/chromedriver"}

# Instantiating a browser object as follows...
# Pass 'headless=False' to make Chrome launch a visible window
browser = Browser("chrome", **executable_path, headless=True)
browser.visit(url)
html = BeautifulSoup(browser.html, 'html.parser')
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Declare the JavaScript that scrolls to the end of the page...
scrollJS = "window.scrollTo(0, document.body.scrollHeight);"

# Declare number of attempts to make if extended page is not loaded in first attempt
attempt = 2
text = ""

while attempt > 0:

    # Scroll to the bottom of the page
    browser.execute_script(scrollJS)

    # Use BS4 to get the HTML
    soup = BeautifulSoup(browser.html, 'html.parser', from_encoding="utf-8")

    # Remove Styling/Scripting HTML Tags
    for script in soup(["script", "style"]):
    	script.extract()

    # Obtain raw text
    text = soup.get_text()

    # Sleep for some time so that extended page gets loaded by that time
    sleep(30)

    # Scroll down again, and run the loop
    browser.execute_script(scrollJS)

    # Reduce the attempt counter
    attempt -= 1


# Data Preprocessing
text = text.replace('⋅','').replace('ⓘ','').replace('  ',' ').replace('\n ','\n').replace(' » Top Stories','').replace('View Latest Posts⋅Get Email ContactSubscribe newsletter', '\n').replace('View Latest PostsGet Email ContactSubscribe newsletter', '').replace(': Daily News on India, World, Cricket, and More', '\n')
s_indx = text.find('Compact')
e_indx = text.find('Tags: indian')
text = text[s_indx:e_indx-2]
news_item = list(re.split('[0-9]+[.] ', text))[1:]
# print(len(news_item))


# Attribute Extraction from Crawled Data

# Declare Dictionary to store all information for each news website
news_websites = {}

# Count to maintain the key in news_websites corresponding to Feedspot index of website
cnt = 0

# For each news item in extracted data
for news in news_item:

	# Store the data of all the attributes for particular website
	attribute_list = {}

	# Using Regular Expression to extract data for different attributes for all the websites.
	# Regular expression patterns mentioned are based on observations for feedspot's extracted data.
	if news_item.index(news) > 59:
		if re.search('IndiaAbout', news):
			attribute_list['Website_Name'] = news[:news.find("IndiaAbout")]
		else:
			attribute_list['Website_Name'] = news[:news.find("About")]
	else:
		attribute_list['Website_Name'] = news[:news.find('\n')]
	
	if re.search("(IndiaAbout|\n.*India About)", news):
		if news_item.index(news) > 59:
			attribute_list['Location'] = 'India'
		else:
			attribute_list['Location'] = re.search("\n.*India About", news).group(0)[1:-6]
	else:
		attribute_list['Location'] = 'N/A'
	
	if re.search('About Website', news):
		attribute_list['About_Website'] = news[news.find('About Website')+14:news.find(' Frequency')]
	else:
		attribute_list['About_Website'] = 'N/A'

	if re.search("Frequency [0-9]+ post[s]? / (day|week|year|quarter)", news):
		attribute_list['Frequency'] = re.search("Frequency [0-9]+ post[s]? / (day|week|year|quarter)", news).group(0)[10:]
	else:
		attribute_list['Frequency'] = 'N/A'
	
	if re.search("day Website|week Website|year Website|quarter Website", news):
		if news_item.index(news) > 59:
			attribute_list['Website'] = re.search("Website http[s]?[\S]+[.](com|net|news|info|in|me|website)", news).group(0)[8:]
		else:
			attribute_list['Website'] = re.search("[d|w|y|q][a|e|u][y|e|a][k|r]?[t]?[e]?[r]? Website [\S]+[.][c|i][o|n][m]?", news).group(0)[13:].split()[-1]
	else:
		attribute_list['Website'] = 'N/A'

	if 'Facebook fans' in news:
		attribute_list['Facebook_Reach'] = re.search("Facebook fans [0-9]+[.]?[0-9]*[M|K]?", news).group(0)[14:]
	else: 
		attribute_list['Facebook_Reach'] = 'N/A'

	if 'Twitter Followers' in news or 'Twitter followers' in news:
		attribute_list['Twitter_Reach'] = re.search("Twitter [F|f]ollowers [0-9]+[.]?[0-9]*[M|K]?", news).group(0)[18:]
	else:
		attribute_list['Twitter_Reach'] = 'N/A'

	if 'Instagram Followers' in news or 'Instagram followers' in news:
		attribute_list['Instagram_Reach'] = re.search("Instagram [F|f]ollowers [0-9]+[.]?[0-9]*[M|K]?", news).group(0)[20:]
	else:
		attribute_list['Instagram_Reach'] = 'N/A'

	if 'Social Engagement' in news:
		attribute_list['Social_Engagement'] = re.search("Social Engagement [0-9]+[.]?[0-9]*[M|K]?", news).group(0)[18:]
	else:
		attribute_list['Social_Engagement'] = 'N/A'

	if 'Domain Authority' in news:
		attribute_list['Domain_Authority'] = re.search("Domain Authority [0-9]+[.]?[0-9]*[M|K]?", news).group(0)[17:]
	else:
		attribute_list['Domain_Authority'] = 'N/A'

	if 'Alexa Rank' in news:
		attribute_list['Alexa_Rank'] = re.search("Alexa Rank [0-9]+[.]?[0-9]*[M|K]?[ |\n]*", news).group(0)[11:]
	else:
		attribute_list['Alexa_Rank'] = 'N/A'

	# Increment count for next website in Feedspot list
	cnt += 1

	news_websites[cnt] = attribute_list

# Print Metadat for all the websites to observe the output and improve inconsistencies in above RE-based extraction
for key in news_websites.keys():
	print(key)
	print('Website_Name     : ', news_websites[key]['Website_Name'])
	print('Location         : ', news_websites[key]['Location'])
	print('About_Website    : ', news_websites[key]['About_Website'])
	print('Frequency        : ', news_websites[key]['Frequency'])
	print('Website          : ', news_websites[key]['Website'])
	print('Facebook_Reach   : ', news_websites[key]['Facebook_Reach'])
	print('Twitter_Reach    : ', news_websites[key]['Twitter_Reach'])
	print('Instagram_Reach  : ', news_websites[key]['Instagram_Reach'])
	print('Social_Engagement: ', news_websites[key]['Social_Engagement'])
	print('Domain_Authority : ', news_websites[key]['Domain_Authority'])
	print('Alexa_Rank       : ', news_websites[key]['Alexa_Rank'])
	print()


# Enter a list of fields or column names or headers required in the csv output
fields = ['FeedSpot_Rank', 'Website_Name', 'Location', 'About_Website', 'Frequency', 'Website', 'Facebook_Reach', 'Twitter_Reach', 'Instagram_Reach', 'Social_Engagement', 'Domain_Authority', 'Alexa_Rank']

# Opening a CSV file in write format
with open("Feedspot Dataset.csv", "w") as f:
	# Write header and data to csv file
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for k in news_websites.keys():
        w.writerow({field: news_websites[k].get(field) or k for field in fields})