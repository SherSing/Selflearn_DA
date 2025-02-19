# Hierarchical Clustering
# https://www.kaggle.com/code/heeraldedhia/hierarchical-clustering-for-customer-data

 
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import pandas as pd

df = pd.read_csv('./Raw Data/Mall_Customers.csv')
# print(df.head())
print(df.describe())

# Gender_map = df['Gender'].map({'Male': 0, 'Female': 1})

# data = list(zip(df['Age'], df['Annual Income (k$)']))   
# # print(data)



# # linkage_data = linkage(data, method='ward', metric='euclidean')
# # dendrogram(linkage_data, orientation='right',truncate_mode='lastp')
# # plt.show()

# hierarchical_cluster = AgglomerativeClustering(n_clusters=3, metric="euclidean", linkage="ward")

# labels = hierarchical_cluster.fit_predict(data)

# plt.scatter(df['Age'], df['Annual Income (k$)'], c=labels)
# plt.show()