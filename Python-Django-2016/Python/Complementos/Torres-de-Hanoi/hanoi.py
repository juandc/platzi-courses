"""
Inicio | fin | aux
   1  |  3  |  2
   3  |  1  |  2
   1  |  2  |  3
   2  |  1  |  3
   2  |  3  |  1
   3  |  2  |  1

6 - inicial - final
"""

def hanoi(numero_discos, inicio = 1, fin = 3):
    if numero_discos :
        hanoi(numero_discos-1, inicio, 6 - inicio - fin) # De la actial a la auxiliar
        print "Mueve el disco %d de la torre %d a la torre %d" % (numero_discos, inicio, fin)
        hanoi(numero_discos - 1, 6 - inicio - fin, fin) # De la auxiliar a la final

numero = int(raw_input('Selecciona el nivel de dificultad:\n\nNumero: '))
hanoi(numero_discos=numero)
