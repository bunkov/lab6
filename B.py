inp=open('input.txt')
out=open('output.txt','w')
s=inp.readline().rstrip()
n=int(s)
s=inp.readline().rstrip()
a = list(map(int, s.split()))
a = a[:n]
bank=credit=total=0
for i in range(n):
	if a[i] == 5:
		bank+=1
	else:
		credit+=(a[i]-5)//5
		while bank > 0 and credit > 0:
			credit -= 1
			bank -= 1
	total += credit
	credit = 0
	print(bank,total)
print(total)
print(total,file=out)
inp.close()
out.close()