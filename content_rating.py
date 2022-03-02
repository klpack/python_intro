# Homework 12 Problem 2

import pandas as pd
import matplotlib.pyplot as plt
catalog = pd.read_csv('app_store.csv')

paid = catalog[(catalog['Type'] == 'Paid')]
print(paid)

reviews_paid = paid.groupby('Content Rating')['Reviews'].sum()
print(reviews_paid)

reviews_paid.plot.pie(title="Reviews based on the content rating",autopct='%1.0f%%')
plt.show()