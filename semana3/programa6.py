"""
    Programa 6
    Nombre: Erick Gutierrez Hernandez
    Fecha: 31/01/2023
    Descripción: Programa para calcular el perimetro y area de un circulo y un cuadrado
"""
PI = 3.1416
radio = float(input("Ingrese el valor del radio del circulo: "))  #  Se asigna una cadena de texto a una variable la cual es convertida en un "int"
diametro = 2 * radio  #  multiplica un variable y la guarda en otra variable
perimetroCirculo = PI * diametro  #  multiplica una variable por otra y lo guarda en otra variable
areaCirculo = PI * (radio ** 2)  #  se asgina el resultado de una expresion matematica a una varibale
print("El perimetro del circulo es:", perimetroCirculo , "\nEl area del circulo es:", areaCirculo)  #  se imprime una cadena de texto junto a unas variables

lado = float(input("Ingresa el valor del lado de un cuadrado: "))  #  Se asigna una cadena de texto a una variable la cual es convertida en un "int"
perimetroCuadrado = 4 * lado  #  multiplica un variable y la guarda en otra variable
areaCuadrado  = lado * lado  #  multiplica una variable por otra y lo guarda en otra variable
print("El perimetro del cuadrado es:", perimetroCuadrado , "\nEl area del cuadrado es:", areaCuadrado)  #  se imprime una cadena de texto junto a unas variables


