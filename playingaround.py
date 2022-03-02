import numpy as np


def solve(a, b, ignore_columns):
    # remove columns associated with 0 x's
    square_a = np.delete(a, ignore_columns, 1)

    # solve the linear system with squared a
    x = np.linalg.solve(square_a, b)

    # create updated_x for adding 0's at proper spots
    updated_x = x
    for column in ignore_columns:
        updated_x = np.insert(updated_x, column, 0)

    return np.around(updated_x, 2)


a = np.linspace(1, 14, 24)
a.shape = (4, 6)
b = np.linspace(10, 20, 4)
x = solve(a, b, [1, 3])
print(x)