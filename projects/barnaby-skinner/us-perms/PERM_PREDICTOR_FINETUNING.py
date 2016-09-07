
# coding: utf-8

# # PERM Acceptance Rate Nation by Nation 2009 - 2016
# ## Regardless of their profession or the company they are applying to

# ## CONTENTS:
#
# ### IMPORTING DATA AND PULLING OUT RELEVANT COLUMNS
#
# ### WORKING ON THE PREDICTOR
#
# ### THE PREDICTOR OUTPUT
# - Creating a list for check the users input
#
#

# In[209]:

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import random

import requests
import urllib
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn import tree, metrics
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier

import statsmodels.api as sm
from statsmodels.nonparametric.kde import KDEUnivariate
#from statsmodels.nonparametric import smoothers_lowes

import matplotlib
import matplotlib.pyplot as plt
#get_ipython().magic('matplotlib inline')


# # IMPORTING PREPPED DATA

# In[212]:

df = pd.read_csv('data/prepped_pred_data.csv')


# In[213]:

df = df.dropna()


# # WORKING ON THE PREDICTOR

# In[214]:

#Learning the Employer's name
le_employer_name = preprocessing.LabelEncoder()


# In[215]:

le_employer_name.fit(df['EMPLOYER_NAME'])


# In[216]:

#Encoding the Employer's name
df['EMPLOYER_NAME_label'] = le_employer_name.transform(df['EMPLOYER_NAME'])


# In[217]:

#SOC Code
le_soc_code = preprocessing.LabelEncoder()


# In[218]:

le_soc_code.fit(df['2018 SOC Title'])


# In[219]:

df['SOC_Title_label'] = le_soc_code.transform(df['2018 SOC Title'])


# In[220]:

#COUNTRY_OF_CITZENSHIP
country_of_citizenship = preprocessing.LabelEncoder()


# In[221]:

country_of_citizenship.fit(df['COUNTRY_OF_CITZENSHIP'])


# In[222]:

df['COUNTRY_OF_CITZENSHIP_label'] = country_of_citizenship.transform(df['COUNTRY_OF_CITZENSHIP'])


# In[223]:

#Creating dataframe for the matrix (but will I still be able to transform values back? It seems to work)
df_matrix = df[['ACCEPTED', 'WAGE_OFFER_FROM_9089', 'EMPLOYER_NAME_label', 'SOC_Title_label', 'COUNTRY_OF_CITZENSHIP_label']].copy()


# In[224]:

#Making x and y and selecting the corrent colums
result_array = df_matrix.as_matrix()
x = result_array[:,1:]
y = result_array[:,0]


# In[225]:

#Random Forest is impressively good


# In[226]:

X_train, X_test, y_train, y_test = train_test_split(x, y, stratify=y, test_size=0.20,train_size=0.80)


# In[227]:

forest = RandomForestClassifier(n_estimators=100, random_state=100)
forest.fit(X_train, y_train)
dt = forest.fit(X_train, y_train)


# In[228]:

print("accuracy on training set: %f" % forest.score(X_train, y_train))
print("accuracy on test set: %f" % forest.score(X_test, y_test))


# In[229]:

plt.plot(dt.feature_importances_,'o')
plt.ylim(0,1)


# In[230]:

#Label Encoder Names

#le_employer_name   df['EMPLOYER_NAME_label']
#le_soc_code  df['SOC Title_label']
#country_of_citizenship   df['COUNTRY_OF_CITZENSHIP_label']

#And Wage

#'WAGE_OFFER_FROM_9089'
#'EMPLOYER_NAME_label',
#'EMPLOYER_STATE_label',
#'le_soc_code'
#'COUNTRY_OF_CITZENSHIP_label'


#'WAGE_OFFER_FROM_9089', 'EMPLOYER_NAME_label', 'SOC_Title_label', 'COUNTRY_OF_CITZENSHIP_label'


# In[231]:

INDIA = country_of_citizenship.transform('INDIA')
round(forest.predict_proba([85072.0, 20, 20, INDIA])[0][1], 4)


