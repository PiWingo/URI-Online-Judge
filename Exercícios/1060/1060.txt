cont = 0

def pos(a, c):
    if a>0:
        c = c + 1
    return c



for i in range (6):
    n = float(input())
    cont = pos(n, cont)

print (cont, "valores positivos")