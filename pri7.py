a,n=map(int,input().split())
arr=list(input().split())
arr=[int(x) for x in arr]
sum=0
for j in range(0,n):
  sum=sum+arr[j]
print(sum)
