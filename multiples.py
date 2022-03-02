


def sum_of_multiples(limit,multiples):
    SumAll = 0 # initial sum
    counter = 2

    #take each multiple out of list and assign it to a variable having the numbers on two different variables to check against themselves
    FirstCheck = multiples[0] 
    SecondCheck = multiples[1]
    ThirdCheck = multiples[2]
    
    FirstFirst= multiples[0]
    SecondSecond = multiples[1]
    ThirdThird = multiples[2]

    #checking first number
    while FirstCheck < limit:
        SumAll = FirstCheck + SumAll # Adding the incresed variable to Sum
        FirstCheck = FirstFirst * counter # increasing the initial value to check against 30
        counter = counter + 1 # increasing counter
    
   
    counter = 2             # reinstating counter to 2
    
    
    #checking second number
    while SecondCheck < limit:
        SumAll = SecondCheck + SumAll
        SecondCheck = SecondSecond * counter # increasing the initial value to check against 30
        counter = counter + 1 # increasing counter
    
    counter = 2             # reinstating counter to 2

    #checking third number
    while ThirdCheck < limit:
        SumAll = ThirdCheck +SumAll       # Adding the incresed variable to Sum 
        ThirdCheck = ThirdThird * counter # increasing the initial value to check against 30
        counter = counter + 1             # increasing counter
    
    print(SumAll)  #printing the sum




(sum_of_multiples(30,[7,13,17]))