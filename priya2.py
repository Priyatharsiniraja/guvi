a=int(input("Enter the 1st value:"))
b=int(input("Enter the 2nd value:"))
c=int(input("Enter the 3rd value:"))
if((a>b) and(a>c)):
    print("a is greater",a)
elif((b>a) and(b>c)):
    print("b is greater",b)
else:
    print("c is greater",c)
