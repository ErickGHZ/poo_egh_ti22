"""
    Programa 7
    Nombre: Erick Gutierrez Hernandez
    Fecha: 01/02/2023
    Descripción: Programa para comparar 2 números enteros e imprimir el número mayor
"""
numero1 = int(input("Ingresa un numero entero:"))  #  Asigan el valor de una cadena de texto a una variable y la convierte en un entero
numero2 = int(input("Ingresa otro numero entero:"))  #  Asigan el valor de una cadena de texto a una variable y la convierte en un entero
if numero1>numero2:  #  realiza una comparacion de dos variables
    print(numero1)  #  muestra una cadena de texto si la comparacion anterior es "true"
elif numero1 == numero2:  #  realiza otra comparacion en caso de que la anterior sea falsa
    print(None)  #  muestra una cadena de texto si la comparacion anterior es "flase" y esta es verdadera
else:  #  asigna una accion en caso de que la comparacion sea falsa 
     print(numero2)  #  muestra una cadena de texto si la comparacion anterior es "flase"
