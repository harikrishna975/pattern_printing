n=int(input())
for i in range(1,n+1):
    cnt=i
    for j in range(1,n+1):
        print(cnt,end=" ")
        cnt=cnt+n
    print()
        