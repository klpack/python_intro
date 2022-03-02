def find_all_armstrong(lower_range,upper_range):
    
   
    
    #Converting to a list
    test_list = range(lower_range, upper_range+1,1)
    armstrong_list = []

    # Importing is_armstrong function
    from armstrong import is_armstrong

    # Operations
    for number in test_list:
        test_value = is_armstrong(number)

        if test_value == True:
            armstrong_list.append(number)
    
    return(armstrong_list)

print(find_all_armstrong(300,400))