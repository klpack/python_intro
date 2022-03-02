import math # importing math function

# funciton of aliqout that is later pulled into classify function 
def aliquot_sum(number):    # aliqout function
    factors = set()         
    
    # math for aliqout 
    upper_bound = int(math.sqrt(number)) 
    for i in range(1, upper_bound + 1):
        if number % i == 0:
            factors.update([i, number//i])
    factors.remove(number)
    return sum(factors) 

def classify(number):       # classify function
    if number <= 0:
        raise ValueError("Error") #raisning value error 

    a_sum = aliquot_sum(number) # calling aliqout sum

    # conditions deciding what the number is 
    if a_sum == number:
        return 'perfect'
    if a_sum > number:
        return 'abundant'
    return 'deficient'

print(classify(8))      # calling classify