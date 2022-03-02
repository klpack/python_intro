
def slices(series1,length1):
    sub = ""
    substirng = list(sub)
    
    if length1 > len(series1) or length1 == 0:
        raise ValueError("Error")
    
    counter = 0
    
    while counter <= length1:
        
        seriesSlice = series1[counter:length1+counter]
        
        print(seriesSlice)
        counter = counter + 1

   
slices("9142",2) 
