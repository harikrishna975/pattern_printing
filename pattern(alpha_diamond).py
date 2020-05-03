n=int(input())
cnt=65
cnt1=97
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(n-i-1,n):
        if i%2==0:
            print(chr(cnt),end=" ")
        else:
            print(chr(cnt1),end=" ")
    if i%2==0:
        cnt=cnt+1
    else:
        cnt1=cnt1+1
    print()
for i in range(1,n):
    for j in range(i):
        print(" ",end="")
    for j in range(i,n):
        if i%2==0:
            print(chr(cnt),end=" ")
        else:
            print(chr(cnt1),end=" ")
    if i%2==0:
        cnt=cnt+1
    else:
        cnt1=cnt1+1
    print()
            