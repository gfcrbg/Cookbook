'''
Walmart Scraper
'''

# python scraper_walmart.py

import requests
import json
import pandas as pd
import time

# paste the Python-Requests code snippet from Postman; just the payload and headers; paste the url into the 'url' variable in the loop below
payload={}
headers = {
  'authority': 'www.walmart.com',
  'accept': 'application/json',
  'wm_client_ip': '',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
  'content-type': 'application/json',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.walmart.com/browse/movies-tv-shows/movies/4096_530598?page=1&redirectQuery=movies&redirect_query=movies&search_redirect=true',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'brwsr=ce7d7ed4-f08c-11ea-a4eb-42010a246cc1; DL=78758%2C%2C%2Cip%2C78758%2C%2C; vtc=ctJc8k1n2l-H0bhKTlEb6g; adblocked=false; TBV=7; cart-item-count=0; _pxvid=67ad5d85-6ba9-11eb-93b3-0242ac120008; __gads=ID=7cc75f9ae737f078:T=1612966090:S=ALNI_MYmQKZM2xuRnt1KEXWJ00bYaVApbw; _gcl_au=1.1.279445837.1612966090; _fbp=fb.1.1612966090699.2111990755; TS01af768b=01538efd7cdbc7d74a7e437ebb57bf72f0c67cfe93944f2bcf58d79609af3b611fb356bf68d95e0c53895cbf062e55a8f791ef48e5; TS012c809b=01538efd7cdbc7d74a7e437ebb57bf72f0c67cfe93944f2bcf58d79609af3b611fb356bf68d95e0c53895cbf062e55a8f791ef48e5; GCRT=81ab3e6f-42cd-454f-bd6b-105552832517; hasGCRT=1; ACID=8a9556a0-6ba9-11eb-9339-cf25ba7bff1c; hasACID=1; s_vi=[CS]v1|3011F482BD81C98D-600005FB216A7168[CE]; s_sess_2=%20cmp%3Df0V2wkIyM0%3B%20ent%3DHomePage%257COVERLAY_VIEW%3B%20s_cc%3Dtrue%3B%20chan%3Daff%3B%20v59%3D%3B%20v54%3DHomePage%257COVERLAY_VIEW%2520%3B%20cps%3D0%3B%20s_sq%3D%3B; tb_sw_supported=true; TS01bae75b=01538efd7c8bfb9e9c22bd73e59e17df58c4b4564f8b9201b120562b909734f0350fb499d8c437a40631aac3cd11c029924e1b557e; wm_mystore=Fe26.2**cef665c64ab045aac3717e7689c0b528b5652d71bc30c43f96d0e0252435bd2c*JsgkYqzOKqWK1Bhs-_B-zg*QmrJBhfYMrC63482DE938ljJ5mMq0QT8Y1N9g4iEjM5TKidl5fnRVK63N7362eA9SWBjBDWQQE0zOuQR2rLHBdj15RCiHJFQRLafVC73EZyEL5yrK6_jbZlLyqgJlMq742wUnC2E82u9mnEvAQ6UKw**ff65507b197f1ad312466d496dc6b5c6a38b51484958c6172d2f197fc2b54506*7ojUQsj8bmJslGbM6JtL_5YGBn1ytoDADzm_Gzj8rHY; x-csrf-jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiY29va2llIiwidXVpZCI6ImIyNzJhOTUwLTdiNmUtMTFlYi1iZTE4LTliMTNlM2E5NjI0MCIsImlhdCI6MTYxNDcwMDA5MywiZXhwIjoxNjE1NzgwMDkzfQ.0NTfa6JYTIpxreOZ-f5SEl7BsRfSoARlzrDSD-blZEc; s_pers=%20s_cmpstack%3D%255B%255B%2527aff%2527%252C%25271614113898494%2527%255D%252C%255B%2527seo_un%2527%252C%25271614175744221%2527%255D%255D%7C1771942144221%3B%20s_fid%3D2FA8EAD0D78D3961-1577B807665B5AAD%7C1677772093418%3B%20s_v%3DY%7C1614701893422%3B%20gpv_p11%3DHousehold%2520Essentials%253ACleaning%2520Tools%253AProduct%2520Range%7C1614701893443%3B%20gpv_p44%3DHousehold%2520Essentials%7C1614701893448%3B%20s_vs%3D1%7C1614701893454%3B; s_sess=%20s_cc%3Dtrue%3B%20ent%3DleaningTools%253AProductRange%3B%20cp%3DY%3B%20chan%3Dorg%3B%20v59%3DHousehold%2520Essentials%3B%20v54%3DHousehold%2520Essentials%253ACleaning%2520Tools%253AProduct%2520Range%3B%20cps%3D1%3B%20s_sq%3D%3B; akavpau_p14=1614700702~id=d2d61ba5d289e783329ef291eedd8bd0; s_pers_2=om_mv3d%3Daff%3Aadid-%3Asourceid-imp_Q59y7gS2QxyOWjLwUx0Mo3bxUkEQiyV92wkIyM0%3Awmls-imp_2003851%3Acn-%7C1615052144682%3B%20%2Bom_mv7d%3Dsem%3Aadid-22222222224226138098%3Asourceid-%3Awmls-wmtlabs%3Acn-%7C1613574489762%3B%20%2Bom_mv14d%3Dsem%3Aadid-22222222224226138098%3Asourceid-%3Awmls-wmtlabs%3Acn-%7C1614179289764%3B%20%2Bom_mv30d%3Dsem%3Aadid-22222222224226138098%3Asourceid-%3Awmls-wmtlabs%3Acn-%7C1615561689764%3B%20useVTC%3DY%7C1676081289%3B%20om_mv7d%3Daff%3Aadid-%3Asourceid-imp_Q59y7gS2QxyOWjLwUx0Mo3bxUkEQiyV92wkIyM0%3Awmls-imp_2003851%3Acn-%7C1615397744684%3B%20om_mv14d%3Daff%3Aadid-%3Asourceid-imp_Q59y7gS2QxyOWjLwUx0Mo3bxUkEQiyV92wkIyM0%3Awmls-imp_2003851%3Acn-%7C1615998944685%3B%20om_mv30d%3Daff%3Aadid-%3Asourceid-imp_Q59y7gS2QxyOWjLwUx0Mo3bxUkEQiyV92wkIyM0%3Awmls-imp_2003851%3Acn-%7C1617381344686; TS013ed49a=01538efd7c510cd3ed089d0050fe5606df279c9a24f5b201eae7efd54a9c80d9cfeaaee1bdb46c5d2a2148712ea60fb32b95404cd1; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=1; location-data=78758%3AAustin%3ATX%3A%3A1%3A1|2r5%3B%3B2.45%2C3ii%3B%3B2.87%2Cwx%3B%3B3.4%2Cd7%3B%3B6.94%2C487%3B%3B7.37%2Cvd%3B%3B7.52%2C2g1%3B%3B9.89%2C37n%3B%3B11.39%2C488%3B%3B11.54%2Cyt%3B%3B11.86||7|1|1yif%3B16%3B3%3B6.9%2C1yic%3B16%3B7%3B8.69%2C1yai%3B16%3B8%3B9.69%2C1yah%3B16%3B9%3B9.88; TB_DC_Flap_Test=0; bstc=dCBP2Au2Hdu0RWCuVtL8Ow; mobileweb=0; xpa=-INrT|-TbQt|5fGOp|FbH9D|k7ymV|s-848|xQAsH; exp-ck=-TbQt25fGOp1FbH9D1k7ymV2s-8481; xpm=1%2B1614869633%2BctJc8k1n2l-H0bhKTlEb6g~%2B0; next-day=1614949200|true|false|1615032000|1614870754; com.wm.reflector="reflectorid:imp_Q59y7gS2QxyOWjLwUx0Mo3bxUkEQiyV92wkIyM0@lastupd:1614870772011@firstcreate:1614789343641"; akavpau_p8=1614871376~id=771dc1008d8f78f456935b511b1bd391; _px3=6f9996d751d8a4c9301243e098536d364dfacbc63a3229703e5cdf0cd5b38b93:ZXfyRbDvRVarkwUeUzTYg+EnKYMaEWV3GUUEVEmk3+GBUjWTxwcRhymRyIf7LWkCoF8Mrrzfo5ARJdB6QkgUag==:1000:eGUP38XpRTf9G58O6bMQCT771RUIS3CZ1HKPKTjvdXhGADuJn5ojBwOGJ6njTl29oTlCAnJ5rl2HQ5va9TwNOaqUyFTmCB6VHjZY+lQLSCUwUCp6RH0SntYwGjVMRA7Xc14j1FnE4GqiJjrYaFBsVQo3eD+VPCT9fG3+7IE6Tv0=; _uetsid=b06a4b907b8f11eb87c7976f0e808a4f; _uetvid=682562f06ba911eb83cc131985bf9ae3; _uetmsclkid=_uetb02590e4009317db073df0da9ace3d87; TS01b0be75=01538efd7c61b17ec0c48bea56ce73aa8959ecdf24526e02a1e8f9086b7ea30ee397dd8083d5ef849f3b9b11d556a9f1228254a66d; _pxde=630468607a6dd48a46d7e7c67021f785eec690af3ea22fa8708d3b234a156871:eyJ0aW1lc3RhbXAiOjE2MTQ4NzA3ODU1NjksImZfa2IiOjAsImlwY19pZCI6W119; DL=78758%2C%2C%2Cip%2C78758%2C%2C; TB_DC_Flap_Test=0; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; TS012c809b=01538efd7c4fd265c8dd8bab0956ab49a396a520ac97f8bfe33ff08776faaf1bf4d4a70e5c9fe38f6b4366bcf6f3ed0558877d91dc; TS013ed49a=01538efd7c510cd3ed089d0050fe5606df279c9a24f5b201eae7efd54a9c80d9cfeaaee1bdb46c5d2a2148712ea60fb32b95404cd1; TS01af768b=01538efd7c4fd265c8dd8bab0956ab49a396a520ac97f8bfe33ff08776faaf1bf4d4a70e5c9fe38f6b4366bcf6f3ed0558877d91dc; bstc=dCBP2Au2Hdu0RWCuVtL8Ow; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1614714904452@firstcreate:1614714904452"; exp-ck=-TbQt25fGOp1FbH9D1k7ymV2s-8481; location-data=78758%3AAustin%3ATX%3A%3A1%3A1|2r5%3B%3B2.45%2C3ii%3B%3B2.87%2Cwx%3B%3B3.4%2Cd7%3B%3B6.94%2C487%3B%3B7.37%2Cvd%3B%3B7.52%2C2g1%3B%3B9.89%2C37n%3B%3B11.39%2C488%3B%3B11.54%2Cyt%3B%3B11.86||7|1|1yif%3B16%3B3%3B6.9%2C1yic%3B16%3B7%3B8.69%2C1yai%3B16%3B8%3B9.69%2C1yah%3B16%3B9%3B9.88; mobileweb=0; next-day=1614949200|true|false|1615032000|1614870371; vtc=ctJc8k1n2l-H0bhKTlEb6g; xpa=-INrT|-TbQt|5fGOp|FbH9D|k7ymV|s-848|xQAsH; xpm=1%2B1614870371%2BctJc8k1n2l-H0bhKTlEb6g~%2B0; TS01b0be75=01538efd7c9d7459270a299761280927c343994df49ebb78b89ab007e2315cff2e6afa33ace44f1032d6b95ffb6c530d0c929bec68; TS01bae75b=01538efd7c4fd265c8dd8bab0956ab49a396a520ac97f8bfe33ff08776faaf1bf4d4a70e5c9fe38f6b4366bcf6f3ed0558877d91dc; akavpau_p8=1614871469~id=442095169ca62999bc77674d25e718b4; x-csrf-jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiY29va2llIiwidXVpZCI6IjE0NWUwYTMwLTdiOGItMTFlYi05NGQ5LWY3ZTY3OTNiZjA2MCIsImlhdCI6MTYxNDcxMjI4MywiZXhwIjoxNjE1NzkyMjgzfQ.nOp8v_jGicWGxNFtaQuKUCQFoSIn3QEMBbpZJhJq2c0'
}

prods = pd.DataFrame([])

# for loops that loops through each page
for page in range(1,26):
  url = f"https://www.walmart.com/search/api/preso?cat_id=4096_530598&prg=desktop&page={page}&search_redirect=true"
  r = requests.get(url, headers=headers)
  data = json.loads(r.text)
  # data tag is 'items', however it can also be another tag such as 'products', update accordingly
  prods = prods.append(pd.json_normalize(data['items']), ignore_index=True)
  # 3 second interval between loops
  time.sleep(3)
  # message that indicates the page number and the start of a loop
  print(f'Getting page {page}', 'waiting..')

# output
prods.to_csv('walmart-products.csv')
