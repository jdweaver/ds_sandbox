# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 17:04:56 2015

@author: joshuaw
"""

import json
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.set(style="white")
with open('C:/Users/Joshuaw/Documents/GA_Data_Science/data/yelp.json', 'rU') as f:
    data = [json.loads(row) for row in f]


# convert the list of dictionaries to a DataFrame
#note that the cool, funny, and useful vote types were in a nested dictionary: u'votes': {u'cool': 2, u'funny': 0, u'useful': 5}
yelp = pd.DataFrame(data)
yelp.head(2)    
    
# add DataFrame columns for cool, useful, and funny, do this by creating a new column for each column
#use list comprehension to pass the nested structure, remember it's as rows, e.g. row['votes]['cool] 
yelp['cool'] = [row['votes']['cool'] for row in data]
yelp['useful'] = [row['votes']['useful'] for row in data]
yelp['funny'] = [row['votes']['funny'] for row in data]


# drop the votes column
#since votes was a nested data type votes:cool, votes:funny, votes:useful, the votes column has all types of vote data
#making the data not so useful so drop it, remember axis=1 indicates that we want to drop a particular column, we would use 
#axis=0 to drop a specific row
yelp.drop('votes', axis=1, inplace=True)
yelp.head(1)


# treat stars as a categorical variable and look for differences between groups
yelp.groupby('stars').mean()

#create correlation matrix 
corr = yelp.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 8))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3,
            square=True, linewidths=.5, 
            cbar_kws={"shrink": .5})
            
#visualize single regression formulas for each potential feature 
sns.set(style="white")
sns.pairplot(yelp, x_vars=['cool', 'useful', 'funny'], y_vars='stars', size=6, aspect=0.7, kind='reg', markers = '+')

#create independent and dependent variables, IV in this case is a list of IVs
feature_cols = ['cool', 'useful', 'funny']
x = yelp[feature_cols]
y = yelp.stars

drinks.drop(['mL', 'servings'], axis=1, inplace=True)   # drop multiple columns


yelp_analyze = yelp.drop(['business_id', 'text', 'date', 'type', 'review_id', 'user_id'], axis=1)

#instantiate the linear regression model
from sklearn.linear_model import LinearRegression

#store the regression model function as a variable called 'linreg'
linreg = LinearRegression(fit_intercept=True)

#fit a linear regression model
linreg.fit(x, y)

#find coeffecient of determination aka R2 
#result = 0.044
r2 = linreg.score(x, y, sample_weight=None)

#create a list of lists that shows the independent variables and their coeffecients 
#note: need to see whether this is a b weight or a beta weight and how to look at significance of the coeffecients
coef = zip(feature_cols, linreg.coef_)
print(r2)
print(coef)
print(linreg.intercept_)

#overall votes is a poor predictor of stars, sentiment is likely to be a better predictor
#find stat significance of coeffecients 

from __future__ import print_function
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.sandbox.regression.predstd import wls_prediction_std

model = sm.OLS(x,y)
results = model.fit()
print(results.summary())

#now let's evaluate using the split, test/train method. 
# define a function that accepts a list of features and returns testing RMSE
def train_test_rmse(feature_cols):
    X = yelp[feature_cols]
    y = yelp.stars
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    linreg = LinearRegression()
    linreg.fit(X_train, y_train)
    y_pred = linreg.predict(X_test)
    return np.sqrt(metrics.mean_squared_error(y_test, y_pred))