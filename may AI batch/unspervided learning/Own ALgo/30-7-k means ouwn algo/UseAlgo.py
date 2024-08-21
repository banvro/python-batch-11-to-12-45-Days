import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from myKMeansAlgo import MyKMeansAlg

cluster_centriods = [(-5, 5), (5, 5)]
cluster_stdd = [1, 1]

x, y = make_blobs(n_samples = 100, centers = cluster_centriods, cluster_std = cluster_stdd, n_features = 2, random_state =  2)


kmeans = MyKMeansAlg()

cluser_group, centriod = kmeans.fit_predict(x)

print(centriod)
# print(cluser_group)
# print(x[cluser_group == 0, 0])

# print(cluser_group)

plt.scatter(x[cluser_group == 0, 0], x[cluser_group == 0, 1], color = "red", label = "0th Cluster")
plt.scatter(x[cluser_group == 1, 0], x[cluser_group == 1, 1], color = "green", label = "1th Cluster")
plt.scatter(centriod[0][0], centriod[0][1], color = "black", label = "1st centriod")
plt.scatter(centriod[1][0], centriod[1][1], color = "blue", label = "2th centriod")

plt.show()
plt.legend()


