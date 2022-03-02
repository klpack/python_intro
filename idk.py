import numpy as np
import matplotlib.pyplot as plt


y = np.random.rand(1000)
y.sort()
x = np.arange(len(y))

# Matplotlib allows having multiple axes (plots) on a figure. All plotting commands
# apply to the current axes.

# matplotlib.pyplot.subplots(nrows=1, ncols=1): Create a figure and a set of subplots.

# matplotlib.pyplot.subplot(nrows, ncols, index): Add/select a subplot to the current
# figure.

fig, ax = plt.subplots(2, 2)

# linear
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)


# log
plt.subplot(2, 2, 2)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log
plt.subplot(2, 2, 3)
plt.plot(x, y)
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)


# logit
plt.subplot(2, 2, 4)
plt.plot(x, y)
plt.yscale('logit')
plt.minorticks_off()
plt.title('logit')
plt.grid(True)

# matplotlib.pyplot.subplots_adjust(left=<>, bottom=<>, right=<>, top=<>, wspace=<>, hspace=<>):
# Tune the subplot layout.

# left: the left side of the subplots of the figure
# right: the right side of the subplots of the figure
# bottom: the bottom of the subplots of the figure
# top: the top of the subplots of the figure
# wspace: the amount of width reserved for space between subplots,
#         expressed as a fraction of the average axis width
# hspace: the amount of height reserved for space between subplots,
#         expressed as a fraction of the average axis height
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()