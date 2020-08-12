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

#Plotting the status type
dataset2 = dataset1.status_type.value_counts().plot(kind='bar',figsize=(10,5),title='Status type')
dataset2.set(xlabel='status type',ylabel='count')

#lets add the all the reaction
dataset1['Total number of Reaction'] = dataset1.iloc[:,]
