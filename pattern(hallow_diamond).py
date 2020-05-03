n=int(input())
a=[]
for i in range(n):
    b=[]
    for j in range(n-i):
        b.append("*")
    for j in range(n-i,n):
        b.append(" ")
    c=b[:-1]
    c=c[::-1]
    b=b+c
    a.append(b)
for i in a:
    for j in i:
        print(j,end=" ")
    print()
for i in range(n-2,-1,-1):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()
    
#with alphabets 
n=int(input())
a=[]
for i in range(n):
    b=[]
    cnt=65
    for j in range(n-i):
        b.append(chr(cnt))
        cnt=cnt+1
    for j in range(n-i,n):
        b.append(" ")
    c=b[:-1]
    c=c[::-1]
    b=b+c
    a.append(b)
for i in a:
    for j in i:
        print(j,end=" ")
    print()
for i in range(n-2,-1,-1):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()
        
        