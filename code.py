# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 11:11:02 2022

@author: voevodinn
"""

# This is a test python script to check out the basic functionality of git
# Splitting this code in 4 parts. To avoid merging conflicts each of us can only modify his own part.


# Libraries . Lets keep it common. See what happens


import requests, json
import pandas as pd
import io
from sodapy import Socrata
from datetime import date, timedelta
import gc
import string
import zipfile
import requests, zipfile, io
import urllib
import numpy as np
from requests.packages.urllib3.util import Retry
from requests.adapters import HTTPAdapter
from requests import Session, exceptions




# Phillip - pull all active fhvs from open data. End result of you code should be a dataframe called active_fhvs


# using this until Phillip completes his part
active_fhvs = pd.read_csv("I:\\COF\\COF\\_DA&E_\\Nikita\\Python_Projects\\testing_git\\data.csv")

# Chris - filter out everything but SHLs. SHLs are the ones that have permit number. End result should be a list of shl vins called vins

shl= active_fhvs.loc[active_fhvs['Permit License Number'].notnull()]
shl_permits = shl['Vehicle VIN Number']
#vins = str(list(shl_permits.astype(str)))[1:-1]
#test

vins = shl['Vehicle VIN Number'].to_list()
# Nikita - Decode that vins and return a dataframe with the vehicle info.

# Yield successive n-sized 
# chunks from l. 
# =============================================================================
# def divide_chunks(l, n): 
#       
#     # looping till length l 
#     for i in range(0, len(l), n):  
#         yield l[i:i + n] 
#   
# # How many elements each 
# # list should have 
# n = 30
#   
# vins_chunks = list(divide_chunks(vins, n))
# 
# 
# df = pd.DataFrame()
# 
# 
# for i in vins_chunks:
# 
# 
# 
#     my_string = ';'.join(i)
# 
#     print(my_string)
#     s = Session()
#     url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
#     s.mount(url, HTTPAdapter(max_retries=Retry(total=2, backoff_factor=1, method_whitelist=frozenset(['GET', 'POST']), status_forcelist=[ 500, 502, 503, 504, 521])))
#     post_fields = {'format': 'json', 'data':f'{my_string}'}
#     r = requests.post(url, data=post_fields)
#     print(r.status_code)
#     x = r.json()
#     data = pd.DataFrame(x['Results'])[['VIN','Make','Model','ModelYear','BodyClass']]
#     df = df.append(data)
#     print('done')
# =============================================================================

# John - Rename body classes so that we know how many sedans there are. 
# Final result should be a dataframe with 3 columns: industry, body_type, count

# step 1: identify body classes
final_df = df.groupby(['Make', 'BodyClass'])['VIN'].count().reset_index()
final_df = final_df.rename(columns = {'BodyClass': 'body_type', 'Make':'industry', 'VIN':'count'})

# step 2: aggregate data (count *) and groupby industry, body_type

# step 3: push without updates

