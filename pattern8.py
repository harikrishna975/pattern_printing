n=int(input())
a=[]
cnt1=n+2
for i in range(1,n+1):
    cnt=1
    cnt1=cnt1-1
    x=cnt1
    for j in range(1,i):
        print(x,end=" ")
        x=x+1
    for j in range(i,n+1):
        print(cnt,end=" ")
        cnt=cnt+1
    print()