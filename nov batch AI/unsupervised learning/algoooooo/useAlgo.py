from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from createAlgo import OwnKMeansAlgo

clustter_center = [(-5, -5), (5, 5)]

std = (2, 2)

x, y = make_blobs(n_samples = 100, n_features = 2, cluster_std = std, centers = clustter_center)


obj = OwnKMeansAlgo()
centriods, clutsers = obj.fit_predict(x)


plt.scatter(x[:, 0], x[:, 1])
plt.scatter(centriods[0][0], centriods[0][1], marker = "o", s = 10)
plt.scatter(centriods[1][0], centriods[1][1], marker = "o", s = 10)
plt.show()
