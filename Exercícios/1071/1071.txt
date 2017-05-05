X = int(input())
Y = int(input())
Soma = 0

for i in range (Y+1,X):
	imp = i%2
	if imp == 1:
		Soma = Soma + i
print (Soma)