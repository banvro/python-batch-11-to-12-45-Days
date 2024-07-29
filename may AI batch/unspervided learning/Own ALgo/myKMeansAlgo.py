# 1) Desidde N-cluster
# 2) Init Centriods
# 3) Assign Cluster
# 4) Move Centroid
# 5) Finish

import random

class MyKMeansAlg:
    def __init__(self, n_cluster = 2, max_ittrations = 100):
        self.n_cluster = n_cluster
        self.max_iter = max_ittrations
        self.centroids = None

    def fit_predict(self, x):
        # Init Centriods
        random_index = random.sample(range(x.shape[0]), self.n_cluster)

        self.centroids = x[random_index]

        # print(self.centroids)
        return self.centroids
    
    