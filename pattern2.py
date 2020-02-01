n=int(input())
cnt=0
for i in range(1,n+1):
    for j in range(i):
        cnt=cnt+1
        print(cnt,end=" ")
    x=cnt
    for j in range(i,2*i-1):
        x=x-1
        print(x,end=" ")
    print()