# Imprime información del autor
print("")
print("Dylan Aaron Elicserio Martínez 3°W #Control1179")
print("")

# Solicita al usuario que ingrese tres valores enteros
a = int(input("Ingresa el primer valor: "))  # Primer valor
b = int(input("Ingresa el segundo valor: "))  # Segundo valor
c = int(input("Ingresa el tercer valor: "))    # Tercer valor

def mayor_de_tres(a, b, c):
    """
    Función que devuelve el mayor de tres números.

    Parámetros:
    a (int): El primer número.
    b (int): El segundo número.
    c (int): El tercer número.

    Retorna:
    int: El mayor de los tres números ingresados.
    """
    return max(a, b, c)  # Devuelve el mayor de los tres números usando la función max

# Ejemplo de uso
print(mayor_de_tres(a, b, c))  # Imprime el mayor de los tres valores ingresados