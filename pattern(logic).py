n=int(input())
for i in range(1,n+1):
    a=[]
    for j in range(1,i):
        print(i,end=" ")
        a.append(i)
    for j in range(i,n+1):
        print(j,end=" ")
        a.append(j)
    b=a[::-1]
    for i in range(1,len(b)):
        print(b[i],end=" ")
    print()
for i in range(n-1,0,-1):
    a=[]
    for j in range(1,i):
        print(i,end=" ")
        a.append(i)
    for j in range(i,n+1):
        print(j,end=" ")
        a.append(j)
    b=a[::-1]
    for i in range(1,len(b)):
        print(b[i],end=" ")
    print()