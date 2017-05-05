line = input()
A, B, C = line.split()
A, B, C = [int(A), int(B), float(C)]
line1 = input ()
D, F, G = line1.split()
D, F, G = [int(D), int(F), float(G)]

VALOR = (B*C) + (F*G)

print ("VALOR A PAGAR: R$ %.2f" % VALOR)