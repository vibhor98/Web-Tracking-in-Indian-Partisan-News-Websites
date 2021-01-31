'''

This Code uses the Disconnect List to obtain the category of the third-party cookie domain and to obtain a leaning-wise distribution of these categories in our data.
Date: 09 September 2020

'''

# Necessary Imports
import sys
# Path to folder Containing Cookie Synchronization codes
sys.path.append('../Cookie Synchronization/')
import find_site_leaning
import census_util

import sqlite3 as lite
import pandas as pd
import json
import os


# This function can be used to search for the tracking domains from your data in disconnect_list and also obtain their categories
# We have already found these and added the list of tracking domains in our data (list :: tp_cookie_domain_list) 
# and their categories (list :: cats) and added them below the function

'''

def search_disconnect_list():
	data_folder_path = os.path.join(os.path.join(os.path.abspath(os.pardir)), 'Cookie Analysis - DisconnectList Data')
	file_path1 = os.path.join(data_folder_path, 'trackers.json')
	file_path2 = os.path.join(data_folder_path, 'disconnect_list.json')

	with open(file_path1) as f1:
	  trackers = json.load(f1)

	all_domains = trackers.get("domains", [])
	first_parties = trackers.get("fp_domains", [])
	cookies = list(set(trackers.get("tp_cookies", [])) - set(first_parties))

	with open(file_path2, encoding="utf8") as f2:
	  disconnect_list = json.load(f2)

	disconnect_list_trackers = {}
	for cat in disconnect_list.get("categories", {}).keys():
		category = cat
		for company_dict in disconnect_list["categories"][cat]:
			company = list(company_dict.keys())[0]
			company_url = list(company_dict[company].keys())[0]
			for domain in company_dict[company][company_url]:
				disconnect_list_trackers[domain] = {}
				disconnect_list_trackers[domain]["owning_company"] = company
				disconnect_list_trackers[domain]["tracker_category"] = category

	tp_cookie_domain_list = tracker.keys()
	for tracker in domains:
		if tracker in disconnect_list_trackers.keys():
			cats.append(disconnect_list_trackers[domain]["tracker_category"])
		else:
			cats.append("Other")

'''


# We place here the tp_cookie_settting_domains which are present in disconnect_list as obtained from above function
tp_cookie_domain_list = ["mobileadtrading.com", "adjust.com", "smaato.com", "everesttech.net", "quantserve.com", "adnxs.com", "ml314.com", "microad.jp", "atdmt.com", 
"betweendigital.com", "emerse.com", "amazon-adsystem.com", "admedia.com", "turn.com", "adsrvr.org", "rlcdn.com", "springserve.com", "demdex.net", "mfadsrvr.com", 
"yahoo.com", "ipredictive.com", "rtk.io", "bluekai.com", "disqus.com", "tapad.com", "eqads.com", "pro-market.net", "kargo.com", "googlesyndication.com", "adform.net", 
"zemanta.com", "id5-sync.com", "affinity.com", "pubmatic.com", "adsymptotic.com", "clmbtech.com", "scorecardresearch.com", "dotomi.com", "bttrack.com", "liadm.com", 
"gumgum.com", "gleam.io", "serving-sys.com", "sitescout.com", "adkernel.com", "eyeota.net", "tidaltv.com", "stackadapt.com", "addthis.com", "mookie1.com", 
"smartadserver.com", "dyntrk.com", "outbrain.com", "taboola.com", "33across.com", "sharethrough.com", "fwmrm.net", "imrworldwide.com", "owneriq.net", "openx.net", 
"ad-stir.com", "connexity.net", "adhigh.net", "pippio.com", "statcounter.com", "krxd.net", "spotxchange.com", "rubiconproject.com", "lkqd.net", "extend.tv", 
"onaudience.com", "simpli.fi", "media.net", "reemo-ad.jp", "emxdgt.com", "adition.com", "youtube.com", "technoratimedia.com", "gssprt.jp", "w55c.net", "casalemedia.com", 
"impact-ad.jp", "doubleclick.net", "yieldmo.com", "brealtime.com", "crwdcntrl.net", "mxptint.net", "stickyadstv.com", "admatrix.jp", "appier.net", "linkedin.com", 
"exelator.com", "lijit.com", "bidswitch.net", "adotmob.com", "adgrx.com", "mathtag.com", "contextweb.com", "deepintent.com", "zedo.com", "skimresources.com", "agkn.com", 
"acuityplatform.com", "tribalfusion.com", "rfihub.com", "insightexpressai.com", "microsoft.com", "twitter.com", "effectivemeasure.net", "sonobi.com", "tremorhub.com", 
"3lift.com", "google.com", "advertising.com", "creativecdn.com", "sekindo.com", "bidr.io", "tynt.com", "iasds01.com", "digitru.st", "sharethis.com", "facebook.com", 
"twimg.com", "admedo.com", "fameitc.com", "adgebra.co.in", "lentainform.com", "adxpremium.services", "ccgateway.net", "adtelligent.com", "omnithrottle.com", 
"fireworktv.com", "imonomy.com", "volvelle.tech", "fw-ad.jp", "audiencemanager.de", "e-volution.ai", "dmxleo.com", "izooto.com", "mrpdata.net", "jiosaavn.com", 
"weatherwidget.io", "myvisualiq.net", "mmonline.io", "dailymotion.com", "uncn.jp", "cognitivlabs.com", "brand-display.com", "gsspat.jp", "s3xified.com", "topyaps.com", 
"blismedia.com", "mykhel.com", "cauly.co.kr", "tvid.in", "smrtb.com", "ladsp.com", "r-ad.ne.jp", "vrtzads.com", "cmcd1.com", "ctnsnet.com", "xspadvertising.com", 
"dnacdn.net", "a-mo.net", "aso1.net", "ad-m.asia", "anandabazar.com", "consensu.org", "lemmatechnologies.com", "cuberoot.co", "akamaihd.net", "truepush.com", 
"responsibletourismindia.com", "walmart.com", "vdo.ai", "app.link", "sportradarserving.com", "readwhere.com", "playground.xyz", "gmdelivery.com", "zeotap.com", 
"bfmio.com", "advangelists.com", "ad.style", "outlookhindi.com", "smadex.com", "metype.com", "digitaleast.mobi", "avct.cloud", "nrich.ai", "servenobid.com", 
"adspruce.com", "bidtheatre.com", "idealmedia.io", "geistm.com", "innovid.com", "thrtle.com", "colossusssp.com", "sharedid.org", "erne.co", "sphereup.com", "dc-1.net", 
"vidgyor.com", "chocolateplatform.com", "socdm.com", "feedify.net", "qlitics.com", "wzrkt.com", "kesari.tv", "elfsight.com", "audienceplay.com", "adpushup.com", 
"resetdigital.co", "mgid.com", "onetag-sys.com"]


