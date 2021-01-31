# Count no. of domains in which fingerprinting scripts are present.

import sqlite3
import operator
import requests
import numpy as np
import pandas as pd
import seaborn as sns

fp_scripts = [
    'https://www.sentinelassam.com/scripts/hocalwirecommonlightpart1.min.bf6b3d58.js',
    'https://analytics-v2.whizzbi.com/wa.js?pid=WA-IV81HgGC-1',
    'https://s4.scoopwhoop.com/v4/newdesignassets/static/sw/newDesign/desktop/js/app.bundle.0.1.22.js',
    'https://thelogicalindian.com/scripts/hocalwirecommonlightpart1.min.bf6b3d58.js',
    'https://imasdk.googleapis.com/js/core/bridge3.405.0_en.html#goog_947617639',
    'https://imasdk.googleapis.com/js/core/bridge3.405.0_en.html#goog_2056936552',
    'https://s0.2mdn.net/879366/Enabler_01_242.js',
    'https://s0.2mdn.net/ads/studio/Enabler.js',
    'https://cdn.fqtag.com/1.27.339-ccfb11a/pixel.js',
    'https://jsc.mgid.com/h/i/hindi.webdunia.com.934514.js',
    'https://thelogicalindian.com/scripts/hocalwirecommonlightpart2.min.c265d60b.js',
    'https://ua.financialexpress.com/personlization-sdk.min.js',
    'https://jsc.mgid.com/b/h/bhaskar.com.790730.js',
    'https://jsc.mgid.com/a/n/aninews.in.713570.js?t=202072810',
    'https://imasdk.googleapis.com/js/core/bridge3.405.0_en.html#goog_1806513628',
    'https://cdnjs.cloudflare.com/ajax/libs/ClientJS/0.1.11/client.min.js',
    'https://ua.indianexpress.com/personlization-sdk.min.js',
    'https://checkout.razorpay.com/v1/checkout-frame.js',
    'https://imasdk.googleapis.com/js/core/bridge3.405.0_en.html#goog_1072780719',
    'https://www.sentinelassam.com/scripts/hocalwirecommonlightpart2.min.1d136422.js',
    'https://www.anandabazar.com/microsites/user-action/tracking.min.js',
    'https://jsc.mgid.com/t/i/timesnownews.com.769610.js?t=20207299',
    'https://imasdk.googleapis.com/js/core/bridge3.405.0_en.html#goog_770736604',
    'https://jsc.mgid.com/t/i/timesnownews.com.769604.js?t=20207299',
    'https://jsc.mgid.com/a/n/aninews.in.923105.js'
]

homepages = list(pd.read_csv('news_homepage_urls.csv')['news_url'])

conn = sqlite3.connect('./topics_url_crawls/topics_url_crawl4/crawl-data_all_topics4.sqlite')
c = conn.cursor()


total_scripts = 0
sites_with_fingerprint = []   # Unique Homepages in which Canvas FP is present.
homepage_visit_ids = []
fp_script_homepage_dict = {}
for scr in fp_scripts:
    fp_script_homepage_dict[scr] = []


for row in c.execute('SELECT visit_id, site_url FROM site_visits'):
    if row[1] in homepages:
        homepage_visit_ids.append(row[0])
#print(homepage_visit_ids)

for row in c.execute('SELECT visit_id, script_url, top_level_url, symbol FROM javascript'):
    if row[0] in homepage_visit_ids:
        if row[3].startswith('HTMLCanvasElement') or row[3].startswith('CanvasRenderingContext2D'):
            if row[1] in fp_script_homepage_dict:
                total_scripts += 1
                fp_script_homepage_dict[row[1]].append(row[2])
                sites_with_fingerprint.append(row[2])
conn.close()

print('Total FP scripts:', total_scripts)
print('Unique FP scripts: 25')
print('Total sites in which fingerprinting is present:', len(set(sites_with_fingerprint)))

fp_domain_homepage_dict = {}

#print('\nFP scripts with websites count in which they are present:')
for scr in fp_script_homepage_dict:
    #fp_script_homepage_dict[scr] = set(fp_script_homepage_dict[scr])
    #print(scr, len(fp_script_homepage_dict[scr]))
    domain = scr.split('/')[2]
    if domain in fp_domain_homepage_dict:
        fp_domain_homepage_dict[domain].extend(fp_script_homepage_dict[scr])
    else:
        fp_domain_homepage_dict[domain] = fp_script_homepage_dict[scr]

#print('\nFP scripts with websites in which they are present:')
#print(fp_script_homepage_dict)

print('\nFP domains with websites in which they are present:')
for dom in fp_domain_homepage_dict:
    fp_domain_homepage_dict[dom] = set(fp_domain_homepage_dict[dom])
    print(dom, len(fp_domain_homepage_dict[dom]), fp_domain_homepage_dict[dom])
