jNum = 8
for i in range (0,10):
	for j in range (0,3):
		if i%2 == 1:
			jNum = jNum - 1
			print ("I=%d J=%d" % (i,jNum))
	jNum = 8