import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint

file = open('guns_collection.csv', 'w', encoding='utf-8_sig', newline='\n')
writer_obj = csv.writer(file)
writer_obj.writerow(['Model', 'Price', 'Photo'])

page_index = 1
while page_index <= 5:
    url = f'https://www.caliber.ge/open_category/41?page={page_index}/'
    response = requests.get(url)
    content = response.text

    # print(response.status_code)
    # print(response.headers)

    soup = BeautifulSoup(content, 'html.parser')

    guns_section = soup.find('div', class_='shop-product-wrap grid row aligned-row')
    guns = guns_section.find_all('div', class_='col-lg-3 col-md-4 col-sm-6')
    for each in guns:
        descr = each.find('div', class_='product-name')
        model = descr.h4.a.text.strip()
        price = each.find('span', class_='regular-price').text
        image = each.img.attrs.get('src')
        writer_obj.writerow([model, price, image])
    page_index += 1
    time.sleep(randint(15, 20))
