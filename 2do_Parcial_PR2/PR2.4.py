# Imprime información del autor
print("")
print("Dylan Aaron Elicserio Martínez 3°W #Control1179")
print("")

# Solicita al usuario que ingrese un número para calcular el precio con IVA
numero = input("Ingresa el número al que le quieras calcular el precio del IVA: ")
n = int(numero)  # Convierte la entrada a un entero

def calcular_factura(sin_iva, iva=21):
    """
    Calcula el total de una factura incluyendo IVA.

    Parámetros:
    sin_iva (float): El monto de la factura sin IVA.
    iva (float, opcional): La tasa de IVA a aplicar (por defecto es 21).

    Retorna:
    float: El total de la factura incluyendo IVA.
    """
    total = sin_iva * (1 + iva / 100)  # Calcula el total sumando el IVA al monto original
    return total  # Retorna el total calculado

# Ejemplo de uso
print(calcular_factura(n))  # Imprime el total del precio incluyendo IVA