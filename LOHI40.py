vl2,gv=map(int,input().split())
l6=list(map(int,input().split()))
vl2=[]
l6.insert(0,0)
for a in range(gv):
     uu=[]
     summup=0
     xx,yy=map(int,input().split())
     for c in range(xx,yy+1):         
         summup^=l6[c]     
     vl2.append(summup)
for d in vl2:
    print(d)
