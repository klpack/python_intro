# This program is about bob the teenager responding to different text phrases
# Kenneth Levi Pack
# IE 331
# Problem 2


def hey(phrase):
    
    list1 = list(phrase.upper()) # this function takes phrase and splits in into every characte into a list
    

    if "?" in list1 and phrase != phrase.upper():   # Checking if sentence ends with a ? while ignoring uppercase
        print("\n Sure.")

    if phrase == phrase.upper() and "?" not in list1 and len(phrase) > 0: # Checks if phrase is upper with no ? - phrase must be greater than zero
        print("\n Whoa, chill out!") 
    
    if phrase == phrase.upper() and "?" in list1:   # Checks if upper and ? in phrase
        print("\n Calm down, I know what I’m doing!")
    
    if phrase == "" or phrase == " " and phrase != phrase.upper() and phrase != phrase.lower(): # Checks if nothing is said
        print("\n Fine. Be that way.")
    else:
        print("Whatever.") # Respoding to anything else 

hey("fuck.")



