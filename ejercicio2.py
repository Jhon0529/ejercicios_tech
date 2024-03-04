def ordenar_alfab(cadena):
    lista_letras = sorted(cadena)
    lista_sin_repeticion = []
    for letra in lista_letras:
        if letra not in lista_sin_repeticion:
            lista_sin_repeticion.append(letra)
    cadena_ordenada = ''.join(lista_sin_repeticion)
    return cadena_ordenada

cadena = "hola mundo"
print(ordenar_alfab(cadena))