from catalog import products
import matplotlib.pyplot as plt
import numpy as np

def plot_product_categories(products):
    # Counter Variables to count each category
    i = 0
    u = 0
    n = 0
    c = 0
    q = 0

    # Counter variables for each category
    Lighting = 0
    Electrical = 0
    Industrial = 0
    OfficeSup = 0
    Furniture = 0
    
    for info in products:
        if products[i][1] == "Office Supplies":
            OfficeSup = OfficeSup + 1
        i = i + 1
    
        if products[u][1] == "Electrical":
            Electrical = Electrical + 1
        u = u + 1

        if products[n][1] == "Industrial":
            Industrial = Industrial + 1
        n = n + 1

        if products[c][1] == "Furniture":
            Furniture = Furniture + 1
        c = c + 1

        if products[q][1] == "Lighting":
            Lighting = Lighting + 1
        q = q + 1
    
    # Amounts Array
    Amounts = (OfficeSup,Electrical,Industrial,Furniture,Lighting)
    
    # Plotting the bar graph
    Categories = ("Office Supplies", "Electrical", "Industrial", "Furniture", "Lighting")
    x_pos = np.arange(len(Categories))
    plt.bar(x_pos,Amounts)
    plt.ylabel("Count")
    plt.title("Amount in each category")
    plt.xticks(x_pos,Categories)
    plt.show()
plot_product_categories(products)