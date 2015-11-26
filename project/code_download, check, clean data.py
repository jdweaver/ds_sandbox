# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 17:41:53 2015

@author: joshuaw
"""

'''
This release contains the Basic Stand Alone (BSA) Outpatient Procedures Public Use Files (PUF) with information from Medicare 
outpatient claims. The CMS BSA Outpatient Procedures PUF is a procedure-level file in which each record is a procedure in an 
outpatient claim incurred by a 5% sample of Medicare beneficiaries. There are some demographic and claim-related variables provided 
in this PUF as detailed below. However, as claim or beneficiary identities are not provided, it is not possible to link procedures 
that belong to the same claim or beneficiary.

The CMS BSA Outpatient Procedures PUF originates from a 5% simple random sample of beneficiaries drawn (without replacement) 
from the 100% Beneficiary Summary File for the reference year. The sample that is used for the CMS BSA Outpatient Procedures PUF 
is disjoint from the existing 5% CMS research sample in the sense that there is no overlap in terms of the beneficiaries in the 
CMS BSA Outpatient Procedures PUF and the 5% CMS research sample. It is also disjoint from the other BSA PUFs (i.e., CMS 2008 
Inpatient Claims PUF, CMS 2008 PDE PUF, CMS 2008 DME Line Items PUF, and CMS 2008 Hospice Beneficiary PUF, CMS 2008 SNF Beneficiary 
PUF, CMS 2008 HHA Beneficiary PUF, and CMS 2008 Carrier Line Items PUF) that have been released so far. This property prevents users 
from linking data across multiple files for identification purposes.

In addition to the General documentation file, there is a data dictionary and codebook containing information about each variable 
on the file and its values, as well as formatted frequencies for each variable on the data file.
'''

import requests, zipfile, StringIO
import pandas as pd 

#download zip file and store it in an response object
# download each one separately for ease of data quality checking, 
#that way if we have to correct data we can do isolate in a single file
r1 = requests.get("http://downloads.cms.gov/BSAPUF/2008_BSA_Outpatient_Procedures_PUF_1.zip")
r2 = requests.get("http://downloads.cms.gov/BSAPUF/2008_BSA_Outpatient_Procedures_PUF_2.zip")
r3 = requests.get("http://downloads.cms.gov/BSAPUF/2008_BSA_Outpatient_Procedures_PUF_3.zip")

#check status of eacch 
r1.status_code


zipr1 = zipfile.ZipExtFile(StringIO.StringIO(r1.content))
