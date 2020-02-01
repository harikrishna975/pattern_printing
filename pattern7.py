n=int(input())
a=[]
for i in range(1,2*n,2):
    a.append(i)
#print(a)
for i in range(n):
    x=a[i:]
    y=a[:i]
    res=x+y
    for j in range(n-i):
        print(res[j],end="")
    res2=y[::-1]
    for j in range(i):
        print(res2[j],end="")
    print()
        
#other pattern of same type
    
n=int(input())
a=[]
for i in range(1,2*n,2):
    a.append(i)
for i in range(n):
    x=a[i:]
    y=a[:i]
    res=x+y
    for j in range(n):
        print(res[j],end="")
    print()