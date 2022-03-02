# Homework 11 Problem 1

import pandas as pd
import matplotlib.pyplot as plt
catalog = pd.read_csv('app_store.csv')

Cata = catalog.groupby('Category')['App'].count()
Cata.plot.bar(title="Number of Apps In Each Category")
plt.ylabel("Counts")
plt.show()
