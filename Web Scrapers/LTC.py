# python ltc_locations.py

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import re
import json
from requests_html import HTMLSession

# Make a request
url = 'https://www.laredotacocompany.com/restaurant-locator-regions'
headers = {'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}

s = HTMLSession()

baseurl = 'https://www.laredotacocompany.com'

r1 = requests.get(url)

state_links = []
# r = requests.get(f'https://www.laredotacocompany.com{x}')

# This produces the link to each state.
soup1 = BeautifulSoup(r1.content, 'html.parser')
state = soup1.find_all('div','col-sm-4 mb-5')
for item in state:
    for link in item.find_all('a', href=True):
        state_links.append(baseurl + link['href'])

region_len = len(state_links)


# print(state_links)
# OUTPUT
# ['https://www.laredotacocompany.com/restaurant-locator-cities/TX', 'https://www.laredotacocompany.com/restaurant-locator-cities/NM', 'https://www.laredotacocompany.com/restaurant-locator-cities/LA', 'https://www.laredotacocompany.com/restaurant-locator-cities/OK', 'https://www.laredotacocompany.com/restaurant-locator-cities/CA', 'https://www.laredotacocompany.com/restaurant-locator-cities/DC', 'https://www.laredotacocompany.com/restaurant-locator-cities/FL', 'https://www.laredotacocompany.com/restaurant-locator-cities/VA', 'https://www.laredotacocompany.com/restaurant-locator-cities/PA', 'https://www.laredotacocompany.com/restaurant-locator-cities/TN', 'https://www.laredotacocompany.com/restaurant-locator-cities/CO']


# Pulls cities
# testlink1 = 'https://www.laredotacocompany.com/restaurant-locator-cities/NM'

city_links = []
 
for x in state_links:
    r1 = requests.get(x)
    soup1 = BeautifulSoup(r1.content, 'html.parser')
    city = soup1.find_all('li','mb-1')
    for item in city:
        for link in item.find_all('a', href=True):
            city_links.append(baseurl + link['href'])

city_links_table = pd.DataFrame(city_links)

# print(city_links_table.to_string())
# OUTPUT
# ['https://www.laredotacocompany.com/restaurant-locator-city/NM/ARTESIA', 'https://www.laredotacocompany.com/restaurant-locator-city/NM/CLOVIS', 'https://www.laredotacocompany.com/restaurant-locator-city/NM/HOBBS', 'https://www.laredotacocompany.com/restaurant-locator-city/NM/JAL', 'https://www.laredotacocompany.com/restaurant-locator-city/NM/LOVINGTON', 'https://www.laredotacocompany.com/restaurant-locator-city/NM/PORTALES', 'https://www.laredotacocompany.com/restaurant-locator-city/NM/ROSWELL', 'https://www.laredotacocompany.com/restaurant-locator-city/NM/TATUM', 'https://www.laredotacocompany.com/restaurant-locator-city/NM/TEXICO']


# Pulls location info
# testlink2 = 'https://www.laredotacocompany.com/restaurant-locator-city/TX/ABILENE'

location_links = []

for x in city_links:
    r2 = s.get(x)
    soup2 = BeautifulSoup(r2.content, 'html.parser')
    location = soup2.find_all('li','list-inline-item mb-2')
    for item in location:
        for link in item.find_all('a', href=True):
            location_links.append(baseurl + link['href'])



location_links_table = pd.DataFrame(location_links)

detail_links = []


# print(foo.string)

# print(location_links_table.to_string())
# OUTPUT
#                                                                                                       0
# 0        https://www.laredotacocompany.comhttp://maps.google.com/?q=6026 HWY. 277 SOUTH+ABILENE,TX+79606
# 1                                        https://www.laredotacocompany.com/restaurant-locator/detail/252
# 2  https://www.laredotacocompany.comhttp://maps.google.com/?q=1409 DUB WRIGHT BOULEVARD+ABILENE,TX+79606
# 3                                        https://www.laredotacocompany.com/restaurant-locator/detail/275
# 4              https://www.laredotacocompany.comhttp://maps.google.com/?q=4057 LOOP 322+ABILENE,TX+79606
# 5                                       https://www.laredotacocompany.com/restaurant-locator/detail/2250
# 6  https://www.laredotacocompany.comhttp://maps.google.com/?q=2717 INDUSTRIAL BOULEVARD+ABILENE,TX+79605
# 7                                       https://www.laredotacocompany.com/restaurant-locator/detail/2295

# pull links that contain "detail"
for x in location_links:
    if "detail" in x:
        detail_links.append(x)

detail_links_table = pd.DataFrame(detail_links)
# rint(detail_links_table.to_string())
# OUPUT
#                                                                  0
# 0   https://www.laredotacocompany.com/restaurant-locator/detail/252
# 1   https://www.laredotacocompany.com/restaurant-locator/detail/275
# 2  https://www.laredotacocompany.com/restaurant-locator/detail/2250
# 3  https://www.laredotacocompany.com/restaurant-locator/detail/2295

# print(location_links)


# pull store detals
testlink3 = 'https://www.laredotacocompany.com/restaurant-locator/detail/186'

detail_list = []

for x in detail_links:
    r3 = s.get(x)
    soup3 = BeautifulSoup(r3.content, 'html.parser')
    store_number = soup3.find('div','text-muted mb-1').text
    address1 = r3.html.xpath('//*[@id="maincontent"]/article/section/div/div/div[1]/address/text()[1]', first=True).strip()
    address2 = r3.html.xpath('//*[@id="maincontent"]/article/section/div/div/div[1]/address/text()[2]', first=True).strip()
    address = (address1 + "  " + address2)
    phone = soup3.find('div', 'text-orange mt-2 mb-4').text
    hours = soup3.find('em').text
    details = {
        'Store Number': store_number,
        'Address': address,
        'Phone Number': phone,
        'Hours': hours,
    }
    detail_list.append(details)

df = pd.DataFrame(detail_list)

# print(detail_list)

print(df.to_string())
# OUTPUT
#      Store Number                                       Address  Phone Number                 Hours
# 0   Restaurant 252        6026 HWY. 277 SOUTH  ABILENE, TX 79606  325-692-5126  Open 5am - 4pm daily
# 1   Restaurant 275  1409 DUB WRIGHT BOULEVARD  ABILENE, TX 79606  325-793-0423  Open 5am - 4pm daily
# 2  Restaurant 2250              4057 LOOP 322  ABILENE, TX 79606  325-793-0432  Open 5am - 4pm daily
# 3  Restaurant 2295  2717 INDUSTRIAL BOULEVARD  ABILENE, TX 79605  325-690-6551  Open 5am - 4pm daily


json_object = json.dumps(detail_list, indent=4)

def output():
    f = open('ltc.json', 'w')
    f.write(json_object)
    f.close()
    print("File saved.")

output()
