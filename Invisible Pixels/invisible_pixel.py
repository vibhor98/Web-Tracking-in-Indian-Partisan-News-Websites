import sqlite3
import json
import pandas as pd
import numpy as np

homepages = list(pd.read_csv('news_homepage_urls.csv')['news_url'])

conn = sqlite3.connect('./topics_url_crawls/topics_url_crawl4/crawl-data_all_topics4.sqlite')
c = conn.cursor()

res = [['image_url', 'content_length', 'req_id', 'visit_id', 'news_site']]
image_count = 0
total_res = 0
total_imgs = 0
homepage_visit_ids = {}

for row in c.execute('SELECT visit_id, site_url FROM site_visits'):
    if row[1] in homepages:
        homepage_visit_ids[row[0]] = row[1]

for row in c.execute('SELECT hres.url, hres.headers, hres.request_id, hres.visit_id FROM http_responses AS hres'):
    if row[3] in homepage_visit_ids:
        total_res += 1
        header = json.loads(row[1])
        both_present = 0
        content_len = 0
        for tup in header:
            if tup[0].lower() == 'content-type':
                if tup[1].startswith('image'):
                    total_imgs += 1
                    both_present += 1
            elif tup[0].lower() == 'content-length':
                if int(tup[1]) <= 100000:
                    both_present += 1
                    content_len = int(tup[1])
            if both_present == 2:
                res.append([row[0], content_len, row[2], row[3], homepage_visit_ids[row[3]]])
                image_count += 1
                if image_count % 100 == 0:
                    print(image_count, 'images have been crawled.')
                break
df = pd.DataFrame(res)
df.to_csv('invisible_pixel_100kb.csv', index=False)

conn.close()
print('Total crawled images:', image_count)
print('Total images in homepages:', total_imgs)
print('Total responses in homepages:', total_res)
