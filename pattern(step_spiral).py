n=int(input())
a=[]
for i in range(n):
    b=[]
    cnt=1
    for j in range(i+1):
        b.append(cnt)
        cnt=cnt+1
    for j in range(i+1,n):
        b.append(b[-1])
    c=b[:-1:]
    b=b+c[::-1]
    a.append(b)
for i in a:
    for j in i:
        print(j,end=" ")
    print()
for i in range(n-2,-1,-1):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()
    
    
##other logic for the same problem
#n=int(input())
#for i in range(-n+1,n):
#    for j in range(-n+1,n):
#        if abs(i)>=abs(j):
#            print(abs(n-i),end="")
#        else:
#            print(abs(n-j),end="")
#    print()