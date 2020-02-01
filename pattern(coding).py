n=int(input())
cnt=1
strings=[]
for i in range(n):
	strings.append('')

for i in range(n):
	strings[i]+=("-"*2)*i
	for j in range(i,n):
		strings[i]+=(str(cnt)+"*")
		cnt+=1

for i in range(n-1,-1,-1):
	for j in range(i,n):
		strings[i]+=(str(cnt)+"*")
		cnt+=1

for i in range(n):
	strings[i]=strings[i][:-1]

for i in range(n):
	print(strings[i])