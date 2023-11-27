###  Adivinar un número ###
###Escribe un programa que elija al azar un número entre el uno y el diez, 
### que le pregunte al jugador un número y que compruebe si has acertado o no.

## Elegir número, requiere paquetería
numero_azar=8

## Preguntar número a usuario
numero_usuario=int(input("Adivine un número entre el 0 y el 10"))
    # línea 8-"int" porque debemos convertir en un valor numérico la respuesta, "input" para que oedirle al usuario 
    # que ingrese el valor (python siempre toma "input" como cadema de texto). 

## Comparar valores e indicar si son el mismo
if numero_usuario==numero_azar:
    print("¡Correcto! Adivinaste el número :)")
else:
    print("Incorrecto, el número al azar era:", numero_azar)
    # Usar "==" para comparar. Recordar estructura del "if", seguido de condición ":" y resultado eb siguiente columna 
    # indetado. 
#-----------------------------------------------------------------------------------------------------------------------------------------#
