def score(string):
    
    # Different lists to compare strings

    list1 = list("aeioulnrst")
    list2 = list("dg")
    list3 = list("bcmp")
    list4 = list("fhvwy")
    list5 = list("k")
    list6 = list("jx")
    list7 = list("qz")

    # Initial Counter
    counter = 0

    # Statements determining the score total
    for letter in string:
        if letter in list1:
            counter = counter + 1
    
        if letter in list2:
            counter = counter + 2
            
        if letter in list3:
            counter = counter + 3

        if letter in list4:
            counter = counter + 4
        if letter in list5:
            counter = counter + 5

        if letter in list6:
            counter = counter + 8

        if letter in list7:
            counter = counter + 10
            
    return counter
print(score("cabbage"))