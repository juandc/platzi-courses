# -*-coding:utf-8-*-
import Tkinter, tkSimpleDialog, tkMessageBox
from time import sleep
import random

def ingreso():
	u = tkSimpleDialog.askinteger("Opcion","Que opcion deseas?:\n1. Piedra\n2. Papel\n3. Tijera\n4. Spock\n5. Lagarto\n0. Salir")
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
		sleep(0.5)
		tkMessageBox.showinfo("PC Juega","Ver Resultado!")
		u= "Elegiste: %s" % opc[usuario]
		p= "La computadora Eligió: %s" %opc[pc]
		tkMessageBox.showinfo("Resultado",u+"\n"+p+"\n"+logica(pc,usuario))
		op=tkSimpleDialog.askinteger("Seguir","0: Salir\nOtro numero: Seguir Jugando")
	tkMessageBox.showinfo("Exit","Gracias por Jugar")

#Declaracion de opciones y llamada al juego
opc = {1:"Piedra",2:"Papel",3:"Tijera",4:"Spock",5:"Lagarto"}
root = Tkinter.Tk()
root.withdraw()
juego(opc)
