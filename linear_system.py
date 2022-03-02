import numpy as np
from data import data
from data import raw_data

def solve(a,b,ignore_columns):
    #Remove ignored columns
    square_a = np.delete(a,ignore_columns,1)

    x = np.linalg.solve(square_a,b)

    for index in ignore_columns:
        x = np.insert(x,index,0)

    return np.around(x,2)

a = np.linspace(1,14,24)
a.shape = (4,6)
b = np.linspace(10,20,4)
x = solve(a,b,[1,3])
print(x)