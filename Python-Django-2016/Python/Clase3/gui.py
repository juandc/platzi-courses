import Tkinter, tkSimpleDialog

root = Tkinter.Tk()
root.withdraw()

numero = tkSimpleDialog.askinteger("Entero", "Introduce un entero")
print numero
texto = tkSimpleDialog.askstring("String", "Introduce un String")
print texto
