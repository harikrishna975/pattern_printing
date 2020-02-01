r,c=input().split()
r=int(r)
c=int(c)
s='WELCOME'
pat='.|.'
pl=len(pat)
l=len(s)
for i in range(r//2):
    for j in range(c//2-3*i-1):
        print("-",end="")
    for j in range(2*i+1):
        print(pat,end="")
    for j in range(c//2-3*i-1):
        print("-",end="")
    print()
'''for i in range(r//2,r//2+1):
    for j in range(r):
        print("-",end="")
    for j in s:
        print(j,end="")
    for j in range(r+l,c):
        print("-",end="")
    print()'''
print(s.center(c,"-"))
for i in range(r//2-1,-1,-1):
    for j in range(c//2-3*i-1):
        print("-",end="")
    for j in range(2*i+1):
        print(pat,end="")
    for j in range(c//2-3*i-1):
        print("-",end="")
    print()
