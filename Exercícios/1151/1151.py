n = int(input())

a = 1
b = 1

for i in range (n):
    if i == 0:
        print ("0", end=" ")
    else:
        x=a
        a=b
        b=b+x
        if i ==n-1:
            print (x)
        else:
            print (x, end=" ")