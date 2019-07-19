def power(b,i ):
    if(i==1):
     return(b)
    if(i != 1):
     return(b*power(b,i-1))
b,i = map(int,(input().split()))
print(power(b,i))
