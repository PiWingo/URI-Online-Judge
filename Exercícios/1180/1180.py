num = int(input())
X = []
X = list(map(int,input().split()))

menorValor = X[0] 
pos = 0 

for i in range (num):
	if X[i] <= menorValor:
		menorValor = X[i]
		pos = i
	
print ("Menor valor:", menorValor)
print ("Posicao:", pos)