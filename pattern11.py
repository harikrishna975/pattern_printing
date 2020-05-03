n=int(input())
for i in range(1,n+1):
    for j in range(2*n-2*i):
        print(" ",end="")
    for j in range(2*i-1):
        print("**",end="")
    print()

#other pattern with same logic......

n=int(input())
for i in range(1,n+1):
    for j in range(2*n-2*i):
        print(" ",end="")
    for j in range(2*i-1):
        print("**",end="")
    print()
    for j in range(2*n-2*i):
        print(" ",end="")
    for j in range(2*i-1):
        print("**",end="")
    print()