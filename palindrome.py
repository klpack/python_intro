# This is a function that determines whether or not a string argument is a palindrome 

def palindrome(string):
    counter = 0
    string = string.lower()
    listString = list(string)
    length = len(string)
    for i in string:
        counter = counter + 1
        length = length - 1
        if string[counter] == string[length-1]:
            return True
        else:
            return False

print(palindrome("Hannah"))