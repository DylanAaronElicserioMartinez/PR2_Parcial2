# Imprime información del autor
print("")
print("Dylan Aaron Elicserio Martínez 3°W #Control1179")
print("")

# Solicita al usuario que ingrese un número para calcular el área del círculo
numero = input("Ingresa el número al que le quieras calcular el área del círculo: ")
n = int(numero)  # Convierte la entrada a un entero

# Solicita al usuario que ingrese un número para calcular el volumen del cilindro
numero1 = input("Ingresa el número al que le quieras calcular el área del cilindro: ")
w = int(numero1)  # Convierte la entrada a un entero

import math  # Importa el módulo math para acceder a constantes y funciones matemáticas

def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
    radio (float): El radio del círculo.

    Retorna:
    float: El área del círculo.
    """
    return math.pi * radio ** 2  # Calcula el área usando la fórmula A = π * r^2

def volumen_cilindro(radio, altura):
    """
    Calcula el volumen de un cilindro dado su radio y altura.

    Parámetros:
    radio (float): El radio de la base del cilindro.
    altura (float): La altura del cilindro.

    Retorna:
    float: El volumen del cilindro.
    """
    area = area_circulo(radio)  # Llama a la función para calcular el área de la base
    return area * altura  # Calcula el volumen usando la fórmula V = A * h

# Ejemplo de uso
print(area_circulo(n))  # Imprime el área del círculo con el radio proporcionado
print(volumen_cilindro(n, w))  # Imprime el volumen del cilindro con el radio y altura proporcionados