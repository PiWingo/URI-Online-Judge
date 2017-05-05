num = int(input())
a = 0

for i in range (1000):
	a = a + 1
	if i%num == 0:
		a = 0
		
	print("N[%d] = %a" %(i, a))