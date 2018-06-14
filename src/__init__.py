#! python3

import os
import math
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup


def download_from_url(url):
    image_name = os.path.basename(url)
    print('Downloading ' + image_name + '...')
    image_request = requests.get(url, stream=True)
    image_file = open(os.path.join('devhumor', image_name), 'wb')
    total_size = int(image_request.headers.get('content-length', 0))
    block_size = 1024
    for data in tqdm(image_request.iter_content(block_size),
                     total=math.ceil(total_size//block_size),
                     unit='KB', unit_scale=True):
        image_file.write(data)


print('Downloading Latest Devhumor Pictures...')
os.makedirs('devhumor', exist_ok=True)
res = requests.get('http://devhumor.com/')

soup = BeautifulSoup(res.text, 'html.parser')

image_tags = soup.select('img.single-media')

for image_tag in image_tags:
    image_url = image_tag.get('src')
    download_from_url(image_url)

print('Latest Pictures from Devhumor.com is now downloaded!')
