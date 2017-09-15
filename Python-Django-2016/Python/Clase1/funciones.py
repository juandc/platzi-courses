"""a = "Hola"
b = "Mundo"
c = "!"
def mi_funcion():
    return "Esta es mi primera funcion"

def mi_funcion_2():
    print "Esta es otro tipo de funcion"
    
resultado = mi_funcion()
print resultado
mi_funcion_2()

def suma(a1,b1):
    return a1 + b1

resultado_2 = suma(10,5)
print resultado_2
"""
#print resultado_2



def saludo(nombre):
    return "Hola %s" % nombre

#print saludo("Fabian")
#print saludo("Franco")
#print saludo("Freddier")
#print saludo("Juan Pablo")
#print saludo("Beco")

ingreso = raw_input("Como te llamas?")
print saludo(ingreso)
