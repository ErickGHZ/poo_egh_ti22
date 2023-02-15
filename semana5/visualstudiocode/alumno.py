from persona import Persona   #  Importa la calse Persona del archivo persona.py

class Alumno(Persona):  #  Crea la clase Alumno que hereda de la clase Persona
    def __init__(self) -> None:  #  Constructor de la clase Alumno
        super().__init__()  #  Llama al constructor de la clase Persona
        print("Alumno")  #  Imprime el texto Alumno

objeto_alumno = Alumno()  #  Crea una objeto de la clase 