# The Disconnect list (DL) is used to categorize above domains by a direct lookup in online available DL as done in above function
cats = ["Advertising","Fingerprinting","Advertising","Fingerprinting","Advertising","Advertising","Analytics","Advertising","Other","Advertising","Advertising",
"Advertising","Advertising","Advertising","Fingerprinting","Advertising","Advertising","Fingerprinting","Advertising","Content & Social","Advertising",
"Advertising","Fingerprinting","Content & Social","Fingerprinting","Advertising","Advertising","Advertising","Other","Advertising","Advertising",
"Advertising","Advertising","Advertising","Fingerprinting","Advertising","Analytics","Fingerprinting","Advertising","Advertising","Advertising","Advertising",
"Advertising","Advertising","Advertising","Analytics","Content & Social","Advertising","Content & Social","Advertising","Advertising","Advertising",
"Advertising","Advertising","Advertising","Advertising","Content & Social","Advertising","Advertising","Fingerprinting","Advertising","Analytics",
"Advertising","Analytics","Analytics","Fingerprinting","Advertising","Advertising","Advertising","Advertising","Analytics","Advertising","Advertising",
"Advertising","Advertising","Advertising","Content & Social","Advertising","Advertising","Advertising","Advertising","Advertising","Other","Fingerprinting",
"Advertising","Fingerprinting","Advertising","Advertising","Advertising","Advertising","Content & Social","Advertising","Advertising","Advertising",
"Advertising","Advertising","Fingerprinting","Advertising","Analytics","Advertising","Advertising","Advertising","Advertising","Advertising","Advertising",
"Advertising","Content & Social","Other","Advertising","Advertising","Advertising","Advertising","Content & Social","Advertising","Advertising","Advertising",
"Advertising","Content & Social","Advertising","Advertising","Content & Social","Other","Other","Advertising","Other","Other","Other","Other","Other","Other",
"Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other",
"Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other",
"Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other",
"Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other","Other",
"Other","Other","Other","Other","Other","Other","Other","Other","Other"]

# Initializing the variables
tp_domain_to_visitid = {}
ids = {}
cat_ids = {"Advertising": {"LEFT": [], "RIGHT": [], "CENTRE": []}, "Content & Social": {"LEFT": [], "RIGHT": [], "CENTRE": []}, 
		   "Analytics": {"LEFT": [], "RIGHT": [], "CENTRE": []}, "Fingerprinting": {"LEFT": [], "RIGHT": [], "CENTRE": []}, 
		   "Other": {"LEFT": [], "RIGHT": [], "CENTRE": []}}
domain_to_cookie_count = {}

