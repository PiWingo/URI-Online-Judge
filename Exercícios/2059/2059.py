p, j1, j2, r, a = map(int, input().split())

soma = (j1+j2)%2

## soma par
if p == 0 and soma == 0 and r == 0 and a == 0 :
	print ("Jogador 2 ganha!")
	
if p == 0 and soma == 0 and r == 0 and a == 1 :
	print ("Jogador 1 ganha!")

if p == 0 and soma == 0 and r == 1 and a == 0 :
	print ("Jogador 1 ganha!")

if p == 0 and soma == 0 and r == 1 and a == 1 :
	print ("Jogador 2 ganha!")

####soma impar

if p == 0 and soma == 1 and r == 0 and a == 0 :
	print ("Jogador 1 ganha!")
	
if p == 0 and soma == 1 and r == 0 and a == 1 :
	print ("Jogador 1 ganha!")
	
if p == 0 and soma == 1 and r == 1 and a == 0 :
	print ("Jogador 1 ganha!")

if p == 0 and soma == 1 and r == 1 and a == 1 :
	print ("Jogador 2 ganha!")
	
###jogador par soma par

if p == 1 and soma == 0 and r == 0 and a == 0 :
	print ("Jogador 1 ganha!")

if p == 1 and soma == 0 and r == 0 and a == 1 :
	print ("Jogador 1 ganha!")
	
if p == 1 and soma == 0 and r == 1 and a == 0 :
	print ("Jogador 1 ganha!")
	
if p == 1 and soma == 0 and r == 1 and a == 1 :
	print ("Jogador 2 ganha!")

### jogador par soma impar

if p == 1 and soma == 1 and r == 0 and a == 0 :
	print ("Jogador 2 ganha!")
	
if p == 1 and soma == 1 and r == 0 and a == 1 :
	print ("Jogador 1 ganha!")
	
if p == 1 and soma == 1 and r == 1 and a == 0 :
	print ("Jogador 1 ganha!")
	
if p == 1 and soma == 1 and r == 1 and a == 1 :
	print ("Jogador 2 ganha!")