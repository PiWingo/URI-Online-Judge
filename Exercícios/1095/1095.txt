for i in range (1,14):
	if i == 1 :
		J = i * 60
		I = i
		print ( "I=", i, "J=", J)
		
	else :
		I = I + 3
		J = J - 5
		print ( "I=", i, "J=", J)