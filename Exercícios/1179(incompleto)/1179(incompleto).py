Vet = []
par = []
impar = []

for i in range (15):
	Vet.append(int(input()))
	
	if Vet[i]%2 == 0:
		par.append(Vet[i])
		print(par)
		if len(par) >= 5:
			for j in range(5):
				print ("par[%d] = %d" %(j, par[j]))
			par =[]
				
	elif Vet[i]%2 == 1:
		impar.append(Vet[i])
		if len(impar) >= 5:
			for j in range (5):
				print ("impar[%d] = %d" %(j, impar[j]))
			impar = []
					

for i in range (len(par)):
	print ("par[%d] = %d" %(i, par[i]))
		
for i in range (len(impar)):
	print ("impar[%d] = %d" %(i, impar[i]))