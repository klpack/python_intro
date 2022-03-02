from data import data 
import numpy as np

def cal_cat_sizes(data):
    result = dict()

    for row in data:
        if row[1]=='':
            continue
        if row[1] in result:
            result[row[1]]+=1
        else:
            result[row[1]] = 1

    return result

print(cal_cat_sizes(data))

def cal_size_histo(data):
    sizes = []

    for row in data:
        raw_size=row[4]

        if raw_size[-1] == 'M':
            size = float(raw_size[:-1])
            sizes.append(size)
        elif: raw_size[-1] == 'k':
            size = float(raw_size[:-1]) / 1024
            sizes.append(size)

    sizes_array = np.array(sizes)
    counts,ranges = np.histogram(sizes_array,5)


    return (counts,ranges)
print(cal_size_histo(data))
