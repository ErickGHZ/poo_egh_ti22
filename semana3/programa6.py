"""
    Programa 6
    Nombre: Erick Gutierrez Hernandez
    Fecha: 31/01/2023
    Descripción: Programa para calcular el perimetro y area de un circulo y un cuadrado
"""
PI = 3.1416
radio =  float(input("Ingrese el valor del radio del circulo: "))  #  Se asigna una cadena de texto a una variable la cual es convertida en un "int"
diametro = 2 * radio
perimetro = PI * diametro
area = PI * (radio ** 2)
radiocuadrado = radio**2
print("El perimetro del dirculo es", perimetro , "\nEl area del circulo es:", area)  #  se imprime una cadena de texto junto a unas variables
