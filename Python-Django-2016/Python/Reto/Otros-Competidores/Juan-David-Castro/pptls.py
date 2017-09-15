#!/usr/bin/env python
#  -*-coding:utf-8-*-
import time
from time import sleep
import random
depo, sus, tab, user_puntos, pc_puntos = ["piedra", "papel", "tijera", "lagarto", "spock"], "-" * 35, " " * 4, 0, 0
print """Hola! Bienvenido al juego Piedra Papel Tijera Lagarto Spock!\nEstas son las reglas:\n Las tijeras cortan el papel\n El papel cubre a la piedra\n La piedra aplasta al lagarto\n El lagarto envenena a Spock\n Spock destroza las tijeras\n Las tijeras decapitan al lagarto\n El lagarto se come el papel\n El papel refuta a Spock\n Spock vaporiza la piedra\n Y como es habitual... la piedra aplasta las tijeras.\nRecuerda que si escribes algun valor incorrecto pierdes un punto!\nEl primero en llegar a 10 puntos gana!
"""
sleep(2)
print "\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
sleep(1)
while (pc_puntos < 10 and user_puntos < 10):
    tu = raw_input("Que eliges? Piedra, papel, tijera, lagarto o Spock:\n('marcador' para ver los puntos)(Control + C para salir)\n\n(Escribe en minusculas)" + tab)
    pc = random.choice(depo)
    sleep(0.5)
    if tu in depo:
        print (("\nElegiste {}\nComputadora eligio {}\nAsi que:").format(tu, pc))
    elif tu not in depo and tu != "marcador":
        print "\nEscribe un valor correcto!\nPierdes un punto"
    if tu == pc:
        print '\n Es un Empate...\n'
    elif tu == 'piedra' and pc == 'tijera':
        user_puntos = user_puntos + 1
        print "\n Ganaste! Como es habitual... la piedra aplasta las tijeras.\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif tu == 'papel' and pc == 'piedra':
        user_puntos = user_puntos + 1
        print "\n Ganaste! Papel cubre a la piedra\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif tu == 'tijera' and pc == 'papel':
        user_puntos = user_puntos + 1
        print "\n Ganaste! Tijeras cortan el papel\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif tu == 'piedra' and pc == 'lagarto':
        user_puntos = user_puntos + 1
        print "\n Ganaste! La piedra aplasta al lagarto\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif tu == 'lagarto' and pc == 'spock':
        user_puntos = user_puntos + 1
        print "\n Ganaste! Lagarto envenena Spock\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif tu == 'spock' and pc == 'tijera':
        user_puntos = user_puntos + 1
        print "\n Ganaste! Spock destroza las tijeras\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif tu == 'tijera' and pc == 'lagarto':
        user_puntos = user_puntos + 1
        print "\n Ganaste! Las tijeras decapitan al lagarto\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif tu == 'lagarto' and pc == 'papel':
        user_puntos = user_puntos + 1
        print "\n Ganaste! El lagarto se come el papel\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif tu == 'papel' and pc == 'spock':
        user_puntos = user_puntos + 1
        print "\n Ganaste! El papel refuta a Spock\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif tu == 'spock' and pc == 'piedra':
        user_puntos = user_puntos + 1
        print "\n Ganaste! Spock vaporiza la piedra\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif tu == "marcador" and pc == pc:
        print "\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
        sleep(0.5)
    else:
        pc_puntos = pc_puntos + 1
        print "\n Lo siento, perdiste: {} le gana a {} \n{}\nPierdes un punto...\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(pc, tu, sus, user_puntos, pc_puntos)
print "Acabo el juego...\nEl ganador es...\n "
sleep(2)
if pc_puntos == 10:
    print "La computadora!\nGracias por jugar!"
else:
    print "Tu!\nGracias por jugar!\nVuelve Pronto!"
