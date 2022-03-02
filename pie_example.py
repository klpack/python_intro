#Importing Numpy and Data Files
import numpy as np
import matplotlib.pyplot as plt
from catalog import products

def plot_prices_histogram(products):
    i = 0
    #Call Out of Price Column
    prices = products[:, 2]
    prices = prices.astype(int)

    for info in prices:
        if prices[i] < 70: 
            print(prices[i])
        i = i + 1
    #Histogram Information
    num_bins = 10
    plt.hist(prices, bins=num_bins)

    plt.xlabel('Price')
    plt.ylabel('Count')
    plt.title('Product Price Histogram')
    plt.show()

plot_prices_histogram(products)