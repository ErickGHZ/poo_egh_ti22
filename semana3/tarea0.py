"""
Programa de Python para calcular y medir el perímetro y área de cualquier triángulo
"""
import math  #  importa la libreria math para poder realizar una raiz cuadrada

lado_a = float(input("Ingresa el valor del primer lado del triangulo: "))
lado_b = float(input("Ingresa el valor del segundo lado del triangulo: "))
lado_c = float(input("Ingresa el valor del tercer lado del trianulo: "))
perimetro = lado_a + lado_b + lado_c
s = perimetro/2
area = math.sqrt(s * (s-lado_a) * (s-lado_b) * (s-lado_c))
print("El perimetro del triangulo es:", perimetro , "\nEl area del triangulo es:", area)