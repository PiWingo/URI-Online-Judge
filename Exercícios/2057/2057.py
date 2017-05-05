S, T, F = map (int,input().split())
Hora = S + T + F 

if Hora == 24 :
	print ("0")
elif Hora > 24 or Hora < 0 :
	nHora = Hora % 24
	print (nHora)
else :
	print (Hora)