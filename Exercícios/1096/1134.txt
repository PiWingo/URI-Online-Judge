a = 0
g = 0
d = 0

while True:
	N = int(input())
	if N == 1 :
		a +=1
	elif N == 2 :
		g +=1
	elif N == 3 :
		d +=1
	elif N == 4 :
		break
print("MUITO OBRIGADO")
print("Alcool: ", a)
print("Gasolina: ", g)
print("Diesel: ", d)