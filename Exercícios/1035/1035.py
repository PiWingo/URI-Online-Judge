line = input()
A, B, C, D = line.split()
A, B, C, D = [int(A),int(B),int(C),int(D)]

somaCD = C+D
somaAB = A+B
Apar = A%2
if ( B>C and D>A and somaCD>somaAB and C>=0 and D>=0 and Apar==0):
	print("Valores aceitos")
else:
	print("Valores nao aceitos")
