import numpy as np

def saddle_point(matrix):
    array = np.array(matrix)
    
    result = set()
    for row_index, row in enumerate(array):
        for column_index, element in enumerate(row):
            #column = [_row[column_index] for _row in matrix]

            if element ==max(row) and element == min(array[...,column_index]):
                result.add((row_index,column_index))

    return result

print(saddle_point([ [6,7,8],
                     [5,5,5],
                     [7,5,6]]))