import numpy as np
import matplotlib.pyplot as plt
from data import raw_data

def plot_all_type_counts(raw_data):
 counter = 0
 i = 0
 while i < 10000:
    if 'Paid' in raw_data[i]:
        counter = counter + 1
    i = i + 1
 print(counter)
 print(raw_data[1,[1]])



plot_all_type_counts(raw_data)