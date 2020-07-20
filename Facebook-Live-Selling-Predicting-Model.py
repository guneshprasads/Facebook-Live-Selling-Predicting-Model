#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the datasets
dataset = pd.read_csv('Live.csv')

#lets see the small part of the dataset
dataset.head(2)

#there is no use of last four coloumns
dataset=dataset.drop(dataset.columns[[-1,-2,-3,-4]],axis=1)

#lets find the count unique values 
dataset.info()
dataset.nunique()

#Remove the Duplicate Values 
duplicated_data = dataset[dataset['status_id'].duplicated() == True]
dataset1 = dataset.drop_duplicates(subset='status_id',keep='last')

