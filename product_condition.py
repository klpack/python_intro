from catalog import products
import matplotlib.pyplot as plt
import numpy as np

# User Defined Function Plotting Product Condition
def plot_product_condition(products):
    
    # Counter varibales for array dimensions
    i = 0
    u = 0
    n = 0
    
    # Counter Variables for Products
    counterNew = 0
    counterRefurb = 0
    counterUsed = 0
    
    # Loop to run and conditions to count 
    for info in products:
        if products[i][5] == "New":
            counterNew = counterNew + 1
        i = i +1
        
        if products[u][5] == "Used":
            counterUsed = counterUsed + 1
        u = u + 1

        if products[n][5] == "Refurbished":
            counterRefurb = counterRefurb + 1
        n = n + 1
    
    # Total Product Conditions 
    total = counterNew + counterRefurb + counterUsed

    # Percentages
    PercentageNew = counterNew / total
    PercentageUsed = counterUsed / total
    PercentageRefurb = counterRefurb / total

    # Percentage Array
    PecentageArray = [PercentageNew,PercentageUsed,PercentageRefurb]

    # Plotting the pie chart
    labels = ["New","Used","Refurbished"]
    plt.pie(PecentageArray, labels=labels,
            autopct='%1.1f%%', startangle=90)  
    plt.title("Product Conditions")
    plt.show()  
   
    # Coding below was to check certain things and counters
    #print(counterNew)
    #print(counterRefurb)
    #print(counterUsed)   
    #print(products[0][5])

plot_product_condition(products)
