#!/usr/bin/env python
#  -*-coding:utf-8-*-
import time
from time import sleep
import random

sus = "-" * 35
depo = ["piedra", "papel", "tijera"]
while True:
    x = raw_input("Que eliges? Piedra, papel, o tijera: ")
    if x not in depo:
        print("No hagas trampa!!!")
        continue

    pc = random.choice(depo)
    sleep(0.5)
    print (("Computadora eligio {}.").format(pc))
    if x == pc:
        print '\n Empate.'
    elif x == 'piedra' and pc == 'tijera':
        print "\n Ganaste"
    elif x == 'papel' and pc == 'piedra':
            print "\n Ganaste"
    elif x == 'tijera' and pc == 'papel':
        print "\n Ganaste"
    else:
        print "\n Perdiste. {} gana {} \n{}".format(pc,x,sus)
