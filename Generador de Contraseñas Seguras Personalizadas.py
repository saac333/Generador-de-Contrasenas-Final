"""""
Version mejorada con un bucle para no acabar el programa y generar de nuevo
"""
# Variables y librerías
import random
# Constantes
LETRAS = "abcdefghijklmñnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
SIMBOLOS = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
NUMEROS = "0123456789"
# Función para mostrar el menú y capturar la opción
def mostrar_menu():
    """
    menu principal
    """
    print("\nBIENVENIDO AL GENERADOR DE CONTRASEÑAS MÁS SEGURO")
    texto = """Opciones:
    1. Solo con letras (mayúsculas y minúsculas)
    2. Solo con símbolos
    3. Con mayúsculas, minúsculas, números y símbolos
    4. Salir
    """
    print(texto)
    return int(input("Ingresa el número de la opción:\n"))

# Función para generar una contraseña
def generar_contrasena(caracteres, largo):
    """
    Genera una contraseña a partir de un conjunto de caracteres.
    - caracteres: Conjunto de caracteres permitido.
    - largo: Longitud de la contraseña.
    """
    if largo > len(caracteres):
        print("Error: La longitud solicitada excede los caracteres disponibles.")
        return None
    return "".join(random.sample(caracteres, largo))

# Función principal para el flujo del programa
def main():
    """
    FUNCION PRINCIPAL
    """
    while True:
        opcion_menu = mostrar_menu()
        if opcion_menu == 1:
            # Opción 1: Contraseña solo con letras
            largo = int(input("¿De cuántos caracteres deseas la contraseña?:\n"))
            contrasena = generar_contrasena(LETRAS, largo)
            if contrasena:
                print("Su contraseña generada es:\n", contrasena)
        elif opcion_menu == 2:
            # Opción 2: Contraseña solo con símbolos
            largo = int(input("¿De cuántos caracteres deseas la contraseña?:\n"))
            contrasena = generar_contrasena(SIMBOLOS, largo)
            if contrasena:
                print("Su contraseña generada es:\n", contrasena)
        elif opcion_menu == 3:
            # Opción 3: Contraseña con letras, números y símbolos
            cantidad_letras = int(input("¿Cuántas letras deseas en la contraseña?:\n"))
            cantidad_numeros = int(input("¿Cuántos números deseas en la contraseña?:\n"))
            cantidad_simbolos = int(input("¿Cuántos símbolos deseas en la contraseña?:\n"))
            # Validar si las cantidades son correctas
            if cantidad_letras + cantidad_numeros + cantidad_simbolos > len(LETRAS + NUMEROS + SIMBOLOS):
                print("Error: La suma de caracteres excede los disponibles.")
                continue
            # Generar contraseñas para cada tipo y combinarlas
            letras_random = random.sample(LETRAS, cantidad_letras)
            numeros_random = random.sample(NUMEROS, cantidad_numeros)
            simbolos_random = random.sample(SIMBOLOS, cantidad_simbolos)
            mezcla = letras_random + numeros_random + simbolos_random
            random.shuffle(mezcla)
            contrasena = "".join(mezcla)
            print("Su contraseña generada es:\n", contrasena)
        elif opcion_menu == 4:
            # Salir del programa
            print("Gracias por usar el generador de contraseñas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
# Ejecutar el programa principal
main()
