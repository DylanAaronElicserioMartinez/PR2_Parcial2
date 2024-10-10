print("")
print ("Dylan Aaron Elicserio Martínez 3°W #Control1179")
print("")
def es_vocal(caracter):
    """
    Función que verifica si un carácter es una vocal.

    Parámetros:
    caracter (str): Un carácter que se va a verificar.

    Retorna:
    bool: True si el carácter es una vocal (a, e, i, o, u), False de lo contrario.
    """
    # Convierte el carácter a minúscula y verifica si está en la cadena de vocales
    return caracter.lower() in 'aeiou'

def main():
    """
    Función principal que solicita al usuario un carácter y verifica si es una vocal.

    Esta función gestiona la entrada del usuario y muestra el resultado de la verificación.
    """
    # Pide al usuario que ingrese un carácter
    caracter = input("Ingresa un carácter: ")

    # Verifica si se ha ingresado un único carácter
    if len(caracter) != 1:
        print("Por favor, ingresa solo un carácter.")
        return  # Sale de la función si la entrada no es válida

    # Llama a la función es_vocal y muestra el resultado
    if es_vocal(caracter):
        print(f"'{caracter}' es una vocal.")
    else:
        print(f"'{caracter}' no es una vocal.")

if __name__ == "__main__":
    # Llama a la función principal para ejecutar el programa
    main()
    