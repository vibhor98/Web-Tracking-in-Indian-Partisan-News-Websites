# Finds leaning-wise median and stdev of cookies for Desktop and Mobile websites
import pandas as pd
import statistics as stats

#df = pd.read_csv('./dsk_mob_crawl_wise_cookies.csv')
df = pd.read_csv('./inv_px_site_dom.csv')

left_dsk = []
right_dsk = []
centre_dsk = []

left_mob = []
right_mob = []
centre_mob = []

for i in range(len(df)):
    row = df.iloc[i]
    leaning = row['leaning']
    if leaning == 'left':
        left_dsk.append(row['#inv_imgs'])
        #left_dsk.append(row['dsk_cookies_crawl1'])
        # left_dsk.append(row['dsk_cookies_crawl2'])
        # left_dsk.append(row['dsk_cookies_crawl3'])
        # left_dsk.append(row['dsk_cookies_crawl4'])
        # left_dsk.append(row['dsk_cookies_crawl5'])
        # if not pd.isnull(row['mob_cookies_crawl1']):
        #     left_mob.append(row['mob_cookies_crawl1'])
        #     left_mob.append(row['mob_cookies_crawl2'])
        #     left_mob.append(row['mob_cookies_crawl3'])
        #     left_mob.append(row['mob_cookies_crawl4'])
        #     left_mob.append(row['mob_cookies_crawl5'])
    elif leaning == 'right':
        right_dsk.append(row['#inv_imgs'])
        # right_dsk.append(row['dsk_cookies_crawl1'])
        # right_dsk.append(row['dsk_cookies_crawl2'])
        # right_dsk.append(row['dsk_cookies_crawl3'])
        # right_dsk.append(row['dsk_cookies_crawl4'])
        # right_dsk.append(row['dsk_cookies_crawl5'])
        # if not pd.isnull(row['mob_cookies_crawl1']):
        #     right_mob.append(row['mob_cookies_crawl1'])
        #     right_mob.append(row['mob_cookies_crawl2'])
        #     right_mob.append(row['mob_cookies_crawl3'])
        #     right_mob.append(row['mob_cookies_crawl4'])
        #     right_mob.append(row['mob_cookies_crawl5'])
    elif leaning == 'centre':
        centre_dsk.append(row['#inv_imgs'])
        # centre_dsk.append(row['dsk_cookies_crawl1'])
        # centre_dsk.append(row['dsk_cookies_crawl2'])
        # centre_dsk.append(row['dsk_cookies_crawl3'])
        # centre_dsk.append(row['dsk_cookies_crawl4'])
        # centre_dsk.append(row['dsk_cookies_crawl5'])
        # if not pd.isnull(row['mob_cookies_crawl1']):
        #     centre_mob.append(row['mob_cookies_crawl1'])
        #     centre_mob.append(row['mob_cookies_crawl2'])
        #     centre_mob.append(row['mob_cookies_crawl3'])
        #     centre_mob.append(row['mob_cookies_crawl4'])
        #     centre_mob.append(row['mob_cookies_crawl5'])

print('Dsk left median:', stats.median(left_dsk))
print('Dsk right median:', stats.median(right_dsk))
print('Dsk centre median:', stats.median(centre_dsk))
# print('Dsk left stdev:', stats.stdev(left_dsk))
# print('Dsk right stdev:', stats.stdev(right_dsk))
# print('Dsk centre stdev:', stats.stdev(centre_dsk))


# print('Mob left median:', stats.median(left_mob))
# print('Mob right median:', stats.median(right_mob))
# print('Mob centre median:', stats.median(centre_mob))
# print('Mob left stdev:', stats.stdev(left_mob))
# print('Mob right stdev:', stats.stdev(right_mob))
# print('Mob centre stdev:', stats.stdev(centre_mob))
