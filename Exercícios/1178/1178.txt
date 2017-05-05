def calcMet(N):
    N.append(float(input()))
    for i in range (0,100):
        temp = N[i]
        cont = temp
        cont = cont/2
        N.append(cont)
    return N

def printT(N):
    for i in range (100):
        print("N[%d] = %.4f" %(i,N[i]))
    
def main():
    N = []
    Ni = calcMet(N)
    printT(Ni)
    
main()