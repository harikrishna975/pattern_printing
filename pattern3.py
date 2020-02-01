n=int(input())
a=['0']
b=[]
for i in range(n,-1,-1):
    for j in range(n,n-i,-1):
        print(" ",end="")
    print(''.join(a))
    for j in range(n-1,n):
        x=i
        a.insert(0,str(x))
        a.append(str(x))