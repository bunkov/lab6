inp = open('input.txt')
out = open('output.txt','w')
s = inp.readline().rstrip()
n, k = map(int, s.split())
a = [0]*k
for i in range (k):
	s = inp.readline().rstrip()
	a[i] = list(map(int, s.split()))
	a[i] = a[i][:3]
profit = [0]*n

for i in range(k):
	profit[a[i][0]-1] -= a[i][2]
	profit[a[i][1]-1] += a[i][2]
print(' '.join(map(str, profit)),file=out)
inp.close()
out.close()