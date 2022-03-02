import re
def encode(plainText):
    plainText=re.sub('[^A-Za-z0-9]+', '',plainText).lower()
    length=len(plainText)

    r=1
    while(True):
        c=r+1
        if((r*c)>=length):
            break
        r+=1
    square=[]
    k=0
    for i in range(0,r):
        list1=[]
        for j in range(0,c):
            if(k<length):
                list1.append(plainText[k])
            else:
                list1.append(' ')
            k+=1
        square.append(list1)
    str1=''
    j=0
    i=0
    k=0
    for j in range(c):
        for i in range(r):
            if(square[i][j] is not ' '):
                str1+=square[i][j]
            k+=1
        str1+=' '
    return str1

#plainText=input('Enter a message to be encode: ')
#print('Encoded text is: ',encode(plainText))
encode