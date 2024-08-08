
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from mykmeansAlgo import MyKmeansAlgoClass

df = pd.read_csv("data.csv")

my_predictor = MyKmeansAlgoClass()

new_dataset = df.drop(columns = ["color"])

group_cluster, centriod, x = my_predictor.fit_predict(new_dataset)


print(x)
# print(new_dataset[group_cluster == 0]["x"])

plt.scatter(df["x"], df["y"])
plt.scatter(new_dataset[group_cluster == 0]["x"], new_dataset[group_cluster == 0]["y"])
plt.scatter(new_dataset[group_cluster == 1]["x"], new_dataset[group_cluster == 1]["y"])
plt.scatter(new_dataset[group_cluster == 2]["x"], new_dataset[group_cluster == 2]["y"])
# plt.scatter(new_dataset[group_cluster == 1, 0], new_dataset[group_cluster == 1, 1])
# plt.scatter(new_dataset[group_cluster == 2, 0], new_dataset[group_cluster == 2, 1])
plt.scatter(centriod[0][0], centriod[0][1], s = 300)
plt.scatter(centriod[1][0], centriod[1][1], s = 300)
plt.scatter(centriod[2][0], centriod[2][1], s = 300)
plt.show()