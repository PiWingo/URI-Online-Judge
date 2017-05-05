def tret(a,c):
    resp = (a*c)/2
    return resp
    
def circ(c):
    resp = 3.14159*c*c
    return resp
    
def trap(a,b,c):
    resp = ((a + b)*c)/2
    return resp
    
def quad(b):
    resp = b*b
    return resp
    
def ret(a,b):
    resp = a*b
    return resp
    
a,b,c = map(float, input().split())

print ("TRIANGULO: %.3f" %tret(a,c))
print ("CIRCULO: %.3f" %circ(c))
print ("TRAPEZIO: %.3f" %trap(a,b,c))
print ("QUADRADO: %.3f" %quad(b))
print ("RETANGULO: %.3f" %ret(a,b))