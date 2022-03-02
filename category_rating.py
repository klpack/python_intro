# Homework 12 Problem 1

import pandas as pd
import matplotlib.pyplot as plt
catalog = pd.read_csv('app_store.csv')

#Getting Data I want - Categories assocated with ratings
mean_ratings = catalog.groupby('Category')['Rating'].mean()
print(mean_ratings)

#Plotting the data 
mean_ratings.plot.bar(title="Average Rating In Each Category")
plt.ylabel("Average Rating")
plt.show()