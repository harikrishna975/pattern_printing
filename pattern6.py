n=int(input())
a=[]
for i in range(n):
    cnt=65
    for j in range(i+1):
        a.append(chr(cnt))
        cnt=cnt+1
    print(''.join(a))
    a.clear()
    
#other pattern of same type
    
n=int(input())
a=[]
for i in range(n):
    cnt=65
    for j in range(i+1):
        a.insert(0,chr(cnt))
        cnt=cnt+1
    print(''.join(a))
    a.clear()


#other pattern of same type
n=int(input())
caps=65
small=97
for i in range(n):
    for j in range(i+1):
        if j%2==0:
            print(chr(caps),end="")
        else:
            print(chr(small),end="")
    caps=caps+1
    small=small+1
    print()