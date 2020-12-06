#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('final_sampled_data.csv')
f = open('final_querytype_dataset_sentence_embeddings.json')  
input_embeddings = json.load(f)


# In[3]:


qt_to_id = {}
qt_to_id['Agriculture Mechanization']=0
qt_to_id['Credit']=1
qt_to_id['Cultural Practices']=2
qt_to_id['Fertilizer Use and Availability']=3
qt_to_id['Fishery Nutrition']=4
qt_to_id['Government Schemes']=5
qt_to_id['Plant Protection']=6
qt_to_id['Seeds']=7
qt_to_id['Weather']=8
qt_to_id['Weed Management']=9


# In[4]:


X = []
y = []
for i in range(len(df)):
    X.append(input_embeddings[str(df['ID'][i])])
    y.append(qt_to_id[df['Query Type'][i]])
X = np.array(X)
y = np.array(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0) 
targets = ['Agriculture Mechanization','Credit','Cultural Practices','Fertilizer Use and Availability','Fishery Nutrition','Government Schemes',
 'Plant Protection', 'Seeds', 'Weather', 'Weed Management']


# In[5]:


from sklearn.tree import DecisionTreeClassifier 
dtree_model = DecisionTreeClassifier(max_depth = 18).fit(X_train, y_train)
dtree_predictions = dtree_model.predict(X_test) 
accuracy = accuracy_score(y_test, dtree_predictions, normalize=True)
print(accuracy)
cm = confusion_matrix(y_test, dtree_predictions) 
print(cm)
print(classification_report(y_test, dtree_predictions, target_names = targets))
plot_confusion_matrix(dtree_model, X_test, y_test, normalize='true', display_labels=targets, xticks_rotation = 45)
plt.title('Query Type Classification using Decision Tree')
plt.savefig('Query Type Classification using Decision Tree.jpg')


# In[6]:


from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier(max_depth = 18).fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test) 
accuracy = accuracy_score(y_test, rf_predictions, normalize=True)
print(accuracy)
cm = confusion_matrix(y_test, rf_predictions) 
print(cm)
print(classification_report(y_test, rf_predictions, target_names = targets))
plot_confusion_matrix(rf_model, X_test, y_test, normalize='true',display_labels=targets, xticks_rotation = 45) 
plt.title('Query Type Classification using Random Forest')
plt.savefig('Query Type Classification using Random Forest.jpg')




# In[7]:


# training a linear SVM classifier 
from sklearn.svm import SVC 
svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X_train, y_train) 
svm_predictions = svm_model_linear.predict(X_test) 
  
# model accuracy for X_test   
accuracy = svm_model_linear.score(X_test, y_test) 
print(accuracy)
# creating a confusion matrix 
cm = confusion_matrix(y_test, svm_predictions) 
print(cm)
print(classification_report(y_test, svm_predictions, target_names = targets))
plot_confusion_matrix(svm_model_linear, X_test, y_test, normalize='true',display_labels=targets, xticks_rotation = 45) 
plt.title('Query Type Classification using linear SVM')
plt.savefig('Query Type Classification using linear SVM.jpg')


# In[8]:


# training a KNN classifier 
from sklearn.neighbors import KNeighborsClassifier 
knn = KNeighborsClassifier(n_neighbors = 5).fit(X_train, y_train) 
  
# accuracy on X_test 
accuracy = knn.score(X_test, y_test) 
print(accuracy) 
  
# creating a confusion matrix 
knn_predictions = knn.predict(X_test)  
cm = confusion_matrix(y_test, knn_predictions)
print(cm)
print(classification_report(y_test, knn_predictions, target_names = targets))
plot_confusion_matrix(knn, X_test, y_test, normalize='true',display_labels=targets, xticks_rotation = 45)
plt.title('Query Type Classification using KNN classifier')
plt.savefig('Query Type Classification using KNN classifier.jpg')




# In[9]:


# training a Naive Bayes classifier 
from sklearn.naive_bayes import GaussianNB 
gnb = GaussianNB().fit(X_train, y_train) 
gnb_predictions = gnb.predict(X_test) 
  
# accuracy on X_test
accuracy = gnb.score(X_test, y_test)
print(accuracy)
  
# creating a confusion matrix
cm = confusion_matrix(y_test, gnb_predictions)
print(cm)
print(classification_report(y_test, gnb_predictions, target_names = targets))
plot_confusion_matrix(gnb, X_test, y_test, normalize='true', display_labels=targets, xticks_rotation = 45)
plt.title('Query Type Classification using Naive Bayes classifier')
plt.savefig('Query Type Classification using Naive Bayes classifier.jpg')


# In[10]:


from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(random_state=0).fit(X_train, y_train)
lr_predictions = clf.predict(X_test)

accuracy = accuracy_score(y_test, lr_predictions, normalize=True)
print(accuracy)
cm = confusion_matrix(y_test, lr_predictions) 
print(cm)
print(classification_report(y_test, lr_predictions, target_names = targets))
plot_confusion_matrix(clf, X_test, y_test, normalize='true', display_labels=targets, xticks_rotation = 45) 
plt.title('Query Type Classification using Logistic Regression')
plt.savefig('Query Type Classification using Logistic Regression.jpg')


# In[ ]:




