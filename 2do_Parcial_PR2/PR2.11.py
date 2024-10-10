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