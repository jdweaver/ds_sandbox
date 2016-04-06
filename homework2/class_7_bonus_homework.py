# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 18:52:10 2015

@author: joshuaw
"""
'''
OPTIONAL WEB SCRAPING HOMEWORK

First, define a function that accepts an IMDb ID and returns a dictionary of
movie information: title, star_rating, description, content_rating, duration.
The function should gather this information by scraping the IMDb website, not
by calling the OMDb API. (This is really just a wrapper of the web scraping
code we wrote above.)

For example, get_movie_info('tt0111161') should return:

{'content_rating': 'R',
 'description': u'Two imprisoned men bond over a number of years...',
 'duration': 142,
 'star_rating': 9.3,
 'title': u'The Shawshank Redemption'}

Then, open the file imdb_ids.txt using Python, and write a for loop that builds
a list in which each element is a dictionary of movie information.
use imdb_ids.txt to build a dataframe that contains the information information defined by the function above

Finally, convert that list into a DataFrame.
'''

# define a function that accepts an IMDb ID and returns a dictionary of movie information
import requests
from bs4 import BeautifulSoup # convert HTML into a structured Soup object

def movie_info(movie_id):
    r = requests.get("http://www.imdb.com/title/" + movie_id)
    html = BeautifulSoup(r.text)
    info = {}
    info["title"] = html.find(name='span', attrs={'class':'itemprop', 'itemprop':'name'}).text #title
    info["rating"] = html.find_all(name='span', attrs={'itemprop':'contentRating'})[0].text.strip() #content rating
    info["duration"] = int(html.find_all(name='time', attrs={'itemprop':'duration'})[0].text.strip().split()[0]) #duration
    info["description"] = html.find(attrs={'itemprop':'description'}).text.strip() #description 
    info["star_rating"] = float(html.find(name='span', attrs={'itemprop':'ratingValue'}).text) #star rating  
    return info

# test the function
movie_info("tt0111161")

# open the file of IDs (one ID per row), and store the IDs in a list
with open('imdb_ids.txt', 'rU') as f: 
    f = f.read().strip()
movie_id_list = f.split("\n")

# get the information for each movie, and store the results in a list
from time import sleep
movie_list = [] 
for movie in movie_id_list:    
    movie_list.append(movie_info(movie))
    sleep(0.5)

# check that the list of IDs and list of movies are the same length
#blank response means that they are the same length
assert(len(movie_id_list) == len(movie_list))

# convert the list of movies into a DataFrame
import pandas as pd 
movie_df = pd.DataFrame(movie_list, index=movie_id_list)