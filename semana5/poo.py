"""
    Programa 14
    Nombre: Erick Gutierrez Hernandez
    Fecha: 14/02/2023
    Descripción: 
"""
class Persona:  #  crea una clase
    
	__nombre = None  #  __nombre variable privada
	__edad = None  #  variable privada
    
	def __init__(self):  #  inicializa la funcion
		print("Persona")  #  imprime esto al iniciar la funcion

	def setNombre(self, nombre):  #  creea una funcion para poder acceder y darle valor a la variable privada
		self.__nombre = nombre  #  asigna un valor a la variable privada
	def getNombre(self):  #  creea una funcion para poder acceder a una variable privada y poder obtener su valor
		return self.__nombre  #  devuelve el valor de la variable privada

	def setEdad(self, edad):  #  creea una funcion para poder acceder y darle valor a la variable privada
		self.__edad = edad  #  asigna un valor a la variable privada
	def getEdad(self):  #  creea una funcion para poder acceder a una variable privada y poder obtener su valor
		return self.__edad  #  devuelve el valor de la variable privada

class Profesor(Persona):
    
    __noNomina = None
    
    def __init__(self):  #  inicializa la funcion
        super().__init__()  #  accede a otras clases mediante la funcion super 
        print("Profesor")   #  imprime esto al iniciar la funcion

    def setNoNomina(self, noNomina):  #  creea una funcion para poder acceder y darle valor a la variable privada
        self.__noNomina = noNomina  #  asigna un valor a la variable privada
    def getNoNomina(self):  #  creea una funcion para poder acceder a una variable privada y poder obtener su valor
        return self.__noNomina  #  devuelve el valor de la variable privada

class Alumno(Persona):
    __matricula = None

    def __init__(self):  #  inicializa la funcion
        super().__init__()  #  accede a otras clases mediante la funcion super 
        print("Alumano")   #  imprime esto al iniciar la funcion

    def setMatricula(self, matricula):  #  creea una funcion para poder acceder y darle valor a la variable privada
        self.__matricula = matricula  #  asigna un valor a la variable privada
    def getMatricula(self):  #  creea una funcion para poder acceder a una variable privada y poder obtener su valor
        return self.__matricula  #  devuelve el valor de la variable privada

class Coordinador(Persona):
    
    __carreraCordina = None
    __noNomina = None

    def __init__(self):  #  inicializa la funcion
        super().__init__()  #  accede a otras clases mediante la funcion super 
        print("Alumano")   #  imprime esto al iniciar la funcion
    
    def setCarreraCordina(self, carreraCordina):  #  creea una funcion para poder acceder y darle valor a la variable privada
        self.__carreraCordina = carreraCordina  #  asigna un valor a la variable privada
    def getCarreraCordina(self):  #  creea una funcion para poder acceder a una variable privada
        return self.__carreraCordina  #  devuelve el valor que se encuentra en la variable privada
           
    def setNoNomina(self, noNomina):  #  creea una funcion para poder acceder y darle valor a la variable privada
        self.__noNomina = noNomina  #  asigna un valor a la variable privada
    def getNoNomina(self):  #  creea una funcion para poder acceder a una variable privada y poder obtener su valor
        return self.__noNomina  #  devuelve el valor de la variable privada

objeto_persona = Persona()  #  asigna a un variable una clase  
objeto_alumno = Alumno()  #  asigna a un variable una clase
objeto_profesor = Profesor() 
objeto_cordinador = Coordinador()
