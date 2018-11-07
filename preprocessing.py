import pandas as pd
import numpy as np
from sklearn import datasets,  preprocessing, linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


data = np.reshape(np.randn(20),(10,2))
labels = np.random.randint(2, size=10) # 10 labels

print(data)
