rp1,rp2=input().split()
cost_diff1=abs(len(rp1)-len(rp2))
for i in range(len(rp1)):
    if len(rp2)==1 and rp2[i] in rp1:
        break
    if rp1[i] != rp2[i]:
        cost_diff1+=1 
print(cost_diff1)
