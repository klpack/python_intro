def encode(string):
    
    string.lower()
    stringF = string.replace(" ","")
    print(stringF)
    # Alphabets
    alpha = "abcdefghijklmnopqrstuvwxyz "
    cipher = "zyxwvutsrqponmlkjihgfedcba "
    
    # Counter
    counter = 0

    # Lists
    alphalist = list(alpha)
    cipherlist = list(cipher)
    indexlist = []
    stringlist = list(stringF.lower())
    
    # List for new cipher
    newlist = []
    
    # For loop to determine what to add to cipher list
    for letter in stringlist:
        
        indexlist = alphalist.index(stringlist[counter])
        counter = counter + 1
        
        newlist.append(cipher[indexlist])
    
       
    # Printing out by five
    subgroupsize = 5
    while subgroupsize < len(newlist):
        newlist.insert(subgroupsize, ' ')
        subgroupsize += (5+1)
    
    returnstring = ''.join(newlist)
    return(returnstring)


print(encode("The quick brown fox jumps over the lazy dog"))





def decode(string2):

    string2.lower()

    # Alphabets
    alpha = "abcdefghijklmnopqrstuvwxyz "
    cipher = "zyxwvutsrqponmlkjihgfedcba "
    
    # Counter
    counter = 0

    # Lists
    alphalist = list(alpha)
    cipherlist = list(cipher)
    indexlist = []
    stringlist = list(string2)
    newlist = []
    
    # For loop to decide what to add to cipher list
    for letter in string2.lower():
        
        indexlist = cipherlist.index(string2.lower()[counter])
        
        counter = counter + 1
        
        newlist.append(alpha[indexlist])
        returnlist = str(newlist)
        returnlist = "".join(newlist)
        returnlist.split()

    return (returnlist)
print(decode("gsv jfrxp yildm ulc qfnkh levi gsv ozab wlt"))

