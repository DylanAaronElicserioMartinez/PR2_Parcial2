print("")
print ("Dylan Aaron Elicserio Martínez 3°W #Control1179")
print("")
numero = input("ingresa el numero al que le quieras calcular el factorial:")
n = int(numero)
def factorial(n):
    """
    Calcula el factorial de un número positivo.
    """
    if n < 0:
        return "Número no válido"
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Ejemplo de uso
print(factorial(n))  #sale el factorial del numero ingresado
