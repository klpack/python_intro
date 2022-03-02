

def check_symbols(string):
    list1 = list(string)
    
    alpha = "qwertyuiopasdfghjklzxcvbnm"
    alphalist = list(alpha)
    
    
    for letter in string:
       
        if letter in string[0]:
            return False

        if letter in alphalist:
            
        
            counter = string.index(letter)
            counter2 = string.index(letter)
            if string[counter-1] == "+" and string[counter+1] == "+" and string[counter2-1] == "+" and string[counter2+1 == "+"]:
                return True
            else:
                return False
    
    



print(check_symbols("+f++d"))