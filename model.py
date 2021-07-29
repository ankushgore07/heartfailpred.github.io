# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 19:52:43 2021

@author: Ankush
"""

# heart fail prediction using ML model

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np

#importing dataset

ds= pd.read_csv(r'C:\Users\Ankush\Desktop\heart-pred\heart_failure_clinical_records_dataset.csv')

ds.head()

#shape of Dataset

ds.shape

#as dataset has no null, or missing values
ds.isnull().values.any()

#also there is no need of feature selection, all features are important

#feature selection

X = ds.iloc[:,0:12]
X.head(3)

y= ds.DEATH_EVENT
y.head(3)

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.20,random_state=1)

#model selection

rfc= RandomForestClassifier()

#training the model
rfc.fit(X_train,y_train)

#checking the score
sc=rfc.score(X_train,y_train)
#print('training score',sc)

#testing score
st=rfc.score(X_test,y_test)
#print('testing score',st)

#saving model to disk
pickle.dump(rfc,open('model.pkl','wb'))

#loding model to compare rsult
model=pickle.load(open('model.pkl','rb'))
print(model.predict([[55,0,7861,0,38,0,263358.03,1.1,136,1,0,6]])) 


