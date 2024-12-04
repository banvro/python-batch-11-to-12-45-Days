# 1) Decide n cluster
# 2) init centriods
# 3) assign clusters
# 4) movie centriods
# 5) Finish
import random
import numpy as np

class OwnKMeansAlgo:
    def __init__(self, n_cluster = 2, max_ittractions = 100):
        self.n_cluster = n_cluster
        self.max_ittractions = max_ittractions
        self.centriod = None
    
    def fit_predict(self, dataset):
        # 2) init centriods
        
        centriod = random.sample(range(dataset.shape[0]), self.n_cluster)
        self.centriod = dataset[centriod]   

        for i in range(self.max_ittractions):
            # 3) assign clusters
            clutsers = self.calcuate_distance(dataset)

            # 4) movie centriods
            new_centriodss = self.move_centriods(dataset, clutsers)
            old_Centriods = self.centriod
            self.centriod = new_centriodss
            # 5) Finish

            if old_Centriods == self.centriod.all():
                break

        return np.array(self.centriod), clutsers


    def calcuate_distance(self, dataset):
        # np.sqrt(np.dot(b-a, b-a))
        distnace = []   
        cluster_group = []

        for row in dataset:
            for centriods in self.centriod:
                distnace.append(np.sqrt(np.dot(row - centriods, row - centriods)))
            
            cluster_group.append(distnace.index(min(distnace)))

            distnace.clear()
        return np.array(cluster_group)
    

    def move_centriods(self, dataset, cluster):
        new_centriods = []
        clusterss = np.unique(cluster)
        for i in clusterss:
            new_centriods.append(dataset[cluster == i].mean(axis = 0))

        return np.array(new_centriods)