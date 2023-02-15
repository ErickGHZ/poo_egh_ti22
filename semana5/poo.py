"""
    Programa 14
    Nombre: Erick Gutierrez Hernandez
    Fecha: 14/02/2023
    Descripción: Herencia de clases mediante funciones
"""
class Persona:  #  crea la clase clase
    
	__nombre = None  #  variable privada
	__edad = None  #  variable privada
    
	def __init__(self):  #  Constructor de la clase Persona
		print("Persona")  #  Imprime el texto

	def setNombre(self, nombre):  #  creea una funcion para poder acceder y darle valor a la variable privada
		self.__nombre = nombre  #  asigna un valor a la variable privada
	def getNombre(self):  #  creea una funcion para poder acceder a una variable privada y poder obtener su valor
		return self.__nombre  #  devuelve el valor de la variable privada

	def setEdad(self, edad):  #  creea una funcion para poder acceder y darle valor a la variable privada
		self.__edad = edad  #  asigna un valor a la variable privada
	def getEdad(self):  #  creea una funcion para poder acceder a una variable privada y poder obtener su valor
		return self.__edad  #  devuelve el valor de la variable privada

class Profesor(Persona):  #  Crea la clase Profesor que hereda de la clase Persona
    
    __noNomina = None  #  variable privada 
    
    def __init__(self):  #  Constructor de la clase Persona
        super().__init__()  #  accede a otras clases mediante la funcion super 
        print("Profesor")   #  Imprime el texto

    def setNoNomina(self, noNomina):  #  creea una funcion para poder acceder y darle valor a la variable privada
        self.__noNomina = noNomina  #  asigna un valor a la variable privada
    def getNoNomina(self):  #  creea una funcion para poder acceder a una variable privada y poder obtener su valor
        return self.__noNomina  #  devuelve el valor de la variable privada

class Alumno(Persona):  #  Crea la clase Alumno que hereda de la clase Persona
    __matricula = None

    def __init__(self):  #  Constructor de la clase Persona
        super().__init__()  #  accede a otras clases mediante la funcion super 
        print("Alumno")   #  Imprime el texto

    def setMatricula(self, matricula):  #  creea una funcion para poder acceder y darle valor a la variable privada
        self.__matricula = matricula  #  asigna un valor a la variable privada
    def getMatricula(self):  #  creea una funcion para poder acceder a una variable privada y poder obtener su valor
        return self.__matricula  #  devuelve el valor de la variable privada

class Coordinador(Persona):  #  Crea la clase Coordinador que hereda de la clase Persona
    
    __carreraCordina = None  #  variable privada
    __noNomina = None  #  variable privada

    def __init__(self):  #  Constructor de la clase Persona
        super().__init__()  #  accede a otras clases mediante la funcion super 
        print("Coordinador")   #  Imprime el texto
    
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
objeto_profesor = Profesor()   #  asigna a un variable una clase  
objeto_cordinador = Coordinador()  #  asigna a un variable una clase  
