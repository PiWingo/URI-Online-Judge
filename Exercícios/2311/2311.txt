n = int(input())

def soma(nota, res):
    return nota + res
    
for i in range (n):
    nome = input()
    grau =float(input())
    notas = list(map(float,input().split()))
    notas.sort()
    resultado = 0
    for j in range (1, len(notas)-1):
        resultado = soma(notas[j], resultado)
    resultado = resultado * grau
    print("%s %.2f" %(nome, resultado))