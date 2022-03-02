import numpy as np

# Function to remove specified columns from the coefficients matrix
def squarify(matrix, column_indicies):
    #Reversing
    for index in reversed(column_indicies):   
        
        #Removing certain column
        matrix = np.delete(matrix, index, 1) 
    return matrix


def solve(coeffs, right_hand_side, column_indicies):
    #Making it square
    if coeffs.shape[0] != coeffs.shape[1]:            
        coeffs = squarify(coeffs, column_indicies)
    #solving
    solved = np.linalg.solve(coeffs, right_hand_side) 
    for index in column_indicies:
        #Placing Zeroes
        solved = np.insert(solved, index, 0) 
        #2 Decimal Places         
    return np.around(solved, decimals = 2)            


a = np.linspace(1, 14, 24)
a.shape = (4, 6)
b = np.linspace(10, 20, 4)

print(solve(a, b, [1, 3]))

