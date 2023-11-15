import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

dataset_train = pd.read_csv("./ds18B20.csv")
training_set = dataset_train.iloc[:, [0]]

sc = MinMaxScaler(feature_range=(0,1))
training_set_scaled = sc.fit_transform(training_set)

print(dataset_train)
print(training_set)
print(training_set_scaled)


