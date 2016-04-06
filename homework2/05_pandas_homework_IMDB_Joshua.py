# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:57:27 2015

@author: joshuaw
"""
'''
Pandas Homework with IMDb data
'''
'''
BASIC LEVEL
'''

import pandas as pd
import matplotlib.pyplot as plt

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
col_headers = ["star_rating", "title", "content_rating", "genre", "duration", "actors_list"]
imdb = pd.read_csv("C:/Users/Joshuaw/Documents/GA_Data_Science/data/imdb_1000.csv", sep = ",", header = None, names=col_headers)
imdb.head()
imdb.shape
imdb.index

#drop first row, axis=0 for rows, 1 for columns
imdb.drop(0)                             

#create var for quick view of column headers 
imdb_columns = imdb.columns

# check the number of rows and columns
imdb.shape

# check the data type of each column
imdb.dtypes

# calculate the average movie duration
imdb["duration"] = pd.to_numeric(imdb.duration, errors="coerce") #convert the "duration" column to a numeric column, and coerce into numbers but setting errors = 'coerce'
imdb["star_rating"] = pd.to_numeric(imdb.star_rating, errors="coerce") #convert the "duration" column to a numeric column, and coerce into numbers but setting errors = 'coerce'

imdb.duration.mean()
imdb.duration.mean()

# sort the DataFrame by duration to find the shortest and longest movies
imdb.duration.max()
imdb.duration.min()

imdb.sort('duration').head(1)
imdb.sort('duration').tail(1)

# create a histogram of duration, choosing an "appropriate" number of bins
plt.style.use('bmh') #set plot style
plt.rcParams['figure.figsize'] = (10, 8) # increase default figure and font sizes for easier viewing
plt.rcParams['font.size'] = 14 # increase default figure and font sizes for easier viewing

imdb.duration.hist() #generic histogram of movie duration 
#imdb.groupby("genre").star_rating.plot(kind="hist") #overlay

# use a box plot to display that same data
imdb.boxplot(column="duration")

'''
INTERMEDIATE LEVEL
'''
# count how many movies have each of the content ratings

imdb.content_rating.value_counts()

# use a visualization to display that same data, including a title and x and y labels
imdb.content_rating.value_counts().plot(kind="bar", title = "Number of Movies in Each Rating Category")
plt.xlabel("Rating Categories")
plt.ylabel("Number of Movies")


#I tried the code below but it gave  me a kind of line graph: #imdb.groupby("content_rating").plot(kind='bar',title = "Number of Movies in Each Rating Category")

#i also followed this code from class: drinks.groupby('continent').mean().drop('liters', axis=1).plot(kind='bar', title = "Average Alcohol Consumption Type by Continent")
#but got an error: "Cannot access callable attribute 'drop' of 'DataFrameGroupBy' objects, try using the 'apply' method" 
#code:imdb.groupby("content_rating").drop("star_ratings", axis=1).plot(kind='bar',title = "Number of Movies in Each Rating Category")

# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP

imdb.content_rating.replace(["NOT RATED", "APPROVED", "PASSED", "GP"], "UNRATED", inplace=True)

imdb["content_rating"]

# convert the following content ratings to "NC-17": X, TV-MA
imdb.content_rating.replace(["X", "TV-MA"], "NC-17", inplace=True)

# count the number of missing values in each column
imdb.isnull().sum()

# if there are missing values: examine them, then fill them in with "reasonable" values
imdb.content_rating.fillna(value="NOT YET RATED", inplace=True)
#I think this would fill an integer value with the mean of that column////
imdb.duration.fillna(imdb.duration.mean(), inplace=True)


# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours
rating_more_than2Hours = imdb[imdb.duration >= 120].star_rating.mean()
rating_less_than2Hours = imdb[imdb.duration < 120].star_rating.mean()
from scipy.stats import ttest_ind
ttest_ind(imdb[imdb.duration < 120].star_rating, imdb[imdb.duration < 120].star_rating)

# use a visualization to detect whether there is a relationship between duration and star rating
imdb.plot(kind="scatter", x="duration", y="star_rating")
imdb["duration"].corr(imdb["star_rating"], method = "pearson") #running a correlation shows there is a correlation but low
from scipy.stats import pearsonr #import pearsonr from scipy.stats 
imdb_clean = imdb.dropna() #drop null values and create a new dataframe 
pearsonr(imdb_clean["duration"], imdb_clean["star_rating"]) #run pearsonr to see correlation and significance

# calculate the average duration for each genre
imdb.groupby("genre").duration.mean()

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration
imdb.groupby('content_rating').mean().drop(['star_rating', 'content_rating_num'], axis=1).plot(kind='bar', sharex=True, title = "Movie Duration by Rating Categories")
plt.xlabel("Rating Categories")
plt.ylabel("Movie Length in Minutes")

# determine the top rated movie (by star rating) for each genre
imdb.sort("star_rating", ascending=False) #sort by top star rating
imdb.groupby("genre").title.first() #group by genere and then find the first title in the genre

# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates
#imdb.duplicated(["title"]).sum()
imdb[imdb.title.duplicated()].title
dupe_title = imdb[imdb.title.duplicated()].title
imdb[imdb.title.isin(dupe_title)]

no duplicates, different versions of the movie


# calculate the average star rating for each genre, but only include genres with at least 10 movies
imdb[imdb.genre >= 120].star_rating.mean()

# option 3: calculate the average star rating for all genres, then filter using a boolean Series
imdb.groupby("genre").star_rating.mean()[imdb.genre.value_counts() >= 10]

'''
BONUS
'''

# Figure out something "interesting" using the actors data!
