#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Juego piedra papel tijera.... para curso python/django de platzi
#Usa varios de los elementos enseñados en clases:
#   *Variables
#   *Operador para disminuir en uno una variable entera
#   *Diccionarios
#   *Tuplas
#   *Bucles while
#   *Condicionales if-elif-else
#   *Operadores in y not in
#   *Operadores lógicos y de comparación
#   *Importar de una librería
#   *Entrada y Salida estándar
#   *Uso de formatos para la salida
#   *Uso de comentarios
#   *Uso de 4 espacios para la indentación de los bloques

#PYTHON 3

from random import choice

opciones = { 'piedra': ("tijera", "lagarto"),
             'papel':  ("piedra", "spock"), 
             'tijera': ("papel", "lagarto"), 
             'lagarto': ("spock", "papel"),
             'spock': ("piedra", "tijera")
           }

print("PIEDRA PAPEL TIJERA LAGARTO SPOCK\nLa máquina te desafía a un duelo al mejor de 5. ¿Estás listo?\n")

#vidas del jugador y enemigo
jugador, villano = 3, 3

#Bucle que se mantiene corriendo hasta que uno de los jugadores tenga vida igual a cero

while jugador and villano :
    
    #elecciones
    eleccion_jugador = input("\nEscribe tu opción(piedra-papel-tijera-lagarto-spock): ")
    
    if eleccion_jugador not in opciones.keys():
        print("Hey!, ingresaste una opción inválida.")
        print("Recuerda, la palabra debe estar escrita tal como aparece en los paréntesis")
        continue #finaliza esta vuelta del bucle aquí y inicia una nueva.
    
    eleccion_villano = choice(tuple(opciones.keys()))
    
    print("\nElegiste %s, y la máquina %s" %(eleccion_jugador, eleccion_villano) )
    
    if eleccion_villano in opciones[eleccion_jugador]:
        print("Ganaste :_(!")
        villano -= 1
    elif eleccion_jugador == eleccion_villano:
        print("Esto es extraño, de algún modo me leiste la cpu y elegimos lo mismo :/")
    else:
        print("Perdiste >:D!")
        jugador -= 1
    print("Te quedan %d vida(s)" %(jugador))
    print("Vidas de la máquina: %d" %(villano))
    
if villano == 0:
    print("\nSHIT! Me has ganado, seguro has usado algún hack...")
else:
    print("\nJajajaja! Perdiste! No te preocupes, es normal, las máquinas somos mejores.")
