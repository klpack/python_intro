# Making revised app store
# Homework 11 Problem 3

import pandas as pd
import matplotlib.pyplot as plt
catalog = pd.read_csv('app_store.csv')

# Filtering the things we do not want 
new_apps = catalog[(catalog['Content Rating'] == 'Everyone') & (catalog['Rating'] > 4.0)]

# Deleting things we do not want 
del new_apps['Android Ver']
del new_apps['Current Ver']
del new_apps['Last Updated']

# Printing out the new data 
print(new_apps)



str_apps = str(new_apps)

# Writing data to a new file 
#revised app store.csv
revised_app_file = open('revised_app_store.csv',"w+")
revised_app_file.write(str_apps)
revised_app_file.close()

