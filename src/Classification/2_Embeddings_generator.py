#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
from torch.autograd import Variable
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
import csv
import json 
from tqdm import tqdm


# In[2]:


torch.backends.cudnn.deterministic = True
torch.manual_seed(123)
torch.cuda.manual_seed_all(123)
np.random.seed(123)
torch.cuda.manual_seed_all(123)


# In[3]:


from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
# Load pre-trained model (weights)
model = BertModel.from_pretrained('bert-base-uncased',
                                  output_hidden_states = True, # Whether the model returns all hidden-states.
                                  )

# Put the model in "evaluation" mode, meaning feed-forward operation.
model.eval()


# In[4]:


df = pd.read_csv('final_sampled_data.csv')
Embed = {}

for i in tqdm(range(len(df))):
# for i in range(1):
    df['Query'][i] = "[CLS] " + df['Query'][i] + " [SEP]"
    tokenized_text = tokenizer.tokenize(df['Query'][i])
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    segments_ids = [1] * len(tokenized_text)

    indices = np.arange(1,len(tokenized_text)-1)
    tokens_tensor = torch.tensor([indexed_tokens])
    segments_tensors = torch.tensor([segments_ids])
    
    with torch.no_grad():
        outputs = model(tokens_tensor, segments_tensors)
        hidden_states = outputs[0]
        
    token_embeddings = torch.squeeze(hidden_states, dim=0)
    
    embedding = np.zeros(token_embeddings[0].numpy().shape, dtype = np.float32)
    if len(indices) > 0:
        for j in indices:
            embedding += token_embeddings[j].numpy()
        embedding = embedding/len(indices)
    Embed[df['ID'][i]] = embedding.tolist()

Embed2 = {}
for key in Embed.keys():
    Embed2[int(key)]=Embed[key]

with open("final_querytype_dataset_sentence_embeddings.json", "w") as outfile:  
    json.dump(Embed2, outfile, indent = 4) 


# In[5]:


query_types = set(df['Query Type'])

Embed = {}

for key in query_types:
    temp = "[CLS] " + key + " [SEP]"
    tokenized_text = tokenizer.tokenize(temp)
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    segments_ids = [1] * len(tokenized_text)

    indices = np.arange(1,len(tokenized_text)-1)
    tokens_tensor = torch.tensor([indexed_tokens])
    segments_tensors = torch.tensor([segments_ids])
    
    with torch.no_grad():
        outputs = model(tokens_tensor, segments_tensors)
        hidden_states = outputs[0]
        
    token_embeddings = torch.squeeze(hidden_states, dim=0)
    
    embedding = np.zeros(token_embeddings[0].numpy().shape, dtype = np.float32)
    if len(indices) > 0:
        for j in indices:
            embedding += token_embeddings[j].numpy()
        embedding = embedding/len(indices)
    Embed[key] = embedding.tolist()

with open("querytype_keys_sentence_embeddings.json", "w") as outfile:  
    json.dump(Embed, outfile, indent = 4) 


# In[6]:


df = pd.read_csv('sector_sampled_data.csv')

Embed = {}

for i in tqdm(range(len(df))):
# for i in range(1):
    df['Query'][i] = "[CLS] " + df['Query'][i] + " [SEP]"
    tokenized_text = tokenizer.tokenize(df['Query'][i])
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    segments_ids = [1] * len(tokenized_text)

    indices = np.arange(1,len(tokenized_text)-1)
    tokens_tensor = torch.tensor([indexed_tokens])
    segments_tensors = torch.tensor([segments_ids])
    
    with torch.no_grad():
        outputs = model(tokens_tensor, segments_tensors)
        hidden_states = outputs[0]
        
    token_embeddings = torch.squeeze(hidden_states, dim=0)
    
    embedding = np.zeros(token_embeddings[0].numpy().shape, dtype = np.float32)
    if len(indices) > 0:
        for j in indices:
            embedding += token_embeddings[j].numpy()
        embedding = embedding/len(indices)
    Embed[df['ID'][i]] = embedding.tolist()
    
Embed2 = {}
for key in Embed.keys():
    Embed2[int(key)]=Embed[key]
    
with open("final_sector_dataset_sentence_embeddings.json", "w") as outfile:  
    json.dump(Embed2, outfile, indent = 4)


# In[7]:


Embed = {}
sectors = set(df['Sector'])

for key in sectors:
    temp = "[CLS] " + key + " [SEP]"
    tokenized_text = tokenizer.tokenize(temp)
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    segments_ids = [1] * len(tokenized_text)

    indices = np.arange(1,len(tokenized_text)-1)
    tokens_tensor = torch.tensor([indexed_tokens])
    segments_tensors = torch.tensor([segments_ids])
    
    with torch.no_grad():
        outputs = model(tokens_tensor, segments_tensors)
        hidden_states = outputs[0]
        
    token_embeddings = torch.squeeze(hidden_states, dim=0)
    
    embedding = np.zeros(token_embeddings[0].numpy().shape, dtype = np.float32)
    if len(indices) > 0:
        for j in indices:
            embedding += token_embeddings[j].numpy()
        embedding = embedding/len(indices)
    Embed[key] = embedding.tolist()
    
with open("sector_keys_sentence_embeddings.json", "w") as outfile:  
    json.dump(Embed, outfile, indent = 4) 


# In[ ]:




