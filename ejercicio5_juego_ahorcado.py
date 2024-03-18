from random import *

lista_palabras = ['casa', 'mundo', 'python', 'uva']
palabra_seleccionada = choice(lista_palabras)
tamaño_palabra = len(palabra_seleccionada)
print("La palabra seleccionada tiene {} letras.".format(tamaño_palabra))

linea = 0
while linea < tamaño_palabra:
    print('_', end=' ')
    linea += 1

intentos = 6
letras_adivinadas = []

while intentos > 0:
    print("\nIntentos restantes:", intentos)
    letra_escogida = input("Ingrese una letra: ")

    if letra_escogida in letras_adivinadas:
        print("Ya has ingresado esta letra. Intenta con otra.")
        continue

    letras_adivinadas.append(letra_escogida)

    if letra_escogida in palabra_seleccionada:
        print("¡Bien hecho!")
    else:
        print("Letra incorrecta.")
        intentos -= 1

    palabra_oculta = ""
    for letra in palabra_seleccionada:
        if letra in letras_adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta += "_ "
    print(palabra_oculta)

    if "_" not in palabra_oculta:
        print("¡Felicidades! Has adivinado la palabra:", palabra_seleccionada)
        break

if intentos == 0:
    print("¡Lo siento! Te has quedado sin intentos. La palabra era:", palabra_seleccionada)
