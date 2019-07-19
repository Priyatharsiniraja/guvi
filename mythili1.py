p=int(input())
s=list(map(int,input().split(None,p)[:p]))
s.sort(key=None,reverse=True)
if s.count(0)==len(s):
    print(0)
else:
    print("".join(map(str,s)))
