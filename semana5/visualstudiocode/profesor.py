"""
    Programa 18
    Nombre: Erick Gutierrez Hernandez
    Fecha: 13/02/2023
    Descripción: Crea una clase la cual tiene atributos los cuales son heredados de otra clase que esta en otro documento
"""
from persona import Persona  #  Importa la calse Persona del archivo persona.py

class Profesor(Persona):  #  Crea la clase Profesor que hereda de la clase Persona
    def __init__(self) -> None:  #  Constructor de la clase Profesor
        super().__init__()  #  Llama al constructor de la clase Persona
        print("Profesor")  #  Imprime el texto Profesor

objeto_profesro = Profesor()  #  Crea una objeto de la clase 