# # Input for the Predictor Output

# ## General predictor with 4 parameters

# In[232]:

#Country list
country_list = list(set(df['COUNTRY_OF_CITZENSHIP'].tolist()))


# In[233]:

#Employer list
employer_list = list(set(df['EMPLOYER_NAME'].tolist()))


# In[234]:

#occupation_list
occupation_list = list(set(df['2018 SOC Title'].tolist()))


# In[235]:

# "Computer Systems Analysts" is the most common job for foreigners applying for Green Cards. Since 2009
# approximately every fifth Green Card issued was for somebody in one of these two professions. Type "1"
# to pick this profession or, 2 to pick a random profession from 647 professions in the data.
profession_list = list(set(df['2018 SOC Title'].tolist()))


# In[236]:

print("Compare the chances of getting a visa based on data from nearly half a million visa applications since 2009.")
country = input("Which country are you from? Please use all caps. ")
employer = input("Which company is hiring you? Please us all caps. (e.g. MICROSOFT CORPORATION, APPLE INC., BLOOMBERG L.P.) ")
occupation = input("What's your occupation? (e.g. Computer and Mathematical, Architecture and Engineering, Management, Food Preparation and Serving Related ")
wage = input("What's your expected yearly salary? ")


# In[237]:

if country in country_list:
    country_name = country
    country = country_of_citizenship.transform(country)
else:
    print('Please check your spelling or caps for the selected country.')

if employer in employer_list:
    employer_name = employer
    employer = le_employer_name.transform(employer)
else:
    print('Please check your spelling or caps for the selected employer.')

if occupation in occupation_list:
    occupation_name = occupation
    occupation = le_soc_code.transform(occupation)
else:
    print('Please check your spelling or caps for the selected occupation.')

try:
    x = forest.predict_proba([wage, occupation, employer, country])[0][1]
    print("As a citizen from", country_name, "earning $", wage, "a year, working for", employer_name,           "and working in a", occupation_name, "occupation, your chances of getting a Green Card in the US are: {0:.1f}%.".format(x*100))
except:
    'ValueError'


# ## Comparative Predictor
# Input: where you enter Nationality and wage (computer profession, 130'000k a year and as company are given Microsoft are given.

# In[238]:

print("Compare the chances of three different nationalities for a Green Card, would they be hired as software developers earning 130000 USD a year working for Microsoft.")
country1 = input("Pick your first country: ")
country2 = input("Your second one: ")
country3 = input("And your third: ")


# In[242]:

if country1 in country_list:
    country_name1 = country1
    country1 = country_of_citizenship.transform(country1)
else:
    print('Please check your spelling or caps for your first selected country.')

if country2 in country_list:
    country_name2 = country2
    country2 = country_of_citizenship.transform(country2)
else:
    print('Please check your spelling or caps for your second selected country.')

if country3 in country_list:
    country_name3 = country3
    country3 = country_of_citizenship.transform(country3)
else:
    print('Please check your spelling or caps for your third selected country.')

try:
    x1 = forest.predict_proba([130000, 5, 3778, country1])[0][1]
    x2 = forest.predict_proba([130000, 5, 3778, country2])[0][1]
    x3 = forest.predict_proba([100000, 5, 3778, country3])[0][1]
    print(country_name1, ": {0:.1f}%.".format(x1*100))
    print(country_name2, ": {0:.1f}%.".format(x2*100))
    print(country_name3, ": {0:.1f}%.".format(x2*100))
except:
    'ValueError'



# In[ ]:

#Saving a model in Pickle
#http://scikit-learn.org/stable/modules/model_persistence.html


# In[ ]:

#import pickle
#s = pickle.dumps(clf)
#clf2 = pickle.loads(s)


# In[243]:

import pickle


# In[244]:

import pickle

classifier = RandomForestClassifier(n_estimators=100, random_state=100)
output = open('classifier.pkl', 'wb')
pickle.dump(classifier, output)
output.close()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:

#Using PIckle
#https://pythontips.com/2013/08/02/what-is-pickle-in-python/
