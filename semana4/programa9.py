"""
    Programa 9
    Nombre: Erick Gutierrez Hernandez
    Fecha: 08/02/2023
    Descripción: Programa para saber que numero es mayor mediante metodos
"""
def mayor (numero1, numero2):  #  define una funcion la cual solicita la entrada de dos variables
    if numero1 > numero2:  #  realiza una comparacion
        print(numero1)  #  si la comparacion anterior es verdadera realiza la impresión de una varibale
    elif numero2 > numero1:  #  si la primera comparación es falsa realiza enta comparación
        print(numero2) #  si la comparación anterior es verdadera imprime una varibale
    else:  #  asigna una accion en caso de que las comparaciones anteriores sean falsa
        print("Iguales")  #  realiza la impresion de una variable

mayor(3,2)  #  Resultado esperado: 3
mayor(2,3)  #  Resultado esperado: 3
mayor(3,3)  #  Resultado esperado: None