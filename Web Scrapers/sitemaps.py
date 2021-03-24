# python sitemaps.py

import requests
from bs4 import BeautifulSoup

headers = {''}

# enter url
url = " "
r = requests.get(url, headers=headers)

# determine parser
sp = BeautifulSoup(r.text, 'lxml')

# find 'loc's
links = sp.find_all('loc')[0:]
 

# print number of links
# print(len(links))


# print the links
for link in links:
    print(link.text)
