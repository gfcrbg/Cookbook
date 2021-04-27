'''
Walmart Scraper
'''

# This scraper extracts the .json file that holds the product information and exports the file to a .csv
# As a result, it's just Request and Output, no Parse.
# This web scraper will require you to download and install Postman.

# paste the Python-Requests code snippet from Postman; just the payload and headers; paste the url into the 'url' variable in the loop below (be mindful of the page insertion)
payload={}
headers = {
  'authority': 'www.walmart.com',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Microsoft Edge";v="90"',
  'wg-correlation-id': '939f2480-a798-11eb-ad95-3758a9d14de7',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46',
  'content-type': 'application/json',
  'accept': 'application/json',
  'x-csrf-jwt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiaGVhZGVyIiwidXVpZCI6IjdlYjgzMGMwLWE3OTgtMTFlYi05MWY4LWNiNTkyMjM0MDUzYSIsImlhdCI6MTYxOTU1NTg5NiwiZXhwIjoxNjIwNjM1ODk2fQ.g_yH3FibNOjUyuc8RvROjmDDA-pBB5YHscEnoGlcqU4',
  'wm_tenant_id': '0',
  'wm_vertical_id': '2',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.walmart.com/grocery/products?aisle=1255027787131_1255027788181&page=1',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'brwsr=ce7d7ed4-f08c-11ea-a4eb-42010a246cc1; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_DC_Flap_Test=0; g=0; g_e=0; vtc=WwdnKCY6Iop_OlUET32Hyk; bstc=WwdnKCY6Iop_OlUET32Hyk; mobileweb=0; xpa=FYF0D|OPRTJ|VN4MW|WqUNI|X6h5F|YhUuk|t4cqG|tWDgk; exp-ck=FYF0D2OPRTJ1VN4MW2WqUNI3YhUuk2t4cqG1tWDgk1; TS01bae75b=01538efd7c3a2dc6c20375dd483744bc2f7755a9781a7723f44a033830358f90af131aa5e63d2f25fbb4a2d2f9efbd87e0379a5adc; TS012c809b=01538efd7c3a2dc6c20375dd483744bc2f7755a9781a7723f44a033830358f90af131aa5e63d2f25fbb4a2d2f9efbd87e0379a5adc; TS01af768b=01538efd7c3a2dc6c20375dd483744bc2f7755a9781a7723f44a033830358f90af131aa5e63d2f25fbb4a2d2f9efbd87e0379a5adc; TBV=7; TS01b0be75=01538efd7c065f9ad55436f191738d612660e3100ad59e84a995b282a3feeef204deaf7d401ebb94ae0454790643f96f38ae65ea03; xpm=1%2B1619555754%2BWwdnKCY6Iop_OlUET32Hyk~%2B0; _pxvid=2a78560e-a798-11eb-8d20-0242ac120007; GCRT=ffe944a5-2663-45c1-af8f-30aef74713c5; hasGCRT=1; wm_mystore=Fe26.2**25876684f906b0081035ee8506c4bf266d3ca908c47a61c99eebe7748faab93a*9ZUh-xovueN9Km1le0jEMg*1dt4WDud-xRmY52er11pWVEUumF3ATnksO8z5i1dUrDp95E5XWIp4NOoznM0EIhzkAB8WhBVsmK4CY8G-13m217TRJphPTIEptuvB6nVuk4JD1J43BViS_T8MZygLjMikpqtbeRg31y03QJsjPfkzA**209579d8158c8e41f0491467bb59bfd2165d08979eae055bf8f6141fa60a7757*Zqgt9U43F9uBwfaMuAgk0WI-lX_6wfx2c99urmwSGBQ; ACID=2a6a28c0-a798-11eb-99de-33904092144d; hasACID=1; _gcl_au=1.1.1515152899.1619555755; s_vi=[CS]v1|30443AD62D584143-600003FB035D6691[CE]; __gads=ID=d69088d65e48995e:T=1619555756:S=ALNI_ManOHh6FOq4B2P-w19LXDrDMT96Ig; viq=Walmart; tb_sw_supported=true; TB_SFOU-100=1; _px3=75addf03682ea76e0900982d912f04cbd903e069181221fa735b8370a31cbff2:4qaG5ReqtPolr9UECZTdjvPOJGwDSklnOtylCtbF+xo0znyvzNYtbvoGtJdu1CjwjLGzpbAkdsBuL4zRExUMqA==:1000:4k4gjEcwK5wN6omnwcgRt2dCLNOVKk+fC1YiuGnPszXuhN0oe/wyUCEtRFV6DAdT3t1f9CwFjmj/tfpVIynaaAQMjkNKhmBDnO6giWUmWVCCv91EWsjYA0+r67unsuVdAvSO3LzVB33L8OWJbVrc/J7PXGS1BBxIxgjW5JtuULQ=; _pxde=881f323e2179fa350cdb2c881a0558dfe651fd04d21f62ebe288578a77875a0b:eyJ0aW1lc3RhbXAiOjE2MTk1NTU4MDUzMTMsImZfa2IiOjAsImlwY19pZCI6W119; x-csrf-jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiY29va2llIiwidXVpZCI6IjdlYjgzMGMwLWE3OTgtMTFlYi05MWY4LWNiNTkyMjM0MDUzYSIsImlhdCI6MTYxOTU1NTg5NiwiZXhwIjoxNjIwNjM1ODk2fQ.9yrAmY_52GHN4ktJCZGnJEkz7XOZ7XX-mYsuuZgpk9s; s_sess=%20ent%3DHomePage%257COVERLAY_VIEW%3B%20cp%3DY%3B%20cps%3D1%3B%20cmp%3Dseo_un%253A%3B%20chan%3Daff%3B%20v59%3DFruits%2520%2526%2520Vegetables%3B%20v54%3DHomePage%257COVERLAY_VIEW%2520%3B%20s_sq%3D%3B; akavpau_p14=1619556505~id=460ae00680ce7e9f1a4ad62246bba2bd; s_pers=%20s_cmpstack%3D%255B%255B%2527aff%2527%252C%25271619555803280%2527%255D%252C%255B%2527seo_un%2527%252C%25271619555929509%2527%255D%255D%7C1777322329509%3B%20s_fid%3D33C0028D080F0C6C-2EE6F3304A1DF27F%7C1682627931705%3B%20s_v%3DY%7C1619557731708%3B%20gpv_p11%3DFruits%2520%2526%2520Vegetables%253AFresh%2520Fruit%253AProduct%2520Range%7C1619557731722%3B%20gpv_p44%3Dno%2520value%7C1619557731725%3B%20s_vs%3D1%7C1619557731730%3B; DL=78758%2C%2C%2Cip%2C78758%2C%2C; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1614714904452@firstcreate:1614714904452"; vtc=ctJc8k1n2l-H0bhKTlEb6g'
}

prods = pd.DataFrame([])

# for loops that loops through each page
for page in range(1,5):
  url = f"https://www.walmart.com/grocery/v4/api/products/browse?count=60&offset=0&page={page}&storeId=3569&taxonomyNodeId=1255027787131_1255027788181"
  r = requests.get(url, headers=headers)
  data = json.loads(r.text)
  # data tag is 'items', however it can also be another tag such as 'products', update accordingly
  prods = prods.append(pd.json_normalize(data['products']), ignore_index=True)
  # 3 second interval between loops
  time.sleep(3)
  # message that indicates the page number and the start of a loop
  print(f'Getting page {page}', 'waiting..')

# output
prods.to_csv('walmart-products.csv')
