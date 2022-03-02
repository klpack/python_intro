"""

Kenneth Levi Pack
IE 331
Student ID:800137008
Problem #1

"""

#Initial Variable Input - asking user for a input to be tested
number = int(input("Enter a whole integer: " ))

  
#Counter for increasing divisibilty
counter = 1                 # Starting out counter at 1


while counter <= number:     # While loop - while counter keeps on going if statement keeps running
    if number % counter == 0:  # If statement deciding whether or not the number has no remainder divided by counter
        print(counter)     # Printing the exact number out 
    counter = counter + 1  #Increasing Counter
else: 
    print("\n See numbers above.")  #Statement telling you to see numbers above.












