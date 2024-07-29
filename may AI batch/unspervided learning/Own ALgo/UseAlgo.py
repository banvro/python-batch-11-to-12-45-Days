import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from myKMeansAlgo import MyKMeansAlg

cluster_centriods = [(-5, 5), (5, 5)]
cluster_stdd = [1, 1]

x, y = make_blobs(n_samples = 100, centers = cluster_centriods, cluster_std = cluster_stdd, n_features = 2, random_state =  2)


kmeans = MyKMeansAlg()

centroids = kmeans.fit_predict(x)


# print(x)
# print(x.shape)

plt.scatter(x[:, 0], x[:, 1], label = "Data Points")
plt.scatter(centroids[:, 0], centroids[:, 1], color = "red", label = "Centriods")
plt.show()
plt.legend()