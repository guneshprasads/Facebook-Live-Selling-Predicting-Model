#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the datasets
dataset = pd.read_csv('Live.csv')

dataset['status_published'] = pd.to_datetime(dataset.status_published)
dataset.dtypes
dataset.insert(2, "Hours", dataset.status_published.dt.time, True)

#Creating the another dataset and Filtering the data Form the dataset