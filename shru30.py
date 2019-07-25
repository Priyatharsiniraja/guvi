d1,d2=map(int,input().split())
lisseq=list(map(int,input().split()))
l6=[]
for i in range(0,d2):
     a6,b6=map(int,input().split())
     l6.append([a6,b6])
for i in range(d2):
     lower1=l6[i][0]
     upper1=l6[i][1]
     s7=sum(lisseq[lower1-1:upper1])
     print(s7)
