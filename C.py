inp=open('input.txt')
out=open('output.txt','w')
s=inp.readline().rstrip()
n=int(s)
s=inp.readline().rstrip()
a = list(map(int, s.split()))
a = a[:n]
k=None

for i in range(n-1):
	for j in range(i+1, n):
		if a[i] == -a[j] and a[i]<0:
			if k == None or k > j-i:
				k = j-i
if k == None:
	k = 0
print(k,file=out)
inp.close()
out.close()