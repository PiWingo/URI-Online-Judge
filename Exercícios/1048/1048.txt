A = float(input())

if ( 400>=A and A>=0):
	Reajuste1 = ((A/100)*15)+ A
	ReajusteG1 = Reajuste1 - A
	print ("Novo salario: %.2f" % Reajuste1)
	print ("Reajuste ganho: %.2f" % ReajusteG1)
	print ("Em percentual: 15 %")
	
elif ( 400>A and 800>=A):
	Reajuste2 = ((A/100)*12)+ A
	ReajusteG2 = Reajuste2 - A
	print ("Novo salario: %.2f" % Reajuste2)
	print ("Reajuste ganho: %.2f" % ReajusteG2)
	print ("Em percentual: 12 %")

elif ( 800>A and 1200>=A):
	Reajuste3 = ((A/100)*10)+ A
	ReajusteG3 = Reajuste3 - A
	print ("Novo salario: %.2f" % Reajuste3)
	print ("Reajuste ganho: %.2f" % ReajusteG3)
	print ("Em percentual: 10 %")

elif ( 1200>A and 2000>=A):
	Reajuste4 = ((A/100)*7)+ A
	ReajusteG4 = Reajuste4 - A
	print ("Novo salario: %.2f" % Reajuste4)
	print ("Reajuste ganho: %.2f" % ReajusteG4)
	print ("Em percentual: 7 %")
	
elif (A>2000):
	Reajuste5 = ((A/100)*4)+ A
	ReajusteG5 = Reajuste5 - A
	print ("Novo salario: %.2f" % Reajuste5)
	print ("Reajuste ganho: %.2f" % ReajusteG5)
	print ("Em percentual: 4 %")