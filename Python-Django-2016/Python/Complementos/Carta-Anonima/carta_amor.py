#!/usr/bin/env python
# -*- coding: latin-1 -*-

import string

def carta_anonima(revistas, nota):
    catalogo = dict()

    for letra in revistas:
        if not letra in catalogo.keys():
            catalogo[letra] = 1
        else:
            catalogo[letra] = catalogo[letra] + 1

    # Para ver las letras disponibles activar el print de abajo
    # print "%s" % catalogo

    for letra in nota:
        if letra in catalogo.keys():
            if catalogo[letra] >= 1:
                catalogo[letra] = catalogo[letra] - 1
            else:
                return "No hay %s disponibles" % letra
        else:
            return "No existe la letra %s en la revista" % letra
    return "Texto completo"



if __name__ == "__main__":
    revistas = raw_input("Que texto base engañoso quieres? ")

    revistas_limpio = revistas.translate(None, string.whitespace)
    carta = raw_input("Cual es tu mensaje de amor? ")
    carta_limpio = carta.translate(None, string.whitespace)

    print carta_anonima(revistas_limpio, carta_limpio)
