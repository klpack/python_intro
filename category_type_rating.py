import pandas as pd

# Reading in 
catalog=pd.read_csv('app_store.csv')
# Output printing 
print(catalog.groupby(['Category','Type'])['Rating'].mean())