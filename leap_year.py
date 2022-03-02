# This program defines a function and determines whether or not a certain year is a leap year

"""

Kenneth Levi Pack

"""

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:   # if statement takes care of it being evenly divisible by 4 and not divisible by 100
        return True 
    else: 
        return False  

print(leap_year(1900))
