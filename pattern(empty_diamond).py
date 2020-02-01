#printing the empty diamond symbol
n=int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    for j in range(n-i,n+i):
        print(" ",end=" ")
    for j in range(n+i,2*n):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i+1,2*n-i-1):
        print(" ",end=" ")
    for j in range(n-i-1,n):
        print("*",end=" ")
    print()
    
#another pattern solution
#reverse of the above code

n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i+1,2*n-i-1):
        print(" ",end=" ")
    for j in range(n-i-1,n):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    for j in range(n-i,n+i):
        print(" ",end=" ")
    for j in range(n+i,2*n):
        print("*",end=" ")
    print()