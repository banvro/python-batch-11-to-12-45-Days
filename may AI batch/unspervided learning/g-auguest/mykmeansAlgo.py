# Steps:      n = 3
#     1) Decoide N-Cluster   --> done
#     2) init Centriod ------> 
#     3) Assign Clustere
#     4) Move Centriod
#     5) Finish
import random 
import numpy as np

class MyKmeansAlgoClass:
    def __init__(self, n_cluster = 3, max_ittrtion = 100):
        self.n_cluster = n_cluster
        self.max_ittrtion = max_ittrtion
        self.centriod = None
    
    def fit_predict(self, dataset):
        # print(dataset.shape[0])
        #     2) init Centriod 
        centriod_index = random.sample(range(dataset.shape[0]), self.n_cluster)
        # print(dataset)
        # print(centriod_index, "qqqqqqqq")
        dataset = dataset.values
        self.centriod = dataset[centriod_index]

        x = 0
        for i in range(self.max_ittrtion):
            x = x + 1
            # 3) Assign Clustere
            group_cluster = self.assign_cluster(dataset)

            # 4) Move Centriod
            new_centriods = self.move_centriod(dataset, group_cluster)
            old_centriods = self.centriod
            self.centriod = new_centriods

            # 5) Finish
            if (old_centriods == self.centriod).all():
                break

        return group_cluster, self.centriod, x
    
    def assign_cluster(self, dataset):
        distance = []
        cluster_group = []

        for i in dataset:
            for centriod in self.centriod:
                distance.append(np.sqrt(np.dot(i - centriod, i - centriod)))
            print(distance)
            min_distance = min(distance)
            # print(min_distance)
            # print(distance.index(min_distance))
            cluster_group.append(distance.index(min_distance))
            # cluster_group.append()
            distance.clear()

        return np.array(cluster_group)



    def move_centriod(self, dataset, group_cluster):
        new_centriod = []
        # distances = []
        # print(group_cluster)
        cluster_type = np.unique(group_cluster)
        
        # print(dataset[cluster_type == 0])
        
        for type in cluster_type:
            new_centriod.append(dataset[group_cluster == type].mean(axis = 0))
        # print("original", self.centriod)
        # print(new_centriod)
            # for j in dataset[group_cluster == type]:
            #     xyz = np.sqrt(np.dot(self.centriod[type] - j, self.centriod[type] - j))
            # print(xyz)
            # print(dataset[group_cluster == type])
        return np.array(new_centriod)

