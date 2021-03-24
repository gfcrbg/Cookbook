'''
QFC Scraper
'''
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50'}

main_list = []

def requestBase():
    x = 1
    base_url = f'https://www.qfc.com/pdp-sitemap/qfc-product-details-sitemap-{x}.xml'
    base_r = requests.get(base_url, headers=headers)
    base_soup = BeautifulSoup(base_r.content, 'lxml')
    return base_soup


def parse(articles):
    for item in articles:
        try:
            name = item.find('h1', class_='ProductDetails-header').text.replace('®', ' ').replace('™','')
        except: 
            name = 'none'
        try:
            upc = item.find('span', class_='kds-Text--m ProductDetails-upc text-default-700').text
        except:
            upc = 'none'
        try:
            price = item.find('data').attrs.get('value', ' ')
        except:
            price = 'none'

        prod_link = product_link

        product = {
            'Name': name,
            'UPC': upc,
            'Price': price,
            'Product Link': prod_link,
        }

        main_list.append(product)
    return


links = requestBase().find_all('loc')[11:12]
for link in links:
    count = links.index(link) + 1
    product_link = link.text
    time.sleep(0)
    print(count, link.next)
    r = requests.get(product_link, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    articles = soup.find_all('div', class_= 'ProductDetails')
    parse(articles)


def output():
    df = pd.DataFrame(main_list)
    df.to_csv('qfc-test2.csv', index=False)


output()
print('Saved to file')
