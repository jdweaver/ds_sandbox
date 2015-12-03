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

##unzip the file
#zipr1 = zipfile.ZipFile(StringIO.StringIO(r3.content))
#zipr1.open("2008_BSA_Outpatient_Procedures_PUF_3.csv")

#create a function that downloads and extracts each file into the 'data' folder
#we extract each file separately to avoid memory limits    
def extract_zip(url):
    import requests, zipfile, StringIO
    zip_file = requests.get(url)
    f = zipfile.ZipFile(StringIO.StringIO(zip_file.content))
    f.extractall("/ds_sandbox/project/data")
 
#list of urls for all files  
urls = ["http://downloads.cms.gov/BSAPUF/2008_BSA_Outpatient_Procedures_PUF_1.zip", "http://downloads.cms.gov/BSAPUF/2008_BSA_Outpatient_Procedures_PUF_2.zip", "http://downloads.cms.gov/BSAPUF/2008_BSA_Outpatient_Procedures_PUF_3.zip"]

#extract each zip file and palce it in the data folder
#note depending on your connection speed and memory this may take up to 18 minutes
for url in urls: 
    extract_zip(url)

#set the path and read in all files
#create empty list and dataframes for the loop
import glob
path = "/ds_sandbox/project/data/medicare"
files = glob.glob(path + "/*.csv")
df = pd.DataFrame()
clist = []

#loop through all csv files in the folder and combine them into a single data frame
for file_ in files:
    df = pd.read_csv(file_,index_col=None, header=0)
    clist.append(df)
df = pd.concat(clist)

#import icd-9 codes and descriptions file
df2 = pd.read_csv("THREE_DIGIT_ICD9_CODE_CATEGORIES.csv", sep=',', header=0, index_col=False)

#renamde the icd-9 file column to a column that can be joined to the medicare data
df2.rename(columns={'icd9_cd':'OP_CLM_ICD9_DIAG_CD'}, inplace=True)

#join icd-9 codes and descirptions file with the medicare data
dfm= df.merge(df2, on='OP_CLM_ICD9_DIAG_CD', how='left')

#create a new column that converts the integer values for sex into strings 
dfm['sex'] = dfm.BENE_SEX_IDENT_CD.map({1:'Male', 2:'Female'})

dfm['age_range'] = dfm.BENE_AGE_CAT_CD.map({1:'Under_65', 2:'65-69', 3:'70-74', 4:'75-79', 5:'80-84', 6:'85_and_older'})

#verify file by looking at shape, should have following shape: (31701499, 12)
dfm.shape
dfm.head(3)

#export new dataframe into csv
dfm.to_csv("medicare.csv", encoding='utf-8', index=False, header=True)


#######################################################################################################
#######################################################################################################
#######################################################################################################
`

import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 14
plt.style.use('fivethirtyeight')

#read in the new file and check that everything imported fine 
medicare = pd.read_csv("C:/medicare.csv", sep=",", header=0)

type(medicare)             # DataFrame
medicare.head()            # print the first 5 rows
medicare.tail()            # print the last 5 rows
medicare.columns           # column names (which is "an index"), 'u' indicates unicode encoding
medicare.dtypes            # data types of each column
medicare.shape             # number of rows (including header row) and columns.
                           # Total of 31701499 rows inclouding the header row

medicare.describe()       # describe all numeric

medicare.isnull().sum()   #count the nulls


#create new column that maps integer values for sex into string values
#leave integer values, for now 
#BENE_SEX_IDENT_CD.medicare.replace(1, 'Male', inplace=True)
#BENE_SEX_IDENT_CD.medicare.replace(2, 'Female', inplace=True)


#export to file 
#medicare.to_csv("medicare2.csv", encoding = 'utf-8')
#
#medicare.BENE_SEX_IDENT_CD.plot(kind='bar')
#
#medicare.BENE_SEX_IDENT_CD.plot(kind='bar', title = "Distribution of Sex in Sample")



#icd = df2.drop('Primary Diagnosis', axis=1)
#
#icd.head(10)
#
#icd['icd_short'] = icd.icd9.str[0:3]
#
#icdf = icd.drop('icd9', axis=1)
#
#icdf2 = icdf[['icd_short', 'Description 1']]




#create a dictionary from a dataframe--->icd_dict = dict(zip(icdf2.icd_short, icdf2.description))


