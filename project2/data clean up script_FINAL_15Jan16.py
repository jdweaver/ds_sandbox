# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 16:28:00 2015

@author: joshuaw
"""



''' 
IMPORT AND CONCATENATE/UNION ALL 5 EXCEL FILES  IMPORT AND CONCATENATE/UNION ALL 5 EXCEL FILES
IMPORT AND CONCATENATE/UNION ALL 5 EXCEL FILES  IMPORT AND CONCATENATE/UNION ALL 5 EXCEL FILES
IMPORT AND CONCATENATE/UNION ALL 5 EXCEL FILES  IMPORT AND CONCATENATE/UNION ALL 5 EXCEL FILES

note: the raw csv files had the following edits done to them 
1) removed first 3 rows that included download and metadata information 
   (this was included from the survey platform)
2) moved all header columns to a single row, the header column was two rows
3) item column headers had sequential numbers appended to them (e.g. 
   "15 - Job Performance1", "15 - Job Performance2") this was done as a 
   precautionary step to ensure that the columns would concatenate/union 
   all correctly using the for loop
''' 

#import required packages and set parameters for creating data visualisations and set visualization style color
import glob
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 14
plt.style.use('bmh')

#verify csv files are showing up
glob.glob('C:/Users/Joshuaw/Documents/PhD_Year_5/Data/Raw_Survey/*.csv')

'''
the code commented out below is code to help check that the 
concatenation/union all of the survey files was happening correctly 
i.e. making sure columns were being mapped to the correct columns
'''
##read in each file individually into it's own data frame
#df = pd.read_csv('C:/Users/Joshuaw/Documents/PhD_Year_5/Data/Raw_Survey/11.13.15_Responses_340.csv', index_col=False, header=0, encoding='utf-8')
#df1 = pd.read_csv('C:/Users/Joshuaw/Documents/PhD_Year_5/Data/Raw_Survey/11.21.15_Responses_235.csv', index_col=False, header=0, encoding='utf-8')
#df2 = pd.read_csv('C:/Users/Joshuaw/Documents/PhD_Year_5/Data/Raw_Survey/11.28.15_Responses_196.csv', index_col=False, header=0, encoding='utf-8')
#df3 = pd.read_csv('C:/Users/Joshuaw/Documents/PhD_Year_5/Data/Raw_Survey/12.07.15_Responses_134.csv', index_col=False, header=0, encoding='utf-8')
#df4 = pd.read_csv('C:/Users/Joshuaw/Documents/PhD_Year_5/Data/Raw_Survey/01.08.16_Responses_36.csv', index_col=False, header=0, encoding='utf-8')
#
##append each dataframe to the data frame before it to create a single data frame of all data
#dat = df.append(df1, ignore_index=True)
#dat1 = dat.append(df2, ignore_index=True)
#dat2 = dat1.append(df3, ignore_index=True)
#
##write dataframe to file
#dat2.to_csv("dissertation_test_ind.csv", encoding='utf-8', index=False, header=True)


#loop through all csv files in the folder and combine them into a single data frame
path = "C:/Users/Joshuaw/Documents/PhD_Year_5/Data/Raw_Survey"
files = glob.glob(path + "/*.csv")
df = pd.DataFrame()
for file_ in files:
    f = pd.read_csv(file_,index_col=False, header=0, encoding='utf-8')
    df = df.append(f, ignore_index=True)
    
#write dataframe created with a loop to file 
df.to_csv("dissertation_merge", encoding='utf-8', index=False, header=True)
    
'''
DATA CLEAN UP   DATA CLEAN UP   DATA CLEAN UP   DATA CLEAN UP   DATA CLEAN UP 
DATA CLEAN UP   DATA CLEAN UP   DATA CLEAN UP   DATA CLEAN UP   DATA CLEAN UP
DATA CLEAN UP   DATA CLEAN UP   DATA CLEAN UP   DATA CLEAN UP   DATA CLEAN UP

split the '8 - Location' column into multiple columns to obtain the city as a 
separate column
Note: the split isn't clean but since we already have a country code all we
need is the city for visualization in Tableau.
'''
s = df['8 - Location'].str.split(',').apply(pd.Series,1)
s.name = '8 - Location' #we need a name to be able to join it to the original dataframe
del df['8 - Location'] #drop the location column
#df1 = df.join(s) #join the 10 columns back to the dataframe 
dat = pd.concat([df, s], axis=1)
df = dat #rename the dataframe back to df, for consistency

'''
delete columns: these columns were part of the survey but don't contain 
relevant data
'''
df.drop(['Response Status', 'Seq. Number', 'External Reference', 
       'Respondent Email', 'Email List', '1 - INTRO', '3 - Demographics_header', 
       '14 - Work_Behavior_Header', 	
       'Spot_The_Word_Test:...........1',	   'Spot_The_Word_Test:...........2',	
       'Spot_The_Word_Test:...........3',	   'Spot_The_Word_Test:...........4',	
       'Spot_The_Word_Test:...........5',	   'Spot_The_Word_Test:...........6',	
       'Spot_The_Word_Test:...........7',	   'Spot_The_Word_Test:...........8',	
       'Spot_The_Word_Test:...........9',	   'Spot_The_Word_Test:...........10',	
       'Spot_The_Word_Test:...........11',    'Spot_The_Word_Test:...........12',	
       'Spot_The_Word_Test:...........13',    'Spot_The_Word_Test:...........14',	
       'Spot_The_Word_Test:...........15',    'Spot_The_Word_Test:...........16',	
       'Spot_The_Word_Test:...........17',    'Spot_The_Word_Test:...........18',
       'Spot_The_Word_Test:...........19',    'Spot_The_Word_Test:...........20',	
       'Spot_The_Word_Test:...........21',	'Spot_The_Word_Test:...........22',	
       'Spot_The_Word_Test:...........23',	'Spot_The_Word_Test:...........24',	
       'Spot_The_Word_Test:...........25',	'Spot_The_Word_Test:...........26',	
       'Spot_The_Word_Test:...........27',	'Spot_The_Word_Test:...........28',	
       'Spot_The_Word_Test:...........29',	'Spot_The_Word_Test:...........30',	
       'Spot_The_Word_Test:...........31',	'Spot_The_Word_Test:...........32',	
       'Spot_The_Word_Test:...........33',	'Spot_The_Word_Test:...........34',	
       'Spot_The_Word_Test:...........35',	'Spot_The_Word_Test:...........36',	
       'Spot_The_Word_Test:...........37',	'Spot_The_Word_Test:...........38',	
       'Spot_The_Word_Test:...........39',	'Spot_The_Word_Test:...........40',	
       'Spot_The_Word_Test:...........41',	'Spot_The_Word_Test:...........42',	
       'Spot_The_Word_Test:...........43',	'Spot_The_Word_Test:...........44',	
       'Spot_The_Word_Test:...........45',	'Spot_The_Word_Test:...........46',	
       'Spot_The_Word_Test:...........47',	'Spot_The_Word_Test:...........48',	
       'Spot_The_Word_Test:...........49',	'Spot_The_Word_Test:...........50',	
       'Spot_The_Word_Test:...........51',	'Spot_The_Word_Test:...........52',	
       'Spot_The_Word_Test:...........53',	'Spot_The_Word_Test:...........54',	
       'Spot_The_Word_Test:...........55',	'Spot_The_Word_Test:...........56',	
       'Spot_The_Word_Test:...........57',	'Spot_The_Word_Test:...........58',
       'Spot_The_Word_Test:........... 59'], axis =1, inplace=True)

#rename the columns to make them more pythonic and easy to type
#first create a list that contains the new names for the columns
df_cols = ['Response_ID', 'IP_Address', 'Timestamp', 'Device_Data',	
              'SecondsToComplete', 'Country_Code', 'Region', 'Resume',	
              'Age', 'Gender', 'Race', 'Education', 'Industry', 'Job_Level',	
              'Years_Experience', 'Hours_Week', 'Salary',	'Job_Performance1',	
              'Job_Performance2', 'Job_Performance3',	'Job_Performance4',
              'Job_Performance5', 'Job_Performance6',	'Job_Performance7',	
              'Job_Performance8', 'Job_Performance9',	'Job_Performance10',	
              'Job_Performance11', 'Job_Performance12', 'Job_Performance13',	
              'Job_Performance14', 'Job_Performance15', 'Job_Performance16',	
              'Job_Performance17', 'Job_Performance18', 'Impression_Work1',	
              'Impression_Work2', 'Impression_Work3',	'Impression_Work4',	
              'Impression_Work5', 'Impression_Work6',	'Impression_Work7',	
              'Impression_Work8', 'Impression_Work9',	'Impression_Work10', 
              'Spot_The_Word_Test:slank', 'Spot_The_Word_Test:chariot',	
              'Spot_The_Word_Test:lentil', 'Spot_The_Word_Test:glotex',	
              'Spot_The_Word_Test:stamen',	'Spot_The_Word_Test:dombus',	
              'Spot_The_Word_Test:loba',	'Spot_The_Word_Test:comet',	
              'Spot_The_Word_Test:pylon',	'Spot_The_Word_Test:stroin',	
              'Spot_The_Word_Test:scrapten',	'Spot_The_Word_Test:flannel',	
              'Spot_The_Word_Test:fender',	'Spot_The_Word_Test:ullus',	
              'Spot_The_Word_Test:ragspur',	'Spot_The_Word_Test:joust',	
              'Spot_The_Word_Test:milliary',	'Spot_The_Word_Test:mantis',	
              'Spot_The_Word_Test:sterile',	'Spot_The_Word_Test:palth',	
              'Spot_The_Word_Test:proctive',	'Spot_The_Word_Test:monotheism',	
              'Spot_The_Word_Test:glivular',	'Spot_The_Word_Test:stallion',	
              'Spot_The_Word_Test:intervantation', 'Spot_The_Word_Test:rictus',	
              'Spot_The_Word_Test:byzantine',	'Spot_The_Word_Test:chloriant',	
              'Spot_The_Word_Test:monologue',	'Spot_The_Word_Test:rufine',	
              'Spot_The_Word_Test:elegy',	'Spot_The_Word_Test:festant',	
              'Spot_The_Word_Test:malign',	'Spot_The_Word_Test:vago',	
              'Spot_The_Word_Test:exonize',	'Spot_The_Word_Test:gelding',	
              'Spot_The_Word_Test:bulliner',	'Spot_The_Word_Test:trireme',	
              'Spot_The_Word_Test:visage',	'Spot_The_Word_Test:hyperlisitc',	
              'Spot_The_Word_Test:froin',	'Spot_The_Word_Test:oratory',	
              'Spot_The_Word_Test:meridian',	'Spot_The_Word_Test:phillidism',	
              'Spot_The_Word_Test:grottle',	'Spot_The_Word_Test:strumpet',	
              'Spot_The_Word_Test:equine',	'Spot_The_Word_Test:psynomy',	
              'Spot_The_Word_Test:baggalette',	'Spot_The_Word_Test:riposte',	
              'Spot_The_Word_Test:valance',	'Spot_The_Word_Test:plesmoid',	
              'Spot_The_Word_Test:introvert',	'Spot_The_Word_Test:vinadism',	
              'Spot_The_Word_Test:penumbra',	'Spot_The_Word_Test:rubiant',	
              'Spot_The_Word_Test:breen',	'Spot_The_Word_Test:malinger',	
              'Spot_The_Word_Test:gammon',	'Spot_The_Word_Test:unterried',	
              'Spot_The_Word_Test:coracle',	'Spot_The_Word_Test:prestasis',	
              'Spot_The_Word_Test:paramour',	'Spot_The_Word_Test:imbulasm',	
              'Spot_The_Word_Test:dallow',	'Spot_The_Word_Test:octaroon',	
              'Spot_The_Word_Test:fleggary',	'Spot_The_Word_Test:carnation',	
              'Spot_The_Word_Test:liminoid',	'Spot_The_Word_Test:agnostic',	
              'Spot_The_Word_Test:naquescent',	'Spot_The_Word_Test:plinth',	
              'Spot_The_Word_Test:thole',	'Spot_The_Word_Test:leptine',	
              'Spot_The_Word_Test:crattish',	'Spot_The_Word_Test:reform',	
              'Spot_The_Word_Test:wraith',	'Spot_The_Word_Test:stribble',	
              'Spot_The_Word_Test:metulate',	'Spot_The_Word_Test:pristine',	
              'Spot_The_Word_Test:pauper',	'Spot_The_Word_Test:progotic',	
              'Spot_The_Word_Test:aurant',	'Spot_The_Word_Test:baleen',	
              'Spot_The_Word_Test:palindrome',	'Spot_The_Word_Test:lentathic',
              'Spot_The_Word_Test:hedgehog',	'Spot_The_Word_Test:mordler',	
              'Spot_The_Word_Test:prassy',	'Spot_The_Word_Test:ferret',	
              'Spot_The_Word_Test:torbate',	'Spot_The_Word_Test:drumlin',	
              'Spot_The_Word_Test:texture',	'Spot_The_Word_Test:disenrupted',	
              'Spot_The_Word_Test:isomorphic',	'Spot_The_Word_Test:thassiary',	
              'Spot_The_Word_Test:fremoid',	'Spot_The_Word_Test:vitriol',	
              'Spot_The_Word_Test:farrago',	'Spot_The_Word_Test:gesticity',	
              'Spot_The_Word_Test:minidyne',	'Spot_The_Word_Test:hermeneutic',	
              'Spot_The_Word_Test:pusality',	'Spot_The_Word_Test:chaos',	
              'Spot_The_Word_Test:devastate',	'Spot_The_Word_Test:prallage',	
              'Spot_The_Word_Test:peremptory',	'Spot_The_Word_Test:paralepsy',	
              'Spot_The_Word_Test:chalper',	'Spot_The_Word_Test:camera',	
              'Spot_The_Word_Test:roster',	'Spot_The_Word_Test:fallulate',	
              'Spot_The_Word_Test:scaline',	'Spot_The_Word_Test:accolade',	
              'Spot_The_Word_Test:methagenate',	'Spot_The_Word_Test:pleonasm',
              'Spot_The_Word_Test:drobble',	'Spot_The_Word_Test:infiltrate',	
              'Spot_The_Word_Test:mystical',	'Spot_The_Word_Test:harreen',	
              'Grit1',	'Grit2',	'Grit3',	'Grit4',	'Grit5',	'Grit6',	'Grit7',	
              'Grit8',	'Location1',	'Location2',	'Location3',	'Location4',	
              'Location5',	'Location6',	'Location7',	'Location8',	'Location9',	
              'Location10']
              
#rename columns using the list that was just created	
df.columns = df_cols


'''
RECODE VARIABLES, CREATE CATEGORICAL STRING VARIABLES, & AGGREGATE ITEMS TO VARIABLE
LEVEL
RECODE VARIABLES, CREATE CATEGORICAL STRING VARIABLES, & AGGREGATE ITEMS TO VARIABLE
LEVEL
RECODE VARIABLES, CREATE CATEGORICAL STRING VARIABLES, & AGGREGATE ITEMS TO VARIABLE
LEVEL

take categorical variables which currently have integer values and map them
to their corresponding string variables easiest to create new columns in the 
data set 
'''
#create new gender column with string labels
df['gender_string'] = df.Gender.map({2:'F', 1:'M'})
df.gender_string.value_counts()#verify recode worked 
'''
N = 847
M: 561 (66.23%); rounded to 2 decimal places
F: 286 (33.77%); rounded to 2 decimal places
'''
#recode gender to 0 and 1 
df['Gender'] = df.Gender.map({1:0, 2:1})
df.Gender.describe() #verify recode worked

#recode race
df['race_string'] = df.Race.map({1:'Hispanic or Latino', 
    2:'American Indian or or Alaska Native', 
    3:'Asian', 4:'African American', 
    5:'Native Hawaiian or Other Pacific Islander', 6:'White', 7:'Other'})
    
"race_string" in df #check that column was created
df.race_string.value_counts()#verify recode worked 
'''
N = 847
White: 530 (62.57%)
Asian: 220 (25.97%)
Hispanic or Latino: 33 (3.90%)
Other: 32 (3.87%)
African American                              28 (3.31%)
Native Hawaiian or Other Pacific Islander      3 (0.35%)
American Indian or or Alaska Native            1 (0.12%)
'''

#recode Education 
df['education_string'] = df.Education.map({1:'High School', 2:'Some College',
    3:'Trade, Vocational, or Technical', 4:'Associates', 5:'Bachelors',
    6:'Masters', 7:'Professional', 8:'Doctorate'})

"education_string" in df # check that column was created 
df.education_string.value_counts()
'''
N = 847
Bachelors                          358 (42.27%)
Masters                            165 (19.48%)
Some College                       110 (12.99%)
Doctorate                           60 (7.08%)
Professional                        45 (5.31%)
High School                         42 (4.96%)
Associates                          36 (4.25%)
Trade, Vocational, or Technical     31 (3.66%)
'''

#recode industry
df['industry_string'] = df.Industry.map({1:'Automotive', 2:'Advertising',
    3:'Consulting Services', 4:'Education', 5:'Entertainment', 
    6:'Financial Services', 7:'Government Services', 8:'Healthcare',
    9:'Human Resources', 10:'Information Technology', 11:'Marketing Sales',
    12:'Non-Profit', 13:'Pharmaceuticals', 14:'Public Relations', 
    15:'Technical Services', 16:'Travel', 17:'Other'})

"industry_string" in df #check that column was created
df.industry_string.value_counts()
'''
N =  847
Information Technology    173 (20.43%)
Other                     143 (16.88%)
Education                  95 (11.22%)
Healthcare                 73 (8.62%)
Marketing Sales            61 (7.20%)
Financial Services         56 (6.61%)
Technical Services         44 (5.19%)
Government Services        36 (4.25%)
Consulting Services        34 (4.01%)
Non-Profit                 23 (2.72%)
Entertainment              21 (2.48%)
Advertising                20 (2.36%)
Automotive                 19 (2.24%)
Pharmaceuticals            17 (2.01%)
Human Resources            15 (1.77%)
Travel                     14 (1.65%)
Public Relations            3 (0.35%)
'''

#recode job role 
df['job_level_string'] = df.Job_Level.map({1:'Intern', 2:'Entry Level', 
    3:'Analyst / Associate', 4:'Project or Product Manager', 5:'Manager',
    6:'Senior Manager', 7:'Director', 8:'Director', 9:'Senior Director', 
    10:'Vice President', 11:'Senior Vice President', 12:'C Level Executive',
    13:'President / CEO', 14:'Owner'})

"job_level_string" in df #check that column was created 
df.job_level_string.value_counts()

'''
N = 847

Analyst / Associate           250 (29.52%)
Entry Level                   201 (23.73%)
Manager                       140 (16.53%)
Project or Product Manager    105 (12.40%)
Senior Manager                 39 (4.60%)
Intern                         36 (4.25%)
Owner                          33 (3.90%)
Director                       30 (3.54)
President / CEO                 4 (0.47%)
Senior Director                 4 (0.47%)
C Level Executive               2 (0.24%)
Vice President                  2 (0.24%)
Senior Vice President           1 (0.12%)
'''

#descriptives for average hours worked 
df.Hours_Week.describe() #returns a values_counts() type result, these should be float numbers 
type(df.Hours_Week) #check the data type for this column, it's a series object
df['hours'] = pd.to_numeric(df.Hours_Week, errors='coerce')
#convert the object to a float, by creating a new column 
#drop the other column
df.drop(['Hours_Week'], axis =1, inplace=True)

#run descriptives on hours
df.hours.describe()
df.hours.median()
df.hours.mode()

'''
count     900.000000
mean       45.213611
std       100.274964
min         0.000000
25%        40.000000
50%        40.000000
75%        45.000000
max      3000.000000

We can see that there are some values that are not within an expected range
given that participants had be working full time (min of 32 hours) and there
are not 3,000 hours in a week so we replace out of range values with the 
mode/median. 

Total cases = 54

'''
df.hours.replace(0, 40, inplace=True) 
#since there are multiple let's switch how we use replace 
df.replace({'hours': {0:40, 1:40, 2:40, 3:40, 4:40, 5:40, 6:40, 7:40, 8:40, 9:40,
                 10:40, 15:40, 16:40, 20:40, 24:40, 25:40, 26:40, 28:40,
                 30:40, 3000:40, 480:40, 150:40}}, inplace=True)
                 
#re-run describe to verify that the descriptives look right 
df.hours.describe()
'''
count    846.000000
mean      42.662825
std        7.659092
min       32.000000
25%       40.000000
50%       40.000000
75%       45.000000
max      100.000000
'''

#recode salary 
df['salary_string'] = df.Salary.map({1:'10-20K', 2:'21-40K', 3:'41-60K',
    4:'61-80K', 5:'81-100K', 6:'101-149K', 7:'150K+'})

"salary_string" in df #check that column was created 
df.salary_string.value_counts()

'''
N = 847
10-20K      283 (33.42%)
21-40K      273 (32.23%)
41-60K      148 (17.47%)
61-80K       69 (8.15%)
81-100K      36 (4.25%)
101-149K     22 (2.60%)
150K+        16 (1.89%)
'''

#recode age
df['age_string'] = df.Age.map({1:'18-24', 2:'25-34', 3:'35-44', 4:'45-55',
    5:'55-64', 6:'65+'})

"age_string" in df
df.age_string.value_counts()

'''
N = 847
25-34    466 (55.02%)
18-24    232 (27.39%)
35-44    103 (12.16%)
45-55     34 (4.01%)
55-64     11 (1.30%)
65+        1 (0.12%)
'''


'''We need to recode all of our Job Performance variables from their current 
Likert 1-5 scale to a 0-4 scale, so we can properly create our job performance
variable and run diagnostics on items. To do this we do vector addition (or 
really subtraction) because we are subtracting 1 from every column. 

We can either create a list of the columns and then write a for loop or do a 
more elegant vector addition
'''
#changing using a loop, create a list of column headers then loop through and 
#subtract 1 
jp = ['Job_Performance1',
      'Job_Performance2',
      'Job_Performance3',
      'Job_Performance4',
      'Job_Performance5',
      'Job_Performance6',
      'Job_Performance7',
      'Job_Performance8',
      'Job_Performance9',
      'Job_Performance10',
      'Job_Performance11',
      'Job_Performance12',
      'Job_Performance13',
      'Job_Performance14',
      'Job_Performance15',
      'Job_Performance16',
      'Job_Performance17',
      'Job_Performance18']

#subtract 1 using a for loop      
#for col in jp:
#    df[col] = df[col] -1

#vector addition
df[jp] = df[jp] -1

#verify that the range is now 0-4 
df.Job_Performance1.describe()
'''
count    847.000000
mean       2.870130
std        1.047181
min        0.000000
25%        2.000000
50%        3.000000
75%        4.000000
max        4.000000
Name: Job_Performance1, dtype: float64
'''
df.Job_Performance18.describe()
'''
count    847.000000
mean       1.343566
std        1.208237
min        0.000000
25%        0.000000
50%        1.000000
75%        2.000000
max        4.000000
Name: Job_Performance18, dtype: float64
'''


'''
CREATE JOB PERFORMANCE VARIABLES OF TASK PERFROAMCNE, CONTEXTUAL PERFORMANCE,
AND COUNTER PRODUCTIVE PERFORMANCE
'''
#create variables for TASK PERFORMANCE and look at descriptives for this variable 
df['task_performance'] = ((df.Job_Performance1 + df.Job_Performance2 + df.Job_Performance3 + 
                            df.Job_Performance4 + df.Job_Performance5)/5)
df.task_performance.isnull().sum()
df.task_performance.describe()        
df.task_performance.median()
'''
count    847.00000
mean       2.91405
median     3.00000
std        0.77379
min        0.40000
25%        2.40000
50%        3.00000
75%        3.40000
max        4.00000
'''
#run cronbach's alpha (note: had to do this in SPSS)
CronbachAlpha(task)
0.87 
                                                
#create variables for CONTEXTUAL PERFORMANCE and look at descriptives for this variable                             
df['contextual_performance'] = ((df.Job_Performance6 + df.Job_Performance7 + df.Job_Performance8 + 
                            df.Job_Performance9 + df.Job_Performance10 + df.Job_Performance11 +
                            df.Job_Performance12 + df.Job_Performance13)/8)
df.contextual_performance.isnull().sum()
df.contextual_performance.describe()
df.contextual_performance.median()
'''
count    847.000000
mean       2.622639
median     2.625000
std        0.760560
min        0.125000
25%        2.125000
50%        2.625000
75%        3.125000
max        4.000000
'''
#run cronbach's alpha 
CronbachAlpha(contextual)
0.85

#create variables for COUNTER-PRODUCTIVE PERFORMANCE and look at descriptives for this variable                             
df['cwb'] = ((df.Job_Performance14 + df.Job_Performance15 + df.Job_Performance16 + 
                            df.Job_Performance17 + df.Job_Performance18)/5)
df.cwb.isnull().sum()
df.cwb.describe()
df.cwb.median()
'''
count    847.000000
mean       1.246753
std        0.949349
min        0.000000
25%        0.600000
50%        1.000000
75%        1.800000
max        4.000000
'''
#run cronbahc's alpha: 
CronbachAlpha(cwb)
0.87

'''
CREATE IMPRESSION MANAGEMENT VARIABLE
note: initially I created mean scaled scores, but the original manuscript detailing the creation of
this measure states that scores should be summed. I've checked both variable creation approaches and 
they do not change the relationship with LIWC pronoun categories, it only changes the values of the 
descriptive statistics reported 
'''
#df['impression'] = ((df.Impression_Work1 + df.Impression_Work2 + df.Impression_Work3 + 
#                     df.Impression_Work4 + df.Impression_Work5 + df.Impression_Work6 + 
#                     df.Impression_Work7 + df.Impression_Work8 + df.Impression_Work9 + 
#                     df.Impression_Work10)/10)
#                     
#df.impression.isnull().sum()
#df.impression.describe()
#df.impression.median()
'''
impression management, full variable
count    847.000000
mean       4.292798
median     4.300000
std        1.082532
min        1.000000
25%        3.700000
50%        4.300000
75%        5.000000
max        7.000000
'''
#run cronbahc's alpha 
CronbachAlpha(impression)
0.84

df['impression_other'] = (df.Impression_Work1 + df.Impression_Work2 + df.Impression_Work3 + 
                             df.Impression_Work4 + df.Impression_Work5)
df.impression_other.describe()
df.impression_other.median()
'''
count    847.000000
mean      16.345927
median    16.000000 
std        7.596475
min        5.000000
25%       10.000000
50%       16.000000
75%       22.000000
max       35.000000
'''
#run cronbahc's alpha 
CronbachAlpha(impression_other)
0.87
                     
df['impression_self'] = (df.Impression_Work6 + df.Impression_Work7 + df.Impression_Work8 + 
                            df.Impression_Work9 + df.Impression_Work10)
df.impression_self.describe()
df.impression_self.median()
'''
count    847.000000
mean      26.603306
median    28.000000
std        6.114038
min        5.000000
25%       23.000000
50%       28.000000
75%       31.000000
max       35.000000
'''
#run cronbahc's alpha 
CronbachAlpha(impression_self)
0.84  
    

'''
CREATE SPOT-THE-WORD TEST SCORE
'''                   
df['stw_score'] = df[["Spot_The_Word_Test:chariot", "Spot_The_Word_Test:lentil", 
                   "Spot_The_Word_Test:stamen", "Spot_The_Word_Test:comet", 
                   "Spot_The_Word_Test:pylon", "Spot_The_Word_Test:flannel", 
                   "Spot_The_Word_Test:fender", "Spot_The_Word_Test:joust",
                   "Spot_The_Word_Test:mantis", "Spot_The_Word_Test:sterile", 
                   "Spot_The_Word_Test:monotheism", "Spot_The_Word_Test:stallion",
                   "Spot_The_Word_Test:rictus", "Spot_The_Word_Test:byzantine",
                   "Spot_The_Word_Test:monologue", "Spot_The_Word_Test:elegy",
                   "Spot_The_Word_Test:malign", "Spot_The_Word_Test:gelding",
                   "Spot_The_Word_Test:bulliner", "Spot_The_Word_Test:visage", 
                   "Spot_The_Word_Test:oratory", "Spot_The_Word_Test:meridian",	
                   "Spot_The_Word_Test:strumpet", "Spot_The_Word_Test:equine",
                   "Spot_The_Word_Test:riposte", "Spot_The_Word_Test:valance",
                   "Spot_The_Word_Test:introvert", "Spot_The_Word_Test:penumbra",
                   "Spot_The_Word_Test:malinger", "Spot_The_Word_Test:gammon",
                   "Spot_The_Word_Test:coracle", "Spot_The_Word_Test:paramour",
                   "Spot_The_Word_Test:octaroon", "Spot_The_Word_Test:carnation",	
                   "Spot_The_Word_Test:agnostic", "Spot_The_Word_Test:plinth", 
                   "Spot_The_Word_Test:thole", "Spot_The_Word_Test:reform",	
                   "Spot_The_Word_Test:wraith", "Spot_The_Word_Test:pristine",	
                   "Spot_The_Word_Test:pauper", "Spot_The_Word_Test:baleen",	
                   "Spot_The_Word_Test:palindrome", "Spot_The_Word_Test:hedgehog",	
                   "Spot_The_Word_Test:ferret", "Spot_The_Word_Test:drumlin",
                   "Spot_The_Word_Test:texture", "Spot_The_Word_Test:isomorphic",
                   "Spot_The_Word_Test:vitriol", "Spot_The_Word_Test:farrago",
                   "Spot_The_Word_Test:hermeneutic", "Spot_The_Word_Test:chaos",
                   "Spot_The_Word_Test:devastate", "Spot_The_Word_Test:peremptory",
                   "Spot_The_Word_Test:camera", "Spot_The_Word_Test:roster",
                   "Spot_The_Word_Test:accolade", "Spot_The_Word_Test:pleonasm",
                   "Spot_The_Word_Test:infiltrate",	 "Spot_The_Word_Test:mystical"]].sum(axis=1)            
df.stw_score.isnull().sum()
df.stw_score.describe()
df.stw_score.median()
'''
count    847.000000
mean      45.518300
median    49.000000
std       12.008836
min        0.000000
25%       44.000000
50%       49.000000
75%       52.000000
max       59.000000
alpha      0.951000
'''
#run cronbahc's alpha                 
0.87

'''
CREATE DUMMY VARIABLES
'''
#AGE
age_dummy = pd.get_dummies(df['age_string'], prefix='age') #create dummy variable dataframe
df1 = pd.concat([df, age_dummy], axis=1) #join dummy dataframe to original dataframe
df1.drop(['age_25-34'], inplace=True, axis=1) 
#drop one of the dummy variables since it is redundent (k-1)
#here we drop the largest group, which is 25-34 year olds to make that our reference group 

#SEX: already created since it is dichotomous and we recoded to 0 and 1 earlier 

#RACE 
race_dummy = pd.get_dummies(df1['race_string'], prefix='race') #create dummy variable dataframe
df2 = pd.concat([df1, race_dummy], axis=1) #join dummy dataframe to original dataframe
df2.drop(['race_White'], inplace=True, axis=1)
#drop one of the dummy variables since it is redundent (k-1)
#here we drop race_white dummary variable, making whites our reference group 

#INDUSTRY 
industry_dummy = pd.get_dummies(df1['industry_string'], prefix='industry') 
#create dummy variable dataframe
df3 = pd.concat([df2, industry_dummy], axis=1) #join dummy dataframe to original dataframe
df3.drop(['industry_Information Technology'], inplace=True, axis=1)
#drop one of the dummy variables since it is redundent (k-1)
#here we drop Information Technology dummary variable, making Information Technology our reference group 

#SALARY 
salary_dummy = pd.get_dummies(df1['salary_string'], prefix='salary') 
#create dummy variable dataframe
df4 = pd.concat([df3, salary_dummy], axis=1) #join dummy dataframe to original dataframe
df4.drop(['salary_21-40K'], inplace=True, axis=1)
#drop one of the dummy variables since it is redundent (k-1)
#here we drop salary_21-40K dummary variable, making 21-40K our reference group 

#JOB ROLE 
job_level_dummy = pd.get_dummies(df1['job_level_string'], prefix='job_level') 
#create dummy variable dataframe
df5 = pd.concat([df4, job_level_dummy], axis=1) #join dummy dataframe to original dataframe
df5.drop(['job_level_Analyst / Associate'], inplace=True, axis=1)
#drop one of the dummy variables since it is redundent (k-1)
#here we drop salary_21-40K dummary variable, making 21-40K our reference group 

#EDUCATION 
education_level_dummy = pd.get_dummies(df['education_string'], prefix='education')
#create dummy variable dataframe
df6 = pd.concat([df5, education_level_dummy], axis=1) #join dummy dataframe to original dataframe
df6.drop(['education_Bachelors'], inplace=True, axis=1)

#rename df6 to final
final = df6

'''
Read in both the final survey data and the text analylsis file generated by LIWC
'''
#cleaned up survey data, with dummy variables
df = pd.read_csv('dissertation_complete_spss_15Jan15a.csv', header=0, encoding='utf-8') 

#text analysis file generated by liwc 
dft = pd.read_csv('C:\Users\joshuaw\Documents\PhD_Year_5\Data\liwc_results_all_resumes_1030_files.csv', 
                  header=0, encoding='utf-8')

#join the two files on the "Response_ID", we do an inner join because we only want cases that are in 
#both the survey data and liwc data sets. 
df = pd.merge(df, dft, how='inner', left_on='Response_ID', right_on='Response_ID')

#write the final, analysis ready file to a csv
df1.to_csv("dissertation_complete_847n_dummies_18Jan16a.csv", sep=',', encoding='utf-8', index=False, header=True)


