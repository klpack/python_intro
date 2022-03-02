# This program takes the sum of a number, starting at 1 to that number
# and sqaures it then sqaures each individual number from 1 to the sum 
# and it finds the difference between the two

"""

Kenneth Levi Pack
Student ID:800137008
Homework 2
Problem 4 (Difference)

"""



def difference(num):
    
    #These operations handle all the initial math behind summing and sqauring 
    num_range = range(1,num+1,1)
    num_sum = sum(num_range)
    num_square = num_sum ** 2

    
    
    squared_range = [] # Blank list to start out 

    # Squaring each and every individual value in the range of numbers
    for values in num_range:
        squared_range.append(values ** 2)
    
    # Summing the sqaures
    sumSqaured = sum(squared_range)

    # Sqaured Difference
    squaredDifference = num_square -sumSqaured

        
    return squaredDifference    # returning the final value 
print(difference(10))           # function calling with given example 