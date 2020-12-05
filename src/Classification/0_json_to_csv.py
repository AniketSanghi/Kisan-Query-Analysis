#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import pandas as pd

# Loading Embeddings
# Opening JSON file 
f = open('../data/data.json', encoding="utf8") 
  
# returns JSON object as a dictionary 
kcc_data = json.load(f) 

unique_queries = {}
for year, months in kcc_data.items():
    for month, states in months.items():
        for state, districts in states.items():
            for district, data_list in districts.items():
                for elem in data_list:
                    sector = elem[0]
                    category = elem[1]
                    crop = elem[2]
                    query_type = elem[3]
                    query = elem[4]

                    if query not in unique_queries.keys():
                        unique_queries[query] = [sector, query_type]
                        
i=1
query_list = []
for q in unique_queries.keys():
    query_list.append([i,q,unique_queries[q][0],unique_queries[q][1]])
    i+=1
    
df = pd.DataFrame(query_list)
df.columns =['ID','Query','Sector','Query Type']
df.to_csv('Data.csv',index=False)

