s1=int(input())
s2=[int(i) for i in input().split()]
yyy=0
for i in range(s1):
   for j in range(i):
      if s2[j]<s2[i]:
         yyy+=s2[j]
print(yyy)
