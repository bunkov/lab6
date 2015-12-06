inp=open('input.txt')
out=open('output.txt','w')
s=inp.readline().rstrip()
n=int(s)
s=inp.readline().rstrip()
a = list(map(int, s.split()))
a = a[:n]
k=0

for i in range(n):
	if a[i] == 5:
		k-=1
	else:
		k+=(a[i]-5)//5
print(k,file=out)
inp.close()
out.close()