"""
    Este es un programa de inputs de python por 
    
    __________.__          __         .__ 
    \______   \  | _____ _/  |________|__|
     |     ___/  | \__  \\   __\___   /  |
     |    |   |  |__/ __ \|  |  /    /|  |
     |____|   |____(____  /__| /_____ \__|
                        \/           \/
                        
     Trabaje 15 horas aqui. 19 de enero de 2016
"""


nombre = raw_input("Cual es tu nombre?")
edad = raw_input("Cual es tu edad?")
altura = raw_input("Cual es tu altura?")
peso = raw_input("Cual es tu peso?")
carrera = raw_input("Que estudias?")


print """
         Hola %s, tienes %s, %s m, altura y %s kg.
         Y estudias la carrera de %s.
         Mucho gusto en conocerte
         
         """ % (nombre,edad,altura,peso,carrera)
