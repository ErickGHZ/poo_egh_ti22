"""
    Programa 3
    Nombre: Erick Gutierrez Hernandez
    Fecha: 24/01/2023
    Descripcion: En este programa veremos como realizar impresiones de operaciones aritmeticas de la forma tradicional "print" y con la funcion format
"""
variable1 = 10  #  variable para almacenar una cadena de caracteres
variable2 = 5  #  variable para almacenar una cadena de caracteres
print(variable1+variable2)  #  imprime la suma de dos variable
print("{} + {} = {}".format(variable1,variable2,variable1+variable2))  #  imprime con la funcion format las variables, ademas realiza la suma de estas 2 variables y muestra el resultado de estas 2
print("{} - {} = {}".format(variable1,variable2,variable1-variable2))  #  imprime con la funcion format las variables, ademas realiza la resta de estas 2 variables y muestra el resultado de estas 2
print("{} = {} * {}".format(variable1*variable2,variable2,variable1))  #  imprime con la funcion format las variables, ademas realiza la multiplicacion de estas 2 variables y muestra el resultado de estas 2 con otro orden 
print("El resultado de dividir {} / {} es {}".format(variable1,variable2,variable1/variable2))  #  imprime con la funcion format texto y variables, ademas realiza la divicion de 2 variables y muestra el resultado de estas 2  
