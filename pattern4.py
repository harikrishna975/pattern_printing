n=int(input())
for i in range(n):
    cnt=n
    for j in range(i):
        print(cnt,end="")
        cnt=cnt-1
    for j in range(i,n):
        print(cnt,end="")
    print()
    
#other pattern of same type  
#n=int(input())
#for i in range(n,0,-1):
#    cnt=i
#    for j in range(n-i):
#        print(cnt,end="")
#        cnt=cnt+1
#    for j in range(n-i,n):
#        print(n,end="")
#    print()