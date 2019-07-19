s=int(input())
ar=list(map(int,input().split()))
kr=[]
an=[]
yeah=0
for i in range(s):
	if ar[i] in kr:
		yeah=1
		if ar[i] in an:
			pass
		else:
			an.append(ar[i])
	else:
		kr.append(ar[i])
an=list(sorted(an))
if(yeah==1):
	print(*an)
else:
	print("unique")
