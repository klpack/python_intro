import numpy as np
import matplotlib.pyplot as plt
from catalog import products

def plot_product_weight_inventory(products):

    #Call out of data
    weights = products[:, 4]
    inventory = products[:, 3]
    wvsi = products[:,3:4]
    weights = weights.astype(float)
    inventory = inventory.astype(float)
    print(weights)
    print(inventory)
    
    #Scatter Plot Information
    
    plt.scatter(weights,inventory,s=1)
    
    
    
    plt.xlabel('Weight')
    plt.ylabel('Inventory')
    plt.title('Product Weight-Inventory Relationship')

    plt.show()

print(plot_product_weight_inventory(products))