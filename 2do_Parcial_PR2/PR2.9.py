print("")
print ("Dylan Aaron Elicserio Martínez 3°W #Control1179")
print("")
def sum(numbers):
    """
    Función que suma todos los números en una lista.
    
    Parámetros:
    numbers (list): Una lista de números enteros.
    
    Retorna:
    int: La suma de todos los números en la lista.
    """
    total = 0  # Inicializa la suma total en 0
    for number in numbers:  # Itera sobre cada número en la lista
        total += number  # Suma cada número al total
    return total  # Retorna la suma total

def multip(numbers):
    """
    Función que multiplica todos los números en una lista.
    
    Parámetros:
    numbers (list): Una lista de números enteros.
    
    Retorna:
    int: El producto de todos los números en la lista.
    """
    total = 1  # Inicializa el producto total en 1
    for number in numbers:  # Itera sobre cada número en la lista
        total *= number  # Multiplica cada número al total
    return total  # Retorna el producto total

def main():
    """
    Función principal que solicita al usuario una lista de números,
    y luego calcula y muestra la suma y el producto de esos números.
    """
    # Pedir al usuario que ingrese números separados por comas
    user_input = input("Ingresa los números separados por comas: ")
    
    # Convertir la cadena de entrada en una lista de números enteros
    number_list = [int(num) for num in user_input.split(',')]
    
    # Calcular la suma de los números usando la función sum
    total_sum = sum(number_list)
    
    # Calcular la multiplicación de los números usando la función multip
    total_multiplication = multip(number_list)
    
    # Mostrar los resultados de la suma y la multiplicación
    print(f"La suma de los números es: {total_sum}")
    print(f"La multiplicación de los números es: {total_multiplication}")

if __name__ == "__main__":
    # Llama a la función principal para ejecutar el programa
    main()