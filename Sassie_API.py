# 0TEP 1: Authentication
# Run this code block to generate an access token.
# An access token is valid for 1 hour.


import requests
import json
import csv
import pandas as pd
from google.colab import files


url = 'https://www.sassieshop.com/2mysteryshopinc/sapi/api/token'

payload = {
"grant_type": "client_credentials",
"client_id": "Qcf6EeJr6VqqNwZiTeBvSKKCCwjtH7az",
"client_secret": "vfGuKfbfM3AK1k7HlH1e3PfUJ4K4kfIm"   
}

r = requests.post(url, json=payload)

r.json()

# Run this to create the header.

print("Paste Access Token...")
accessToken = input()
headers = {'Authorization': f'bearer {accessToken}'}
print("Header ready for 1-hour usage.")

# ------------------------------------------------------

# STEP 2a: Fetch a single record
# Run this to retrieve information on a single record.
# Only relatives can be used in single job requests.

# https://www.sassieshop.com/2mysteryshopinc/sapi/api/OBJECT/ID/QUERY

# OBJECT
print("Enter object...")
obj = input()

# ID
print("Enter object ID...")
id = input()

# QUERY
print("Enter relatives...")
relatives = input()

payload = {
'relatives': f'{relatives}'
}

url = f'https://www.sassieshop.com/2mysteryshopinc/sapi/api/{obj}/{id}'

r = requests.get(url, headers=headers, params=payload)

dataA = r.json()

# output will display the single record - successful request
dataA

# ------------------------------------------------------

# STEP 2b: Fetch a list of multiple records
# Run this to retrieve information on multiple records.
# The following options can be used for multiple requests:

# relatives
# filterby
# sortby
# limit
# https://www.sassieshop.com/2mysteryshopinc/sapi/api/OBJECTS/QUERY

# OBJECTS
print("Enter object...")
objs = input()

# QUERY
print("Enter relatives...")
relatives = input()

print("Enter filter...")
filter = input()

print("Enter sort...")
sort = input()

print("Enter limit...")
limit = input()

payload = {
'relatives': f'{relatives}',
'filterby': f'{filter}',
'sortby': f'{sort}',
'limit': f'{limit}'
}

url = f'https://www.sassieshop.com/2mysteryshopinc/sapi/api/{objs}/'


r = requests.get(url, headers=headers, params=payload)

dataB = r.json()

# 200 successful request
r.status_code



# Preview dataB...

dataB

# ------------------------------------------------------

# STEP 3a: Export Record
# Run this to download the fetched record as a JSON file.
# This will save the file locally.


# exports a fetched record as a json file

df = pd.DataFrame(dataA)
print("Enter file name...")
filename = input() + '.json'
df.to_json(filename)
files.download(filename)
print(f"File saved to local drive as: {filename}")

# ------------------------------------------------------

# STEP 3b: Export Records
# Run this to download the fetched records as a JSON file.
# This will save the file locally.

# exports fetched records as a json file

df = pd.DataFrame(dataB)
print("Enter file name...")
filename = input() + '.json'
df.to_json(filename)
files.download(filename)
print(f"File saved to local drive as: {filename}")

# ------------------------------------------------------

# STEP 4: Convert
# JSON --> CSV
# Upload the downloaded file to the converter.
# Converter
