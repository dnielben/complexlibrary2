def suma(a, b):
    return (a[0] + b[0], a[1] + b[1])

def conjugado(c):
    return (c[0], -c[1])

def modulo(c):
    return (c[0]**2 + c[1]**2)**(1/2)

def complexToStr(c):
    return str(c[0]) + " + " + str(c[1]) + "i"
