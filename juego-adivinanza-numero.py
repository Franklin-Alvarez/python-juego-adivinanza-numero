import random


def juego_adivinanza_():
    # Generar un número del uno al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de adivinanza de número!")
    print("Debes adivinar un número entre el 1 al 100")
    print("¡Intenta adivinarlo!")

    while not adivinado:
        # Solicitar un número
        adivinanza = input("Introduzca un número del 1 al 100: ")

        # Verificar que la entrada sea un numero
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(
                    f"¡Felicitaciones has ganando el juego! El número {adivinanza} es el secreto y lo has logrado en {intentos} intentos"
                )
        else:
            print("Por favor ingrese un número valido entre 1 y 100")

    return

juego_adivinanza_()