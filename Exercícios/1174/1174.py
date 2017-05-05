A = []
valorVet = [] 
posVet = []
pos = 0
valor = 0

for i in range (100):
	A.append(float(input()))
	
	if A[i] <= 10:
		valor = A[i]
		valorVet.append(valor)
		pos = i
		posVet.append(pos)

for i in range (len(valorVet)):
	print("A[%d] = %.1f" %(posVet[i], valorVet[i]))