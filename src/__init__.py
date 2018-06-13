#! python3

import os
import requests
from bs4 import BeautifulSoup


def download_from_url(url):
    image_request = requests.get(url)
    image_name = os.path.basename(image_url)
    print('Downloading ' + image_name + '...')

    image_file = open(os.path.join('devhumor', image_name), 'wb')
    for chunk in image_request.iter_content(100000):
        image_file.write(chunk)


print('Downloading Latest Devhumor Pictures...')
os.makedirs('devhumor', exist_ok=True)
res = requests.get('http://devhumor.com/')

soup = BeautifulSoup(res.text, 'html.parser')

image_tags = soup.select('img.single-media')

for image_tag in image_tags:
    image_url = image_tag.get('src')
    download_from_url(image_url)

print('Latest Pictures from Devhumor.com is now downloaded!')
