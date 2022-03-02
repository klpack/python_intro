

def check_symbols(string):
    list1 = list(string)
    
    # Alphabet
    alpha = "qwertyuiopasdfghjklzxcvbnm"
   
   # Alphabet list
    alphalist = list(alpha)
    Length = len(string)
    # Operations
    for letter in string:
       
        if list1[0] in alphalist or list1[Length-1] in alphalist:
        
            return False

        if letter in alphalist:
        
            # coutning the letter at index
            counter = string.index(letter)
            
            
            if string[counter-1] == "+" and string[counter+1] == "+":
                return True
            else:
                return False
    
    



print(check_symbols("+d+=3=+s+"))