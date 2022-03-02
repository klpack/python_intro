"""

Kenneth Levi Pack
IE 331
Student ID: 800137008
Problem #3

"""

# Function to print out the fibonacci numbers in sequence

def fibo(num):
   
   if num <= 1:
       return num
   else:
       return(fibo(num-1) + fibo(num-2)) 


# User input asking for the amount of terms

num_terms = int(input("Please enter the amount of terms: "))






# if statements checking to make sure the terms will work



if num_terms <= 0:
   print("Plese enter a positive integer") # if the terms entered is zero or below this statement will tell user to input positive integer
else:
   print("Fibonacci sequence is as follows:")
   for i in range(num_terms):
       print(fibo(i))