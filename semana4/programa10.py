"""
    Programa 10
    Nombre: Erick Gutierrez Hernandez
    Fecha: 08/02/2023
    Descripción: Comparar 2 numeros enteros en imprimir el numero mayor mediante, Definiciones de la forma pythonic
"""
def mayor(numero1:int, numero2:int)->int:  #  define una funcion la cual solicita la entrada de dos variables y por medio del typing sugiere el tipo de datos que se daran y la salida
    mayor = None  #  asigna un valor en este caso el valor es "vacio" a un variiable
    if numero1 > numero2:  #  realiza una comparación
        mayor = numero1  #  si la comparación anterior es verdadera asigna el valor de esa variable a otra
    elif numero2 > numero1:  #  si la comparación anterior es falsa realiza esta comparación
        mayor = numero2  #  si la comparación anterior es verdadera asigna el valor de esa variable a otra
    else:   #  asigna una accion en caso de que la comparación anteriores sea falsa
        mayor = None  #  si la comparación anterior es verdadera asigna el valor de esa variable a otra
    return mayor  #  returna el valor de una varibale

print(mayor(3,2))  #  Resultado esperado: 3
print(mayor(2,3))  #  Resultado esperado: 3
print(mayor(3,3))  #  Resultado esperado: None