# PR2_Parcial2
actividad en clase


#Codigo 1

print("")

print ("Dylan Aaron Elicserio Martínez 3°W #Control1179")

print("")

#Define el saludo para luego imprimir el texto declarado

def mostrar_saludo():

    print("Hey amigos!")
    
    print("")

#Llamada a la función

mostrar_saludo()

![image](https://github.com/user-attachments/assets/ff371b1e-29e1-48d0-924e-0122941bc2da)
![image](https://github.com/user-attachments/assets/04a8da0b-7078-4cd6-8c15-f41206910807)

#Codigo 2

print("")

print ("Dylan Aaron Elicserio Martínez 3°W #Control1179")

print("")

#Definira el nombre para imprimirlo junto al texto ya ingresado

def saludar(nombre):

    print(f"¡Hola {nombre}!")

#Ejemplo

saludar("Dylan")

![image](https://github.com/user-attachments/assets/0bbe8d21-07d7-4dfb-8bb8-013cb90d03fd)
![image](https://github.com/user-attachments/assets/bfc8c188-492f-4859-827c-b24aea115ef2)

#Codigo 3

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

![image](https://github.com/user-attachments/assets/395026e2-cb20-47fd-b820-8072d7b78fd4)
![image](https://github.com/user-attachments/assets/ee470712-aac6-4c28-a5ea-2a7350f1331d)

#Codigo 4

# Imprime información del autor osea yo

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

![image](https://github.com/user-attachments/assets/9733dc6d-c365-4e38-9eae-75466d85b274)
![image](https://github.com/user-attachments/assets/dec5ff2c-5a99-427d-ac72-dbcad10633f0)

#Codigo 5

# Imprime información del autor osea yo

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

![image](https://github.com/user-attachments/assets/c866eab8-eb3b-43fc-acaf-4ffed26a0c0c)
![image](https://github.com/user-attachments/assets/3008605d-e1d2-4dad-9971-6ad84786b58f)

#Codigo 6

# Imprime información del autor osea yo

print("")

print("Dylan Aaron Elicserio Martínez 3°W #Control1179")

print("")

def validar_email(email):

    """
    
    Función que verifica si un email es válido, en este caso, si contiene '@gmail.com'.

    Parámetros
    
    email (str): La dirección de correo electrónico que se va a validar.

    Retorna:
    
    bool: True si el email es válido, False en caso contrario.
    
    """
    
    # Verifica si la dirección de email contiene '@gmail.com'
    
    if '@gmail.com' in email:
    
        return True  # Retorna True si es un email válido
        
    else:
    
        return False  # Retorna False si no es válido

# Captura la dirección de email del usuario

email_usuario = input("Ingresa tu correo Gmail: ")

# Validación de la dirección de email ingresada

if validar_email(email_usuario):

    print("La dirección de email es válida.")  # Mensaje de éxito si el email es válido
    
else:

    print("La dirección de email no es válida. Asegúrate de haberla escrito bien.")  # Mensaje de error si el email no es válido

![image](https://github.com/user-attachments/assets/6e1ce4ab-0cd2-46af-823c-535e487c56b8)
![image](https://github.com/user-attachments/assets/30ebec1a-5ef4-474b-96c7-e2efc9304d5e)

#Codigo 7

print("")

print ("Dylan Aaron Elicserio Martínez 3°W #Control1179")

print("")

def longitud(texto):

    #Eliminar espacios en blanco y dividirpor espacios
    
    palabras = texto.strip().split()
    
    #verificar si hay palabras en la lista
    
    if palabras:
    
        #regresar la longitud de la ultima palabra
        
        return len(palabras[-1])
        
    else:
    
        return 0 #si no hay palabras, devolver 0

#Captura de texto del usuario

texto_usuario = input("Introduce algunas palabras:")

#obtener longitud de la ultima palabra

longitud1 = longitud(texto_usuario)

#mostrar el resultado

print(f"la longitud de la ultima palabra es: {longitud1}")

![image](https://github.com/user-attachments/assets/a9a1948c-8a8d-44e6-b3d3-1b403a028bf7)
![image](https://github.com/user-attachments/assets/1c08ec38-1e4a-49fa-a60e-94df7c4f0adf)

#Codigo 8

# Imprime información del autor osea yo

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

![image](https://github.com/user-attachments/assets/783ef7bc-3eea-4025-aada-78d901a4dc1a)
![image](https://github.com/user-attachments/assets/2e8d3261-f5e1-42e8-a084-f3448b8bd96d)

#Codigo 9

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

![image](https://github.com/user-attachments/assets/41144cca-0d40-4b87-8e63-6474fb1383bc)
![image](https://github.com/user-attachments/assets/dff0b281-37c5-47b5-9682-134e9c72bb42)
![image](https://github.com/user-attachments/assets/b93a8128-2803-4b37-9091-5ca6625e7af3)


#Codigo 10

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
    
![image](https://github.com/user-attachments/assets/7f91b4b0-11a6-48b4-b553-e4a3963f0468)
![image](https://github.com/user-attachments/assets/1cdce877-47f3-43d1-bdfd-02a6b422a921)

#Codigo 11

print("")

print ("Dylan Aaron Elicserio Martínez 3°W #Control1179")

print("")

import math

def distancia_dirigida(punto1, punto2):

    """
    
    Función que calcula la distancia dirigida entre dos puntos en un espacio 2D.

    Parámetros:
    
    punto1 (tuple): Un tuple que representa las coordenadas del primer punto (x1, y1).
    
    punto2 (tuple): Un tuple que representa las coordenadas del segundo punto (x2, y2).

    Retorna:
    
    float: La distancia dirigida entre los dos puntos.
    
    """
    
    # Desempaqueta las coordenadas del primer punto
    
    x1, y1 = punto1  
    
    # Desempaqueta las coordenadas del segundo punto
    
    x2, y2 = punto2  
    
    # Calcula la distancia utilizando la fórmula de distancia euclidiana
    
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    return distancia  # Retorna la distancia calculada

def main():

    """
    
    Función principal que solicita al usuario las coordenadas de dos puntos
    
    y calcula la distancia dirigida entre ellos.

    Esta función gestiona la entrada del usuario y muestra el resultado de la distancia.
    
    """
    
    # Solicita las coordenadas del primer punto
    
    x1 = float(input("Ingresa la coordenada x del primer punto: "))
    
    y1 = float(input("Ingresa la coordenada y del primer punto: "))
    
    # Solicita las coordenadas del segundo punto
    
    x2 = float(input("Ingresa la coordenada x del segundo punto: "))
    
    y2 = float(input("Ingresa la coordenada y del segundo punto: "))
    
    # Llama a la función distancia_dirigida con los puntos ingresados
    
    punto1 = (x1, y1)  # Crea un tuple para el primer punto
    
    punto2 = (x2, y2)  # Crea un tuple para el segundo punto
    
    distancia = distancia_dirigida(punto1, punto2)  # Calcula la distancia
    
    # Muestra el resultado de la distancia calculada
    
    print(f"La distancia dirigida entre los puntos {punto1} y {punto2} es: {distancia:.2f}")

if __name__ == "__main__":

    # Llama a la función principal para ejecutar el programa
    
    main()

  ![image](https://github.com/user-attachments/assets/a168d403-23e3-42c6-9816-34f71e1b55c2)
  ![image](https://github.com/user-attachments/assets/ffb26b22-0116-49f2-8683-4bdd3ae0125e)
  ![image](https://github.com/user-attachments/assets/24733c58-51a5-445a-8a24-5abb7f6bb40d)


