#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import json 
from tqdm import tqdm
from sklearn.linear_model import LinearRegression
from scipy import spatial
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


# In[2]:


df = pd.read_csv('sector_sampled_data.csv')

f = open('SE_sector_dataset_sentence_embeddings.json')  
input_embeddings = json.load(f)

f = open('SE_sector_keys_sentence_embeddings.json')  
output_embeddings = json.load(f)

sectors = set(df['Sector'])


# In[3]:


def get_data(df):
    x = []
    y = []
    for i in range(len(df)):
        temp = np.array(input_embeddings[str(df['ID'][i])])
        x.append(temp)
        temp = np.array(output_embeddings[df['Sector'][i]])
        y.append(temp)

    x = np.array(x, dtype=np.float32)
    y = np.array(y, dtype=np.float32)
    
    return x, y

def training(x, y):
    model = LinearRegression().fit(x, y)
    return model

def predict(model, x):
    predicted = model.predict(x)
    return predicted

def cosine_simil(y1, y2):
    return 1-spatial.distance.cosine(y1, y2)

def cont_to_dis(y_pred):
    predictions = []
    for i in tqdm(range(len(y_pred))):
        max_cos=0
        max_key = None
        for key in output_embeddings.keys():
            if cosine_simil(y_pred[i],output_embeddings[key]) > max_cos:
                max_cos = cosine_simil(y_pred[i],output_embeddings[key])
                max_key = key
        predictions.append(max_key)

    return predictions

X, y = get_data(df)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

LR = training(X_train,y_train)
y_pred = predict(LR, X_test)
y_true = cont_to_dis(y_test)
regression_predictions = cont_to_dis(y_pred)
accuracy = accuracy_score(y_true, regression_predictions, normalize=True)
print(accuracy)
cm = confusion_matrix(y_true, regression_predictions) 
print(cm)
print(classification_report(y_true, regression_predictions, target_names = ['AGRICULTURE', 'ANIMAL HUSBANDRY', 'HORTICULTURE', 'FISHERIES']))


# In[4]:


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# sphinx_gallery_thumbnail_number = 2

vegetables = ['AGRICULTURE', 'ANIMAL HUSBANDRY', 'HORTICULTURE', 'FISHERIES']
farmers = ['AGRICULTURE', 'ANIMAL HUSBANDRY', 'HORTICULTURE', 'FISHERIES']

harvest = np.zeros(cm.shape)
for i in range(len(cm)):
    harvest[i,:] = cm[i,:]/np.sum(cm[i,:])

harvest = np.around(harvest,2)

fig, ax = plt.subplots()
im = ax.imshow(harvest)

# We want to show all ticks...
ax.set_xticks(np.arange(len(farmers)))
ax.set_yticks(np.arange(len(vegetables)))
# ... and label them with the respective list entries
ax.set_xticklabels(farmers)
ax.set_yticklabels(vegetables)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")

ax.set_title("SE Sector Regression using Classification as Regression technique")
fig.tight_layout()
plt.savefig("SE Sector Regression using Classification as Regression technique.jpg")
plt.show()


# In[ ]:




