n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("H",end="")
    print()
for i in range(n+1):
    for j in range(n//2):
        print(" ",end="")
    for j  in range(n):
        print("H",end="")
    for j in range(n*3):
        print(" ",end="")
    for j in range(n):
        print("H",end="")
    print()
for i in range((n//2+1)):
    for j in range(n//2):
        print(" ",end="")
    for j in range(n*5):
        print("H",end="")
    print()  
for i in range(n+1):
    for j in range(n//2):
        print(" ",end="")
    for j  in range(n):
        print("H",end="")
    for j in range(n*3):
        print(" ",end="")
    for j in range(n):
        print("H",end="")
    print()
for i in range(n-1,-1,-1):
    for j in range(5*n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("H",end="")
    print()


