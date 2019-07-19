g=int(input())
j=[]
for i in range (0,g):
    j.append(input())
l1=len(k[0])
a=""
for i in range (0,l1):
    c=j[0][i]
    f=0
    for k in range (0,g):
        if(c!=j[k][i]):
            f=1
    if(f==0):
        a=a+c
    else:
        break
print(a)
