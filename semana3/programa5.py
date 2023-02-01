"""
    Programa 5
    Nombre: Erick Gutierrez Hernandez
    Fecha: 30/01/2023
    Descripción: Programa de para calcular el perímetro y área de cualquier triángulo
"""
import math  #  importa la libreria math para poder realizar una raiz cuadrada

lado_a = float(input("Ingresa el valor del primer lado del triangulo: "))  #  Se asigna una cadena de texto a una variable la cual es convertida en un "int" 
lado_b = float(input("Ingresa el valor del segundo lado del triangulo: "))  #  Se asigna una cadena de texto a una variable la cual es convertida en un "int" 
lado_c = float(input("Ingresa el valor del tercer lado del trianulo: "))  #  Se asigna una cadena de texto a una variable la cual es convertida en un "int" 
perimetro = lado_a + lado_b + lado_c   #  Se asigna el resultado de la suma de dos variables a una variable 
s = perimetro/2  #  Se asigna el resultado de la divicion de dos varibales a un variable
area = math.sqrt(s * (s-lado_a) * (s-lado_b) * (s-lado_c))  #  se asgina el resultado de una expresion matematica a una varibale
print("El perimetro del triangulo es:", perimetro , "\nEl area del triangulo es:", area)  #  se imprime una cadena de texto junto a unas variables
