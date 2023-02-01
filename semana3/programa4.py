"""
    Programa 4
    Nombre: Erick Gutierrez Hernandez
    Fecha: 30/01/2023
    Descripción: Convertir un string a un int con casting
"""
numero1 = int(input("Numero 1: "))  #  Se asigna una cadena de texto a una variable la cual es convertida en un "int" para que no genere un fallo al querer intentar sumar un int y un string
numero2 = 10  #  Se asigna un valor tipo int a la variable
suma = numero1 + numero2  #  Se realiza una suma de 2 variables y guardan el resultado de estas en otra variable
resta = numero1 - numero2  #  Se realiza una resta de 2 variables y guardan el resultado de estas en otra variable
multiplicacion = numero1 * numero2  #  Se realiza una multiplicación de 2 variables y guardan el resultado de estas en otra variable
division = numero1 / numero2  #  Se realiza una división de 2 variables y guardan el resultado de estas en otra variable
potencia = numero1**numero2  #  Se realiza una potencia de 2 variables y guardan el resultado de estas en otra variable
print("La suma de estos dos numeros es:", suma , "\nLa resta de estos dos numeros es:", resta , "\nLa multiplicacion de estos dos numeros es:", multiplicacion , "\nLa division de estos dos numeros es:", division , "\nLa potencia de estos dos numeros es:", potencia )  #  se imprime unas cadenas de texto junto a unas variables
