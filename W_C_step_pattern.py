n,a=input().split()
n=int(n)
# print(n,a)
cnt=0
l=len(a)
# print(len(a))
for i in range(l):
    for j in range(n):
        if cnt==l:
            break
        else:
            print("*"*j,end="")
            print(a[cnt])
            cnt=cnt+1
    for j in range(n-2,0,-1):
        if cnt==l:
            break
        else:
            print("*"*j,end="")
            print(a[cnt])
            cnt=cnt+1

        