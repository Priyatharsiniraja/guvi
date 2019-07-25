hh,oo=map(int,input().split())
k1=[]
s2=[]
aa=[int(hh) for hh in input().split() ]
for i in range(0,oo):
    uu,vv=map(int,input().split())
    for j in range(uu-1 ,vv):
        s2.append(aa[j])
    xx=sorted(s2)
    k1.append(min(s2))
    del s2[:]
for z in range(0,len(k1)):
    print(k1[z])
