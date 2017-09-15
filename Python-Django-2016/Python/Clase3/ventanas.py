#!/usr/bin/env python
# -*-coding:utf-8-*-
from Tkinter import *  # Importa el módulo

v0 = Tk()  # Tk() Es la ventana principal
v1 = Toplevel(v0)  # Crea una ventana hija


def mostrar(ventana): ventana.deiconify()
def ocultar(ventana): ventana.withdraw()
def ejecutar(f): v0.after(200, f)

v0.config(bg="black")  # Le da color al fondo
v0.geometry("500x500")  # Cambia el tamaño de la ventana

b1 = Button(v0, text="ABRIR VENTANA V1", command=lambda: ejecutar(mostrar(v1)))  # Primer botón
b1.grid(row=1, column=1)  # El botón es cargado
b2 = Button(v0, text="CERRAR VENTANA V1", command=lambda: ejecutar(ocultar(v1)))  # Segundo botón
b2.grid(row=2, column=2)  # El botón es cargado

v1.withdraw()  # Oculta la ventana v1
v0.mainloop()  # Es el evento que llama al inicio de nuestro programa. Siempre lo lleva la ventana principal.
