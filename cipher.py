

def rotate(phrase,key):
    alpha = "abcdefghijklmnopqrstuvwxyz" # original alphabet

    # new swapped alphabet
    alphaNew = alpha[key:] + alpha[:key]
    
    newPhrase = str.maketrans(alpha + alpha.upper(),alphaNew + alphaNew.upper()) # making the translation table
    return phrase.translate(newPhrase) # returning the new phrase
    
    


# printing new phrase
print(rotate("Let’s eat, Grandma!", 21)) 