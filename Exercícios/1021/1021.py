Din = float(input())

Nota100 = Din/100
Nota50 = Din%100/50
Nota20 = Din%100%50/20
Nota10 = Din%100%50%20/10
Nota5 = Din%100%50%20%10/5
Nota2 = Din%100%50%20%10%5/2
Moeda1 = Din%100%50%20%10%5%2/1
Moeda_50 = Din%100%50%20%10%5%2%1/0.5
Moeda_25 = Din%100%50%20%10%5%2%1%0.5/0.25
Moeda_10 = Din%100%50%20%10%5%2%1%0.5%0.25/0.1
Moeda_05 = Din%100%50%20%10%5%2%1%0.5%0.25%0.1/0.05
Moeda_01 = Din%100%50%20%10%5%2%1%0.5%0.25%0.1%0.05/0.01
MoedaCerto_01 = Moeda_01 + 0.000000001

print ("NOTAS:")
print ("%i nota(s) de R$ 100.00" %Nota100)
print ("%i nota(s) de R$ 50.00" %Nota50)
print ("%i nota(s) de R$ 20.00" %Nota20)
print ("%i nota(s) de R$ 10.00" %Nota10)
print ("%i nota(s) de R$ 5.00" %Nota5)
print ("%i nota(s) de R$ 2.00" %Nota2)
print ("MOEDAS:")
print ("%i moeda(s) de R$ 1.00" %Moeda1)
print ("%i moeda(s) de R$ 0.50" %Moeda_50)
print ("%i moeda(s) de R$ 0.25" %Moeda_25)
print ("%i moeda(s) de R$ 0.10" %Moeda_10)
print ("%i moeda(s) de R$ 0.05" %Moeda_05)
print ("%i moeda(s) de R$ 0.01" %MoedaCerto_01)
