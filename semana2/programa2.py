"""
    Programa 2
    Nombre: Erick Gutierrez Hernandez
    Fecha: 24/01/2023
    Descripcion: En este programa veremos como realizar concatenaciones de variables de dos formas ademas de identificar errores y saber de que tipo son 
"""
variable1 = "Hola"  #  variable para almacenar una cadena de caracteres
variable2 = " Python"  #  variable para almacenar una cadena de caracteres
print(variable1 + variable2)  #  concatena cadenas de caracteres y las imprime
print("{}{}".format(variable1,variable2))  #  concatena cadenas de caracteres y las imprime pero con la funcion "format"

"""
    print("{}{}"format(variable1,variable2))  #  sintaxis invalida
    print("{}{}".format(variable1variable2))  #  error de sangria
    print("{ }{}".format(variable1,variable2))  #  error de llave 
"""
