#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
import random
import csv
import json 
from tqdm import tqdm


# In[ ]:


from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('xlm-r-bert-base-nli-stsb-mean-tokens')


# In[14]:


df = pd.read_csv('final_sampled_data.csv')
Embed = {}

corpus_sentences = df['Query'].tolist()
corpus_embeddings = model.encode(corpus_sentences, show_progress_bar=True, convert_to_numpy=True)
for i in range(len(df)):
    Embed[df['ID'][i]]=corpus_embeddings[i].tolist()

Embed2 = {}
for key in Embed.keys():
    Embed2[int(key)]=Embed[key]


with open("SE_querytype_dataset_sentence_embeddings.json", "w") as outfile:  
    json.dump(Embed2, outfile, indent = 4) 


# In[15]:


corpus_sentences = list(set(df['Query Type']))

Embed = {}

corpus_embeddings = model.encode(corpus_sentences, show_progress_bar=True, convert_to_numpy=True)
for i in range(len(corpus_sentences)):
    Embed[corpus_sentences[i]]=corpus_embeddings[i].tolist()

with open("SE_querytype_keys_sentence_embeddings.json", "w") as outfile:  
    json.dump(Embed, outfile, indent = 4) 


# In[ ]:


df = pd.read_csv('sector_sampled_data.csv')
Embed = {}

corpus_sentences = df['Query'].tolist()
corpus_embeddings = model.encode(corpus_sentences, show_progress_bar=True, convert_to_numpy=True)

for i in range(len(df)):
    Embed[df['ID'][i]]=corpus_embeddings[i].tolist()

Embed2 = {}
for key in Embed.keys():
    Embed2[int(key)]=Embed[key]


with open("SE_sector_dataset_sentence_embeddings.json", "w") as outfile:  
    json.dump(Embed2, outfile, indent = 4) 


# In[ ]:


corpus_sentences = list(set(df['Sector']))

Embed = {}

corpus_embeddings = model.encode(corpus_sentences, show_progress_bar=True, convert_to_numpy=True)
for i in range(len(corpus_sentences)):
    Embed[corpus_sentences[i]]=corpus_embeddings[i].tolist()

with open("SE_sector_keys_sentence_embeddings.json", "w") as outfile:  
    json.dump(Embed, outfile, indent = 4) 


# In[ ]:




