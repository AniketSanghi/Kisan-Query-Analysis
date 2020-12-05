#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm


# In[2]:


df = pd.read_csv('Data.csv')

df2 = df[pd.notna(df['Sector'])]
df2 = df2[pd.notna(df2['Query Type'])]

df = df2
df = df.reset_index(drop=True)


# In[3]:


# Plant Protection + Nutrient Management + Disease Management
# Weather + Sowing Time and Weather
# Government Schemes
# Cultural Practices
# Fertilizer Use and Availability
# Agriculture Mechanization
# Seeds and Planting Material + Seeds
# Weed Management
# Credit
# Fishery Nutrition

# Final Query_Type dictionary
Dict = {}
Dict['Nutrient Management'] = 'Plant Protection'
Dict['Plant Protection'] = 'Plant Protection'
Dict['Disease Management'] = 'Plant Protection'
Dict['Sowing Time and Weather'] = 'Weather'
Dict['Government Schemes'] = 'Government Schemes'
Dict['Cultural Practices'] = 'Cultural Practices'
Dict['Fertilizer Use and Availability'] = 'Fertilizer Use and Availability'
Dict['Cultural Practices'] = 'Cultural Practices'
Dict['Agriculture Mechanization'] = 'Agriculture Mechanization'
Dict['Seeds and Planting Material'] = 'Seeds'
Dict['Seeds'] = 'Seeds'
Dict['Weed Management'] = 'Weed Management'
Dict['Credit']='Credit'
Dict['Fishery Nutrition']='Fishery Nutrition'


# In[4]:


sampled_df = df[df['Query Type']=='Fishery Nutrition']
for qt in Dict.keys():
    if qt == 'Fishery Nutrition':
        continue
    df1 = df[df['Query Type']==qt]
#     print(qt, len(df1))
    df1 = df1.sample(frac=1)
    sampled_df = sampled_df.append(df1[:1000])
    
sampled_df = sampled_df.reset_index(drop=True)
    
for i in range(len(sampled_df)):
    sampled_df['Query Type'][i] = Dict[sampled_df['Query Type'][i]]
    
sampled_df.to_csv('final_sampled_data.csv',index=False)


# In[5]:


sampled_df = df[df['Sector']=='FISHERIES']
for qt in set(df['Sector']):
    if qt == 'FISHERIES':
        continue
    df1 = df[df['Sector']==qt]
#     print(qt, len(df1))
    df1 = df1.sample(frac=1)
    sampled_df = sampled_df.append(df1[:2500])
sampled_df.to_csv('sector_sampled_data.csv',index=False)

