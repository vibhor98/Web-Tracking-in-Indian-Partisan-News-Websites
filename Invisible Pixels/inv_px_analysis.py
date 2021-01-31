# Total Invisible Images (1x1): 2,513

import pandas as pd
import urllib.request
from PIL import ImageFile

def getImgSize(uri):
    # get file size *and* image size (None if not known)
    try:
        file = urllib.request.urlopen(uri)
        # size = file.headers.get("content-length")
        # if size: size = int(size)
        p = ImageFile.Parser()
        while 1:
            data = file.read(1024)
            if not data:
                break
            p.feed(data)
            if p.image:
                return p.image.size
                break
        file.close()
    except:
        pass
    return None


df = pd.read_csv('./invisible_pixel_images.csv')
res = [['image_url', 'content_length', 'req_id', 'visit_id', 'news_site']]
res_no_image = [['image_url', 'content_length', 'req_id', 'visit_id', 'news_site']]
total_inv_imgs = 0

size = len(df)
for i in range(size):
    row = df.iloc[i]
    img_size = getImgSize(row['image_url'])
    if img_size and img_size[0]==1 and img_size[1]==1:
        total_inv_imgs += 1
        res.append([row['image_url'], row['content_length'], row['req_id'], row['visit_id'], row['news_site']])
    elif not img_size:
        res_no_image.append([row['image_url'], row['content_length'], row['req_id'], row['visit_id'], row['news_site']])
    if i%100 == 0:
        print(i, 'images processed!!!')

print('Total Invisible Images:', total_inv_imgs)
df_res = pd.DataFrame(res)
df_res.to_csv('./inv_pixel_imgs_1x1.csv', index=False)

df_no_img = pd.DataFrame(res_no_image)
df_no_img.to_csv('./inv_pixel_no_img.csv', index=False)
