"""
    Programa 13
    Nombre: Erick Gutierrez Hernandez
    Fecha: 13/02/2023
    Descripción: Crea una clase de un alumno, incializa variables privadas a las cuales se accede despues mediante funciones y por ultimo mediante funciones accede a las variables privadas y las imprime
"""
class Alumno:  #  crea una clase
	__nombre = None  #  variable privada
	__matricula = None  #  variable privada
	__carrera = None  #  variable privada
	
	def __init__(self):  #  inicializa la funcion
		print("Alumno")  #  imprime esto al iniciar la funcion
	
	def setNombre(self, nombre):  #  creea una funcion para poder acceder y darle valor a la variable privada
		self.__nombre = nombre  #  asigna un valor a la variable privada
	def getNombre(self):  #  creea una funcion para poder acceder a una variable privada
		return self.__nombre  #  devuelve el valor que se encuentra en la variable privada
	
	def setMatricula(self, matricula):  #  creea una funcion para poder acceder y darle valor a la variable privada
		self.__matricula = matricula  #  asigna un valor a la variable privada
	def getMatricula(self):  #  creea una funcion para poder acceder a una variable privada
		return self.__matricula  #  devuelve el valor que se encuentra en la variable privada
	
	def setCarrera(self, carrera):  #  creea una funcion para poder acceder y darle valor a la variable privada
		self.__carrera = carrera  #  asigna un valor a la variable privada
	def getCarrera(self):  #  creea una funcion para poder acceder a una variable privada
		return self.__carrera  #  devuelve el valor que se encuentra en la variable privada

erick = Alumno()  #  asigna a un variable una clase
erick.setNombre("Erick")  #  llama a un objeto junto a una funcion ademas da un valor
print(erick.getNombre())  #  imprime un objeto y llama una funcion
erick.setMatricula("1722110095")  #  llama a un objeto junto a una funcion ademas da un valor
print(erick.getMatricula())  #  imprime un objeto y llama una funcion
erick.setCarrera("Ingenieria en Desarrollo Software")  #  llama a un objeto junto a una funcion ademas da un valor
print(erick.getCarrera())  #  imprime un objeto y llama una funcion
