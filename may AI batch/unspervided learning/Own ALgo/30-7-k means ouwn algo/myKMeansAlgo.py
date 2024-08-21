# 1) Desidde N-cluster
# 2) Init Centriods
# 3) Assign Cluster
# 4) Move Centroid
# 5) Finish

import random
import numpy as np

class MyKMeansAlg:
    def __init__(self, n_cluster = 2, max_ittrations = 100):
        self.n_cluster = n_cluster
        self.max_iter = max_ittrations
        self.centroids = None

    def fit_predict(self, x):
        # Init Centriods
        random_index = random.sample(range(x.shape[0]), self.n_cluster)

        self.centroids = x[random_index]
        # 3) Assign Cluster
      
        cluser_group = self.assign_cluster(x)

        return cluser_group, self.centroids
    
    def assign_cluster(self, x):
        distances = []
        cluster_group = []

        for i in x:
            for centroid in self.centroids:
                    distances.append(np.sqrt(np.dot(i - centroid, i - centroid)))

            print(distances, "xXXXXXXXX")
            
            min_distance = min(distances)
            cluster_group.append(distances.index(min_distance))
            distances.clear()
        return np.array(cluster_group)


