#!/usr/bin/env python3
#Libreria  para llevar el conteo acomulado por palabra
import sys

#Inicializamos variables para rastrear la palabra actual y su conteo total
current_word = None
current_count = 0

#Procesamos la entrada linea por linea
for line in sys.stdin:
    #Eliminar espacios en blancos al iniciar y finalizar de la linea
    word, count = line.strip().split('\t', 1)	#Luego se separa la palabra y su conteo usando tabuladr ('\t')

    #Convertir el valor de conteo en entero o string
    count = int(count)

    #Si la palabra actual es igual a la anterior (Se acomula esta palabra)
    if current_word == word:
    #Sumamos el nuevo conteo acomulado
        current_count += count
    else:
	#Si estamos en una nueva palabra (y no es la primera linea),
	#Imprimimos la palabra anterior con su total acomulado
        if current_word:
            print(f"{current_word}\t{current_count}")

	#Actualizamos la palabra actual y su conteo
        current_word = word
        current_count = count

#Despues de salir el bucle, imprimimos la ultima palabra procesada
if current_word == word:
    print(f"{current_word}\t{current_count}")
