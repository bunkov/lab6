inp=open('input.txt')
out=open('output.txt','w')
s=inp.readline().rstrip()
n=int(s)
s=inp.readline().rstrip()
a = list(map(int, s.split()))
a = a[:n]

a.sort()
for i in range(n):
	if a[i] == a[i+1]:
		print(a[i],file=out)
		break
inp.close()
out.close()