DATA_DIR = os.path.join(os.path.abspath(os.pardir),'OpenWPM Crawls')
cookie_db = os.path.join(DATA_DIR, '<crawl-data-filename>.sqlite')
conn = lite.connect(cookie_db)
cur = conn.cursor()
tp_cookies = []

print("Extracting Sites (visit_id's) in which a TP Cookie Domain is set from OpenWPM Data!")
for d in tp_cookie_domain_list:
	if d not in tp_domain_to_visitid.keys():
		tp_domain_to_visitid[d] = []

	for domain, visit in cur.execute('SELECT DISTINCT host, visit_id FROM javascript_cookies'):
	    domain = census_util.extract_domain(domain)

	    if d in domain:
	    	if visit not in tp_domain_to_visitid[d]:
	    		tp_domain_to_visitid[d].append(visit)

# The above computed visit_id's are used to find leaning of the websites
cnt = 0
for d in tp_cookie_domain_list:
	left = 0
	right = 0
	centre = 0
	for visit_id in tp_domain_to_visitid[d]:
		for res in cur.execute('SELECT arguments FROM crawl_history'+' WHERE visit_id = '+str(visit_id)):
		    site_url = str(res[0]).split(',')[0][9:-1]
		    site_leaning = find_site_leaning.get_leaning(site_url)
		    break
		indx = tp_cookie_domain_list.index(d)
		if site_leaning == "LEFT":
			left += 1
			if visit_id not in cat_ids[cats[indx]][site_leaning]:
				cat_ids[cats[indx]][site_leaning].append(visit_id)
		elif site_leaning == "RIGHT":
			if visit_id not in cat_ids[cats[indx]][site_leaning]:
				cat_ids[cats[indx]][site_leaning].append(visit_id)
			right += 1
		elif site_leaning == "CENTRE":
			if visit_id not in cat_ids[cats[indx]][site_leaning]:
				cat_ids[cats[indx]][site_leaning].append(visit_id)
			centre += 1
	
	cnt += 1
	# print(cnt, ",", d, ",", left, ",", right, ",", centre)


# Finding leaning-wise counts of number of tp_domains present in each category
site_counts = {"Left": {"Advertising": [], "Content & Social": [], "Analytics": [], "Fingerprinting": [], "Other": []},  
			   "Centre": {"Advertising": [], "Content & Social": [], "Analytics": [], "Fingerprinting": [], "Other": []},
			   "Right": {"Advertising": [], "Content & Social": [], "Analytics": [], "Fingerprinting": [], "Other": []}}
# print(list(set(tp_cookies)))

id_to_dom = {}
for k, listt in tp_domain_to_visitid.items():
    for vid in listt:
        if vid not in id_to_dom.keys():
            id_to_dom[vid] = []
        id_to_dom[vid].append(k)

# print(sorted(id_to_dom.keys()))
tmp = {"LEFT": "Left", "RIGHT": "Right", "CENTRE": "Centre", "NA": "NA"}

# Computing Leaning-wise counts of each category
for idd in id_to_dom.keys():
	for res in cur.execute('SELECT arguments FROM crawl_history'+' WHERE visit_id = '+str(idd)):
	    site_url = str(res[0]).split(',')[0][9:-1]
	    site_leaning = tmp[find_site_leaning.get_leaning(site_url)]
	    break
	if site_leaning == "NA":
		continue
	cnt_ad = 0
	cnt_cs = 0
	cnt_anly = 0
	cnt_fp = 0
	cnt_unk = 0
	for d in id_to_dom[idd]:
		indx = tp_cookie_domain_list.index(d)
		cat = cats[indx]
		if cat == "Advertising":
			cnt_ad += 1
			continue
		elif cat == "Content & Social":
			cnt_cs += 1
			continue
		elif cat == "Analytics":
			cnt_anly += 1
			continue
		elif cat == "Fingerprinting":
			cnt_fp += 1
			continue
		elif cat == "Other":
			cnt_unk += 1
			continue

	site_counts[site_leaning]["Advertising"].append(cnt_ad)
	site_counts[site_leaning]["Content & Social"].append(cnt_cs)
	site_counts[site_leaning]["Analytics"].append(cnt_anly)
	site_counts[site_leaning]["Fingerprinting"].append(cnt_fp)
	site_counts[site_leaning]["Other"].append(cnt_unk)

# Saving the dataframe of counts for plotting
df = pd.DataFrame(columns=["Cookie Category", "Leaning", "Values"])
for k1 in site_counts.keys():
	for k2 in site_counts[k1].keys():
		for item in site_counts[k1][k2]:
			df = df.append({
			     "Cookie Category": k2,
			     "Leaning": k1 + " Websites",
			     "Values": item
			      }, ignore_index=True)