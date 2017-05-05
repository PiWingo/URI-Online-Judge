X = []
 
for i in range (20):
	X.append(int(input()))

for i in range(10):
	temp = X[19-i]
	X[19-i] = X[i]
	X[i] = temp
	
for i in range (20):
	print ("N[%d] = %d" %(i, X[i]))