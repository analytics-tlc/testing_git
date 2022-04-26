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

# Chris - filter out everything but SHLs. SHLs are the ones that have permit number. End result should be a list shl of vins called vins





# Nikita - Decode that vins and return a dataframe with the vehicle info.




# John - Rename body classes so that we know how many sedans there are. 
# Final result should be a dataframe with 3 columns: industry, body_type, count

# step 1: identify body classes
# step 2: aggregate data (count *) and groupby industry, body_type



 