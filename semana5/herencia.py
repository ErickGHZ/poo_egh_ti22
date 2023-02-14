"""
    Programa 14
    Nombre: Erick Gutierrez Hernandez
    Fecha: 14/02/2023
    Descripción: Se crean 2 clases la cual una herreda sus atributos a otra mediante funciones
"""
class Persona:  #  crea una clase
    __nombre = None  #  variable privada
    __email = None  #  variable privada
    def __init__(self):  #  inicializa la funcion
        print("Persona")  #  imprime esto al iniciar la funcion

class Alumno(Persona):  #  crea una clase
	def __init__(self):  #  inicializa la funcion
		super().__init__()  #  accede a otras clases mediante la funcion super 
		print("Alumno")   #  imprime esto al iniciar la funcion

objeto_persona = Persona()  #  asigna a un variable una clase  
objeto_alumno = Alumno()  #  asigna a un variable una clase

objeto_persona.nombre = "Dejah Thoris"  #  asigna una valor a una variable de una clase
print(objeto_persona.nombre)  #  imprime el valor de una varibale de una clase

objeto_alumno.nombre = "John Carter"  #  asigna una valor a una variable de una clase
print(objeto_alumno.nombre)  #  imprime el valor de una varibale de una clase

objeto_alumno.email = "john@utectulancingo.edu.mx"  #  asigna una valor a una variable de una clase
print(objeto_alumno.email)  #  imprime el valor de una varibale de una clase

print(dir(objeto_persona))  #  muestra los valores de las variables
print(dir(objeto_alumno))  #  muestra los valores de las variables