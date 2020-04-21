#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 22:07:31 2020

@author: dsp
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv('Mall_Customers.csv')
X=dataset.iloc[:,[3,4]].values

#Y is not required since we don't know what to look for or predict

#Using The elbow method 

from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i, init='k-means++', max_iter=300, 
                  n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11),wcss)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#Applying Kmeans to our dataset
kmeans=KMeans(n_clusters=5,init='k-means++',random_state=0)
ykmeans=kmeans.fit_predict(X)

#visualizing the clusters
plt.scatter(X[ykmeans==0,0],X[ykmeans==0,1],s=100,c='red',
            label='Careful')
plt.scatter(X[ykmeans==1,0],X[ykmeans==1,1],s=100,c='blue',
            label='standard')
plt.scatter(X[ykmeans==2,0],X[ykmeans==2,1],s=100,c='green',
            label='target')
plt.scatter(X[ykmeans==3,0],X[ykmeans==3,1],s=100,c='cyan',
            label='careless')
plt.scatter(X[ykmeans==4,0],X[ykmeans==4,1],s=100,c='magenta',
            label='sensible')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1]
            ,s=300,c='yellow', label='Centroids')
plt.title('Clusters of clients')
plt.xlabel('Annual income')
plt.ylabel('Spending score')
plt.legend()
plt.show()
