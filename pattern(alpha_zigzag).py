n=int(input())
for i in range(n):
    c=65
    d=90
    if i%2==0:
        for j in range(n-i):
            if j%2==0:
                print(chr(c),end="")
                c=c+1
            else:
                print(" ",end="")
    else:
        for j in range(n-i):
            if j%2!=0:
                print(chr(d),end="")
                d=d-1
            else:
                print(" ",end="")
        
    print()
for i in range(1,n):
    c=65
    d=90
    if i%2==0:
        for j in range(i+1):
            if j%2==0:
                print(chr(c),end="")
                c=c+1
            else:
                print(" ",end="")
    else:
        for j in range(i+1):
            if j%2!=0:
                print(chr(d),end="")
                d=d-1
            else:
                print(" ",end="")
        
    print()
    