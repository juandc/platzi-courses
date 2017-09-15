#!/usr/bin/env python
#  -*-coding:utf-8-*-
import random
import sys
from Tkinter import *
import time
from time import sleep
from PIL import Image, ImageTk

tab, user_puntos, pc_puntos = " " * 4, 0, 0

opciones = """
piedra\npapel\ntijera\nagua\nfuego\naire\nesponja """

newdict = {
    "piedra":  ("esponja", "tijera", "fuego"),
    "papel":   ("piedra",  "aire",   "agua"),
    "tijera":  ("esponja", "papel",  "aire"),
    "agua":    ("tijera",  "piedra", "fuego"),
    "fuego":   ("esponja", "tijera", "papel"),
    "aire":    ("tijera",  "agua",   "fuego"),
    "esponja": ("papel",   "aire",   "agua")
}

user = raw_input("Hola! Como te llamas?" + tab)

print "\nHola " + user + "!"

sleep(0.5)

print """\nEstos son unos opciones para que disfrutes mejor del juego:\n
Escribe:
    'opciones' para ver las opciones
    'marcador' para ver los puntos
    'reglas' para ver las reglas oficiales del juego
Y Oprime:
    Control + C para salir\n\n
"""

raw_input("Cuando estes listo me dices ok!" + tab)

sleep(2)

while (pc_puntos < 10 and user_puntos < 10):
    sleep(1)
    
    user_elec = raw_input("\n\nUn, dos, Tres! Piedra papel tijera agua fuego aire esponja!\n\n" + user + ":" + tab).lower()
    pc = random.choice(newdict.keys())
    
    sleep(0.2)

    if user_elec == "marcador":
        print "\n" + user + " lleva: " + str(user_puntos) + " puntos\nY la pc lleva " + str(pc_puntos) + " puntos"
    elif user_elec == 'opciones':
        print opciones
    elif user_elec == 'reglas':
        ventana=Tk()
        ventana.geometry("400x400+0+0")
        ventana.config(bg="#1e9981")
        ventana.title("Imagen de las reglas del juego")
        image = Image.open("image.gif")
        photo = ImageTk.PhotoImage(image)
        label = Label(image=photo)
        label.image = photo
        label.pack()
        ventana.mainloop()
    elif not user_elec in newdict.keys():
        print "Opcion no valida " + user + "... Intentalo de nuevo!"
    elif pc in newdict[user_elec]:
        user_puntos += 1
        print "PC:" + tab + pc
        sleep(1)
        print "\nFelicitaciones " + user + ", ganaste un punto"
    elif user_elec == pc:
        print "PC:" + tab + pc
        sleep(1)
        print "Es un empate!"
    else:
        pc_puntos += 1
        print "PC:" + tab + pc
        sleep(1)
        print "\nLo siento, perdiste"

sleep(1)
if pc_puntos == 10:
    print "\nLa computadora te ha ganado " + user + "\nLo lamento..."
else:
    print "\nLe has ganado a la computadora " + user + "!\nTe felicito"
