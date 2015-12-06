n = int(input())
a = list(map(int, input().split()))
a = a[:n]
for i in range(n-1):
	for j in range(i+1, n):
		if a[i] == a[j]:
			print(a[i])