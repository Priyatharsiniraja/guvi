dj,km=map(int,input().split())
km=list(map(int,input().split()))[:dj]
com=0
for d in range(0,len(km)-1):
  for min in range(d+1,len(km)-1):
    if(km[d]+km[min]==km):
      com+=1  
if com==1:
  print("yes")
else:
  print("no")
