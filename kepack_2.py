"""

Kenneth Levi Pack
IE 331
Student ID: 800137008
Problem #2

"""
list = [] # Blank list before adding numbers that are divisors
import random   # Importing random to generate random number
 
rand_num = random.randint(1,1000) # Random number stored in variable rand_num

counter = 0 # Starting off the counter at zero, checking for all numbers going into random generated number

"""

While loop is used to keep increasing the counter to check if that number is specifically
a divisor or not. Once checked, if there is no remainder, that specific counter value is 
added to my list.

"""
while counter <= rand_num:
    counter = counter + 1 #Increasing Counter by one each if statement iteration 
    
    if rand_num % counter  == 0 :
        list.append(counter)
       
print( "\nThe numbers that go into",rand_num ,"are", list)      # Printing the total list of numbers

"""

If statements declaring whether or not the number that is generated is prime or not. 
First statement checking and seeing if length is greater than 2, and if so it is composite,
becasue we know it should have a list that is longer than 2. If the list is equal to 2,
we now know it is a prime number becasue all that can go into the number is itself and 1.

"""
if len(list) > 2:                         
    print("\n",rand_num, "is composite number.")
if len(list) ==2:
    print("\n",rand_num, "is a prime number.")