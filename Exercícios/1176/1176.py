n = int(input())

vetPed = []
vetFib = []
a = 0
b = 1

for i in range (n):
	vetPed.append(int(input()))
	
for i in range (61):
	temp = a 
	a = b 
	b = b + temp
	vetFib.append(temp)
	
for i in range (n):
	print("Fib(%d) = %d" %(vetPed[i],vetFib[vetPed[i]]))