

def is_armstrong(num):

    num = int(num)

    if num < 0:
        raise ValueError('Input must be positive integer')

    # Mapping to integer list
    number_list = list(map(int, str(num)))

    # Operations for every single element
    number_list_length = len(number_list)
    new_number_list = []

    # Operation
    for values in number_list:
        new_number = values ** number_list_length
        new_number_list.append(new_number)
    

    #Determination
    if num == (sum(new_number_list)):
        return(True)

    elif num != (sum(new_number_list)):
        return(False)
    
print(is_armstrong(153))