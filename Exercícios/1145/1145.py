Col, Max = map(int, input().split())

for i in range (1,Max + 1) :
	if ( i % Col == 0 ) :
		print (i)
	else :
		print(i, end =" ")