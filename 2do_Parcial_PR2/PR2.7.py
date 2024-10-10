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
