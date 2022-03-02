"""

Kenneth Levi Pack
Student ID:800137008
Homework 2
Problem 2 (Average)

"""


def average(*numbers):
    counter = 0             # initial counter starting at zero will keep track of how many numbers are being called
    sum_all = 0             # the initial sum starting at zero 

    for number in numbers:
        sum_all += number       # adding that specific number at the beginning everytime there is a number 
        counter = counter + 1   # increasing the counter by one everytime there is a number 
        
    sum_all = sum_all / counter # dividing the sum by the amount of numbers (my counter) the produce the average 
    
    return sum_all 
    
    


print("The average of the numbers is: ", average(2,5,8,11)) # calling the fucntion with example numbers
 
