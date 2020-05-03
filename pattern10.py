n=int(input())
b=[]
cnt=1
cnt1=n
for i in range(n):
    a=[]
    c=[]
    if i%2==0:
        for j in range(n):
            a.append(cnt)
        cnt=cnt+1
        b.append(a)
    else:
        for j in range(n):
            c.append(cnt1)
        cnt1=cnt1-1
        b.append(c)
for i in b:
    for j in i:
        print(j,end="")
    print()