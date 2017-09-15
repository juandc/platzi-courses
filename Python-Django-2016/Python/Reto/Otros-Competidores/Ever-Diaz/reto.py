# -*-coding:utf-8-*-
from time import sleep
import random

def ingreso():
	u = int(raw_input("""Que opcion deseas?:
				1. Piedra
				2. Papel
				3. Tijera
				4. Spock
				5. Lagarto
				0. Salir
				->"""))
	return u

def logica(pc,usuario):
	res=""
	if usuario == pc:
		res = "Empate!"
	elif usuario == 1 and pc == 3:
		res = "Piedra aplasta Tijera, Ganaste!"
	elif usuario == 1 and pc == 5:
		res = "Piedra aplasta Lagarto, Ganaste!"
	elif usuario == 2 and pc == 1:
		res = "Papel tapa piedra, Ganaste!"
	elif usuario == 2 and pc == 4:
		res = "Papel desautoriza Spock, Ganaste!"
	elif usuario == 3 and pc == 2:
		res = "Tijera corta Papel, Ganaste!"
	elif usuario == 3 and pc == 5:
		res = "Tijera decapita lagarto, Ganaste!"
	elif usuario == 4 and pc == 1:
		res = "Spock vaporiza piedra, Ganaste!"
	elif usuario == 4 and pc == 3:
		res = "Spock rompe tijeras, Ganaste!"
	elif usuario == 5 and pc == 2:
		res = "Lagarto devora papel, Ganaste!"
	elif usuario == 5 and pc == 4:
		res = "Lagarto envenena Spock, Ganaste!"
	else:
		res = "Perdiste! :("

	return res
	
def juego(opc):
	op=1
	while op!=0:
		usuario = ingreso()
		if usuario == 0:
			op = 0
			continue
		elif usuario not in opc.keys():
			print "Trampa!"
			continue
		pc = random.choice(opc.keys())
		print "Jugando"
		sleep(0.5)
		print "Elegiste: %s" % opc[usuario]
		print "La computadora Eligió: %s" %opc[pc]
		print logica(pc,usuario)

		op=int(raw_input("""
					  0: Salir 
					  Otro numero: Seguir Jugando
					  ->"""))

	print "Gracias por Jugar..."

#Declaracion de opciones y llamada al juego
opc = {1:"Piedra",2:"Papel",3:"Tijera",4:"Spock",5:"Lagarto"}
juego(opc)
