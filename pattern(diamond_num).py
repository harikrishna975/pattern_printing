n=int(input())
a=[]
n=n+1
for i in range(n):
    cnt=i
    b=[]
    for j in range(n-i-1):
        b.append(" ")
    for j in range(n-i-1,n):
        b.append(cnt)
        cnt=cnt-1
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