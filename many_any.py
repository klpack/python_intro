def many_any(list1,num):
    
    # Comparing Value 
    counter = 0
    
    # Increasing Counter
    for boolean in list1:
        if boolean == True:
            counter = counter + 1
        else:
            counter = counter + 0
            
    # Decisions 
    if counter >= num:
        return True 
    else:
        return False
        

print(many_any([True, True, False, False], 3))