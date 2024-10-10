# Imprime información del autor
print("")
print("Dylan Aaron Elicserio Martínez 3°W #Control1179")
print("")

def validar_email(email):
    """
    Función que verifica si un email es válido, en este caso, si contiene '@gmail.com'.

    Parámetros:
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