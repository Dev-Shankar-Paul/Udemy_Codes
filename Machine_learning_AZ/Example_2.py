# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:57:56 2020

@author: Dev Shankar Paul
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv('Salary_Data.csv')
X=dataset.iloc[:, :-1].values
Y=dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=1/3,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)

y_pred=regressor.predict(X_test)
y_train_pred=regressor.predict(X_train)

plt.scatter(X_train,Y_train,color='red')
plt.plot(X_train,y_train_pred,color='blue')
plt.title('Salary vs Experience [Training Set]')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(X_test,Y_test,color='red')
plt.plot(X_train,y_train_pred,color='blue')
plt.title('Salary vs Experience [Test Set]')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
