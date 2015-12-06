inp = open('input.txt')
out = open('output.txt','w')
s = inp.readline().rstrip()
k, n = map(int, s.split())
a = [0]*k
for i in range (k):
	s = inp.readline().rstrip()
	a[i] = list(map(int, s.split()))
	a[i] = a[i][:n]
min = [None]*n

for i in range(n):
	for j in range(k):
		if min[i] == None or min[i] > a[j][i]:
			min[i] = a[j][i]
print(' '.join(map(str, min)),file=out)
inp.close()
out.close()