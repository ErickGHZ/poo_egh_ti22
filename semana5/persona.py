"""
    Programa 12
    Nombre: Erick Gutierrez Hernandez
    Fecha: 13/02/2023
    Descripción: Crea una clase de una persona, incializa variables privadas a las cuales se accede despues mediante funciones y por ultimo, mediante funciones accede a las variables privadas y las imprime
"""
class Persona:  #  crea una clase
	__nombre = None  #  __nombre variable privada
	__email = None  #  variable privada

	def __init__(self):  #  inicializa la funcion
		print("Persona")  #  imprime esto al iniciar la funcion

	def setNombre(self, nombre):  #  creea una funcion para poder acceder y darle valor a la variable privada
		self.__nombre = nombre  #  asigna un valor a la variable privada
	def getNombre(self):  #  creea una funcion para poder acceder a una variable privada y poder obtener su valor
		return self.__nombre  #  devuelve el valor de la variable privada

	def setEmail(self, email):  #  creea una funcion para poder acceder y darle valor a la variable privada
		self.__email = email  #  asigna un valor a la variable privada
	def getEmail(self):  #  creea una funcion para poder acceder a una variable privada y poder obtener su valor
		return self.__email  #  devuelve el valor de la variable privada

dejah = Persona()  #  asigna a un variable una clase
dejah.setNombre("dejah")  #  llama a un objeto junto a una funcion ademas da un valor
print(dejah.getNombre())  #  imprime un objeto y llama una funcion
dejah.setEmail("1722@utec.com")  #  llama a un objeto junto a una funcion ademas da un valor
print(dejah.getEmail()) #  imprime un objeto y el objeto llama una funcion