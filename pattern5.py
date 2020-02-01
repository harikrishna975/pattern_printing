n=int(input())
x=64
for i in range(n):
    x=x+1
    caps=x
    for j in range(i):
        print(" ",end="")
    for j in range(n-i):
        print(chr(caps),end=" ")
        caps=caps+1
    print()
    
#other format of same type
n=int(input())
a=['A']
cnt=65
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    print(''.join(a))
    cnt=cnt+1
    a.insert(0,chr(cnt))
    a.append(chr(cnt))

#other format of same type
n=int(input())
a=[]
for i in range(n):
    cnt=65
    for j in range(n-i):
        print(" ",end="")
    for j in range(n-i,n+i+1):
        if j<=n:
            print(chr(cnt),end="")
            cnt=cnt+1
        else:
            print(chr(cnt),end="")
            cnt=cnt-1
    print()
        
    