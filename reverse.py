"""

Kenneth Levi Pack
Student ID:800137008
Homework 2
Problem 1 (Reverse)

"""


# This program takes the input from the called 
# function (reverse) and displays the inverse 
# of that specific string.



def reverse(oldString):         
    
    reversed_string =  " " # starting out with a blank string 
    index = len(oldString)      # len(str1) sets the max index when string is called through reverse
    
    while index > 0:       # while the index is greater than 0, 
     
     reversed_string += oldString[ index - 1]
     index = index - 1     # decreases the index on the next iteration of string replacement

    return reversed_string # returning the reversed string

print(reverse(" !skrow ti ,nrad eb ll'I "))     # printing out the final statement showing string has been reversed


     

