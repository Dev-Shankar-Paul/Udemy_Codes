# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:50:22 2020

@author: Dev Shankar Paul
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy

dataset=pd.read_csv('50_Startups.csv')
X=dataset.iloc[:, :-1].values
Y=dataset.iloc[:, 4].values

"""from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_X=LabelEncoder()
X[:,3]=labelencoder_X.fit_transform(X[:, 3])
ct=ColumnTransformer([('onehotencoder',OneHotEncoder(categories='auto'),[0,1,2])],
                     remainder='passthrough')
#onehotencoder=OneHotEncoder(categories=[3])
X=ct.fit_transform(X)
"""
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
labelencoder_X=LabelEncoder()
X[:,3]=labelencoder_X.fit_transform(X[:,3])
onehotencoder=OneHotEncoder(categorical_features=[3])
X=onehotencoder.fit_transform(X).toarray()

X=X[:, 1:]   #avoiding dummy variable trap (chucking the 0th column)

#X=scipy.sparse.csr_matrix.toarray(X)
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)

Y_pred=regressor.predict(X_test)
#X=scipy.sparse.csr_matrix.toarray(X)

import statsmodels.api as sm
sl=0.05
X = np.append(arr=np.ones((50,1)).astype(int),values=X,axis=1)
column_index=[0,1,2,3,4,5]
X_OPT=X[:,column_index]
regressor_OLS=sm.OLS(endog=Y,exog=X_OPT).fit()
regressor_OLS.summary()
               
while(np.amax(regressor_OLS.pvalues)>sl):
    index_to_remove=int(np.where(regressor_OLS.pvalues==np.amax(regressor_OLS.pvalues))[0])
    print(index_to_remove)
    column_index.pop(index_to_remove)
    X_OPT=X[:,column_index]
    regressor_OLS=sm.OLS(endog=Y,exog=X_OPT).fit()
    regressor_OLS.summary()
    print('deleted an element')

print('model is ready')
print(X_OPT)

from sklearn.linear_model import LinearRegression
newregressor=LinearRegression()
newregressor.fit(np.reshape(X_train[:,3],(-1,1)),Y_train)

Y_newpred=newregressor.predict(np.reshape(X_test[:,3],(-1,1)))
   