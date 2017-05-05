X = []

for i in range(10):
	X.append(int(input()))
	if X[i] <= 0:
		X[i] = 1

for i in range (10):
	print ("X[%d] =" %i, X[i])