from persona import Persona  #  Importa la calse Persona del archivo persona.py

class Profesor(Persona):  #  Crea la clase Profesor que hereda de la clase Persona
    def __init__(self) -> None:  #  Constructor de la clase Profesor
        super().__init__()  #  Llama al constructor de la clase Persona
        print("Profesor")  #  Imprime el texto Profesor

objeto_profesro = Profesor()  #  Crea una objeto de la clase 