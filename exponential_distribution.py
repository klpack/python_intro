from catalog import products
import matplotlib.pyplot as plt
import numpy as np


def plot_distribution(size,mean):
    mean = float(mean)
    exp_dist = np.random.exponential(mean,size)
    plt.hist(exp_dist,bins=10,density=True,label="Histogram of EXP Distribution",rwidth=5)
    plt.xlim(0,20)
    x = np.linspace(0,20,len(exp_dist))
    exp_dist_theoretical = (1/mean)*np.exp(-x/mean)
    plt.plot(x,exp_dist_theoretical,label="Exponential Distribution")
    plt.xlabel("Distribution of x values")
    plt.ylabel("probability density function")
    plt.title("Exponential Distribution with mean={}".format(mean))
    plt.legend()
    plt.grid()
    plt.show()


plot_distribution(50,5)