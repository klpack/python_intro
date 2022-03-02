# This program generates random robot names and numbers
import random 
def generate_name():
    upperAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # 3 random numbers for the robot name
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)
    number3 = random.randint(0,9)
    
    # making the upper alphabet a list
    upperAlphaList = list(upperAlpha)
    
    # random place in the upper alphabet tp pick the letters
    randomPlace1 = random.randint(0,25)
    randomPlace2 = random.randint(0,25)

    # picking the letters
    upperAlphaList1 = upperAlphaList[randomPlace1]
    upperAlphaList2 = upperAlphaList[randomPlace2]

    # printing out the letters and numbers
    print("The robot name is: " + upperAlphaList1,upperAlphaList2,number1,number2,number3)
    

generate_name()