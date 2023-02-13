class Persona:
	__nombre = None  #  __nombre variable privada
	__email = None  #  variable privada
	def __init__(self):  #  inicializa la funcion
		print("Persona")  #  imprime esto al iniciar la funcion
	def setNombre(self, nombre):  #  creea una funcion para poder acceder y darle valor a la variable privada
		self.__nombre = nombre  #  asigna un valor a la variable privada
	def getNombre(self):  #  creea una funcion para poder 
		return self.__nombre
	def setEmail(self, email):
		self.__email = email
	def getEmail(self):
		return self.__email
dejah = Persona()  #  asigna a una objeto una funcion
dejah.setNombre("dejah")
print(dejah.getNombre())
dejah.setEmail("1722@utec.com")
print(dejah.getEmail())
print(Persona.nombre)