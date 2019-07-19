from iter import combine
pi,p1=map(int,input().split())
li=len(str(pi))
lst=list(combine(str(pi),li-p1))
lst=sorted(lst)
print(*lst[0],sep='')
