# In computer programming, pandas is a software library written for the Python programming
# language for data manipulation and analysis. In particular, it offers data structures
# and operations for manipulating numerical tables and time series.

# By convention, the pandas library is typically imported as 'pd'.

import pandas as pd

# pandas.read_csv: Read CSV (comma-separated) file into DataFrame
catalog = pd.read_csv('catalog.csv')

# Pandas provide a two-dimensional size-mutable, potentially heterogeneous tabular data
# structure with labeled axes (rows and columns) called DataFrame. Everytime data is loaded
# from a source, pandas loads it into a data frame.
print(catalog)
print(type(catalog))

# DataFrame.info: Print a concise summary of a DataFrame.
print(catalog.info())

# DataFrame.shape: Return a tuple representing the dimensionality of the DataFrame.
print(catalog.shape)

# DataFrame.describe: Generates descriptive statistics that summarize the central
# tendency, dispersion and shape of a dataset's distribution, excluding NaN values.
print(catalog.describe(include='all'))

# len(DataFrame): Returns number of rows in the data frame.
print(len(catalog))

# DataFrame.loc: Access a group of rows and columns by label(s) or a boolean array.
print(catalog.loc[0])

# DataFrame.iloc: Purely integer-location based indexing for selection by position.
print(catalog.iloc[0])

# DataFrame.head([n]): Return the first n rows. If n is not specified, the first 5
# rows of the data frame will be returned.
print(catalog.head())

# DataFrame.head([n]): Return the last n rows. If n is not specified, the last 5
# rows of the data frame will be returned.
print(catalog.tail())
