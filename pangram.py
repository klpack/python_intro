# This program determines whether or not a certain sentence string is a pangram or not 
# Kenneth Levi Pack
# IE 331
# Problem 1

def is_pangram(string):
    
    
    alpha = "abcdefghijklmnopqrstuvwxyz"   # complete alphabet 
    
    for char in alpha:          # checking if character in alphahbet
        if char not in string:  # if statement for checking in the string
            return False        # returning True
            
    return True                 # returning False
    

print(is_pangram("The quick brown fox jumps over the lazy dog"))
