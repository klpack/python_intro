from catalog import products
import matplotlib.pyplot as plt
import numpy as np

def plot_product_weight_inventory(products):


    #Call out of data
    weights = products[:, 4]
    inventory = products[:, 3]
    
    # Converting type
    weights = weights.astype(float)
    inventory = inventory.astype(float)
    
    
    #Scatter Plot Information
    
    plt.scatter(weights,inventory,s=1)
    plt.xlabel('Weight')
    plt.ylabel('Inventory')
    plt.title('Product Weight-Inventory Relationship')

    plt.show()

plot_product_weight_inventory(products)
