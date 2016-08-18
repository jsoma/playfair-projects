
# coding: utf-8

# # Scraping Lundberg

# In[526]:

import requests
from bs4 import BeautifulSoup
import re

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


# # Prepping beautifulsoup

# In[527]:

from bs4 import BeautifulSoup
soup = BeautifulSoup(open("/Users/barneyjs/Desktop/Transparenz.htm"), 'html.parser')


# In[528]:

#odd numbers for names and adresses
odd = soup.find_all('div', {'class': 'row odd first clearfix'})
len(odd)


# In[529]:

#odd numbers for names and adresses
even = soup.find_all('div', {'class': 'row even first clearfix'})
len(even)


# In[530]:

#Fees
details = soup.find_all('div', {'class': 'row-details clearfix'})
len(details)


# In[531]:

#Together they add up to 191, from 96 and 95. So that makes 191. 
#My plan is to iterate through both the odd and the even list.
#Then zip join them together. And finally join them to the list of 
#fees.


# In[532]:

def names(x):
    if x.find('div', {'class': 'hcptitle'}) is not None:
        return 'Doctor, ' + x.find('div', {'class': 'hcptitle'}).nextSibling.strip()
    else:
        return 'Hospital, ' + x.find('div', {'class': 'col hcohcpname'}).string.strip()


# In[533]:

def address_(x):
    try:
        return x.find('div', {'class': 'col address'}).string  
    except:
        return None


# ## First the names

# In[534]:

#Getting odd names
oddnamelist = []
for item in odd:
    name = names(item)
    oddnamelist.append(name)


# In[535]:

#Getting the even names
evennamelist = []
for item in even:
    name = names(item)
    evennamelist.append(name)


# In[536]:

#Making sure the lists are the same length, and getting the last one, 
#if they're not.
if len(oddnamelist) > len(evennamelist):
    last_odd = oddnamelist.pop()
else:
    last_odd = ''
print(last_odd)


# In[537]:

#Creating whole list of names
wholenamelist = []
for x in zip(oddnamelist,evennamelist):
    wholenamelist.append(x[0])
    wholenamelist.append(x[1])

#Adding on last element of the list, if odd was longer
wholenamelist.append(last_odd)
len(wholenamelist)


# ## Now the Addresses

# In[538]:

#Getting the odd addresslist
oddaddresslist = []
for item in odd:
    address = address_(item)
    oddaddresslist.append(address)
len(oddaddresslist)


# In[539]:

#Getting the even addresslist
evenaddresslist = []
for item in even:
    address = address_(item)
    evenaddresslist.append(address)
len(evenaddresslist)


# In[540]:

if len(oddaddresslist) > len(evenaddresslist):
    last_odd = oddaddresslist.pop()
else:
    last_odd = ''


# In[541]:

#Creating whole list of addresses:
addresslist = []
for x in zip(oddaddresslist,evenaddresslist):
    addresslist.append(x[0])
    addresslist.append(x[1])

#Adding on last element of the list, if odd was longer
addresslist.append(last_odd)
len(addresslist)


# # Now the fees

# In[597]:

#Data prep and unctions 
#Prepping the data to get a list of all the Fees. This step may not be necessary.
Fees = []
Registration = []
for x in details:
    x = x.find('div', {'class': 'col meta'})
    Fees.append(x)

def donations(y):
    try: 
        return int(y.find('span', text = re.compile('Donations')).next_sibling.string.strip().replace(" CHF", ""))
    except:
        None
        return 0
    
def sponsorships(y):
    try:
        return int(y.find('span', text = re.compile('Sponsorship agreement with HCPs')).next_sibling.string.strip().replace(" CHF", ""))
    except:
        None
        return 0

def reg_fees(y):
    try:
        return int(y.find('span', text = re.compile('Registration Fees')).next_sibling.string.strip().replace(" CHF", ""))
    except:
        None
        return 0

def accomodations(y):
    try:
        return int(y.find('span', text = re.compile('Accommodations')).next_sibling.string.strip().replace(" CHF", ""))
    except:
        None
        return 0
    
def fees(y):
    try:
        return int(y.find('span', text = re.compile('Fees')).next_sibling.string.strip().replace(" CHF", ""))
    except:
        None 
        return 0
    
def consultancy(y):
    try: 
        return int(y.find('span', text = re.compile('Related')).next_sibling.string.strip().replace(" CHF", ""))
    except:
        None 
        return 0


# In[598]:

Fees


# In[599]:

#Now making the 6 lists

DONATIONS_AND_GRANTS = []
SPONSORSHIPS = []
REG_FEES = []
ACCOMODATION = []
FEES = []
CONSULTANCY = []

for item in Fees:
    donation = donations(item)
    sponsorship = sponsorships(item)
    reg_fee = reg_fees(item)
    accomodation = accomodations(item)
    fee = fees(item)
    consultant = consultancy(item)
    DONATIONS_AND_GRANTS.append(donation)
    SPONSORSHIPS.append(sponsorship)
    REG_FEES.append(reg_fee)
    ACCOMODATION.append(accomodation)
    FEES.append(fee)
    CONSULTANCY.append(consultant)
    
len(DONATIONS_AND_GRANTS)
len(SPONSORSHIPS)
len(REG_FEES)
len(ACCOMODATION)
len(FEES)
len(CONSULTANCY)


# # Creating a dictionary with all of my lists
# 
# ## What are my lists again:
# - wholenamelist
# - addresslist
# - DONATIONS_AND_GRANTS
# - SPONSORSHIPS
# - REG_FEES
# - ACCOMODATION
# - FEES
# - CONSULTANCY

# In[600]:

Lundberg = []

for name, address, donation, sponsorship, reg_fee, accomodation, fee, consultant in zip(wholenamelist, addresslist, DONATIONS_AND_GRANTS,        SPONSORSHIPS, REG_FEES, ACCOMODATION, FEES, CONSULTANCY):
    
    Lundberg_dict = {'NAME': name, 
                    'ADDRESS': address,
                    'DONATIONS AND GRANTS': donation,
                    'SPONSORSHIPS': sponsorship,
                    'REGISTRATION FEES': reg_fee,
                    'TRAVEL AND ACCOMMODATION': accomodation,
                    'FEES': fee,
                    'OTHER EXPENSES AND CONSULTANCY': consultant}
    Lundberg.append(Lundberg_dict)


# # Creating the DF

# In[601]:

df = pd.DataFrame(Lundberg)


# In[602]:

df.head(1)


# In[603]:

df['DOC, HOS'], df['FULLNAME'] = zip(*df['NAME'].apply(lambda x: x.split(',', 1)))


# In[604]:

del df['NAME']


# In[605]:

df_doctors = df[df['DOC, HOS'] == 'Doctor']
df_doctors.head(1)


# In[606]:

df_hospitals = df[df['DOC, HOS'] == 'Hospital']
df_hospitals.head(1)


# In[607]:

del df_doctors['DOC, HOS']
del df_hospitals['DOC, HOS']


# In[608]:

df_hospitals.to_csv('Lundberg_hospitals.csv', index=False)
df_doctors.to_csv('Lundberg_docs.csv', index=False)


