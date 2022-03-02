# This program is to check and verify an ISBN number
# Kenneth Levi Pack
# IE 331
# Problem 3

def verify_isbn(ISBN):
    
    
    alpha = "qwertyuiopasdfghjklzcvbnm".upper()     # non x alphabet
    alpha_list = list(alpha)    # list of the non x alphabet
    ISBN_Num = list(ISBN.upper())   # listing isbn input 
    
    for letters in alpha_list:      # Checking if no x alphabet is in the isbn at any given element
        if letters in ISBN_Num:
            return False

    # Operations handling every single insert
    Digit1 = int(ISBN_Num[0])*10
    Digit2 = int(ISBN_Num[1])*9
    Digit3 = int(ISBN_Num[2])*8
    Digit4 = int(ISBN_Num[3])*7
    Digit5 = int(ISBN_Num[4])*6
    Digit6 = int(ISBN_Num[5])*5
    Digit7 = int(ISBN_Num[6])*4
    Digit8 = int(ISBN_Num[7])*3
    Digit9 = int(ISBN_Num[8])*2
    Digit10 = (ISBN_Num[9])           # Only one we do not make int due to string, let it equal what it equals
    
    
    
    
    if Digit10 == "X":              # if that specific element equals X then it equals 10
        Digit10 = int(10)*1
    
    
        
    # summing all of the elements
    Big_Sum = (Digit1+Digit2+Digit3+Digit4+Digit5+Digit6+Digit7+Digit8+Digit9+Digit10)
    
    
    # checking if the big sum is evenly divisble with no remainder
    Modulous = Big_Sum % 11

    # If Statements determining if no remainder
    if Modulous == 0:
        return True
    else:
        return False

print(verify_isbn("359821507X"))