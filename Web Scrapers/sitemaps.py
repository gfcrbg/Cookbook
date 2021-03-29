'''
This will allow you to extract links from the sitemap and/or gather general info, such as number of links.
Basically, this can be used to query the sitemap.
'''

import requests
from bs4 import BeautifulSoup

headers = {''}

# Request
# enter url
url = " "
r = requests.get(url, headers=headers)

# Parser
# determine parser, typically either lxml or html
sp = BeautifulSoup(r.text, 'lxml')

# find 'loc's
links = sp.find_all('loc')[0:]
 
# print number of links
print(len(links))

# print the links
for link in links:
    print(link.text)
