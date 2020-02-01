n=int(input())
for i in range(1,n+1):
    cnt=i
    for j in range(1,i+1):
        if j==1:
            print(i,end=" ")
        elif i>=j:
            print(cnt+n,end=" ")
            cnt=cnt+n
#        else:
#            print(" ",end=" ")
    print()