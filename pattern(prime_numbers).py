n=int(input())
cnt=0
a=[]
for i in range(1,10000):
	for j in range(2,i):
		if i%j==0:
			break
	else:
# 		print(i,end=" ")
		a.append(i)
		cnt=cnt+1
	if cnt==n:
	    break
#print(a)
for i in range(len(a)):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(n-i-1,(n-i-1+a[i])):
        print("*",end=" ")
    print()
