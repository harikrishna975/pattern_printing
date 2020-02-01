#printing elements in spiral pattern

n=int(input())
r=n
c=n
mat=[]
#for n*n matrix without input
'''
a=[]
cnt=1
for i in range(n):
    b=[]
    for j in range(n):
        b.append(cnt)
        cnt=cnt+1
    a.append(b)
    '''
# for taking input from user
    
for i in range(n):
    a=list(map(int,input().split()))
    mat.append(a)
#print(mat)
final=n*n
cnt=1
def spiral(r,c,mat):
    k=0
    l=0
    while(k<r and l<c):
        for i in range(l,c):
            print(mat[k][i],end=" ")
        k=k+1
        
        for i in range(k,r):
            print(mat[i][c-1],end=" ")
        c=c-1
        
        if k<r:
            for i in range(c-1,l-1,-1):
                print(mat[r-1][i],end=" ")    
            r=r-1

        if l<c:
            for i in range(r-1,k-1,-1):
                print(mat[i][l],end=" ")
            l=l+1

spiral(r,c,mat)
        
        