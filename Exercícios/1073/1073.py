N = int(input())
resp = N**2
Zero = 0

for i in range (1,N+1):
	if i%2==0 :
		resp = i**2
		print("%d^2 = %d" %(i,resp))