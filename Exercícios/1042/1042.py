A, B, C = map(int, input().split())

tempA = A
tempB = B
tempC = C

if A > B :
	temp = A
	A = B
	B = temp
	
if B > C :
	temp = B
	B = C
	C = temp
	
if A > B :
	temp = A
	A = B
	B = temp

print (A)
print (B)
print (C)
print ("")
print (tempA)
print (tempB)
print (tempC)