import numpy as np
from data import data
from data import raw_data
from collections import defaultdict


ref = {
    'App': 0,
    'Category': 1,
    'Rating': 2,
    'Reviews': 3,
    'Size': 4,
    'Installs': 5,
    'Type': 6,
    'Price': 7,
    'Content Rating': 8,
    'Genres': 9,
    'Last Updated': 10,
    'Current Ver': 11,
    'Android Ver': 12
}



def calculate_category_sizes(data):
    category_dict = dict()
    
    # Numpy Array to Pop Column Out
    app_cats = data[:,1]

    # Numpy Array to List
    app_cats = list(app_cats)

    # Dictionary on 1D List
    for category in app_cats:
        category_dict[category] = category_dict.get(category,0) + 1

    print(category_dict)

print(calculate_category_sizes(data))

  
def calculate_category_ratings(data):
    ratings = defaultdict(list)
    
    for app in data:
        if app[ref['Category']] == '' or app[ref['Rating']] == 'NaN':
            continue
        ratings[app[ref['Category']]].append(float(app[ref['Rating']]))
    for key, value in ratings.items():
        total = 0.0
        for rating in value:
            total += rating
        ratings[key] = round(total/float(len(value)), 2)
    return ratings
print(calculate_category_ratings(raw_data))

def calculate_type_sizes(data):
    type_dict = dict()
 
    cost = data[:,6]

    cost = list(cost)

    for value in cost:
        type_dict[value] = type_dict.get(value,0) + 1
    print(type_dict)
print(calculate_type_sizes(data))

def calculate_type_ratings(data):
    ratings = defaultdict(list)

    for app in data:
        if app[ref['Type']] == '' or app[ref['Rating']] == 'NaN':
            continue
        ratings[app[ref['Type']]].append(float(app[ref['Rating']]))
    for key, value in ratings.items():
        total = 0.0
        for rating in value:
            total += rating
        ratings[key] = round(total/float(len(value)), 2)
    return ratings
print(calculate_type_ratings(raw_data))


def calculate_size_histograms(data):
    histogram = defaultdict(int)
    sizes = []
    for app in data:
        if app[ref['Size']] == "Varies with device":
            continue
        size = float(app[ref['Size']][:-1])
        if app[ref['Size']][-1:] == 'k':
            size /= 1024

        sizes.append(round(size, 2))
    np.set_printoptions(suppress=True)
    histo, edges = np.histogram(sizes, 5)
    for i in range(len(edges)-1):
        histogram[round(edges[i], 2), "-", round(edges[i+1], 2)] = histo[i]
    return histogram

print(calculate_size_histograms(raw_data))