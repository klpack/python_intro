# Homework 11 Problem 2

import pandas as pd
import matplotlib.pyplot as plt
catalog = pd.read_csv('app_store.csv')

#Pritnign out statsitics about the sizes of the apps 
# printing column values statistics (we transpose the result to ensure all the values are displayed)
print('\n Size statistics:')
print(catalog['Size'].describe(include='all').T)

# Creating a subset and printing out largest app sizes - I chose that a large app qualified as larger than 99.0
largest = catalog[(catalog['Size'] > 99.0)]

# Deleting out what we do not want
del largest['Android Ver']
del largest['Current Ver']
del largest['Last Updated']
del largest['Genres']
del largest['Content Rating']
del largest['Price']

# Output 
print('\n The largest apps are: ')
print(largest)
