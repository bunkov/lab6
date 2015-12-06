inp=open('input.txt')
out=open('output.txt','w')
s=inp.readline().rstrip()
n=int(s)
s=inp.readline().rstrip()
a = list(map(int, s.split()))
a = a[:n]

for i in range(n-1):
	for j in range(i+1, n):
		if a[i] == a[j]:
			print(a[i],file=out)
inp.close()
out.close()