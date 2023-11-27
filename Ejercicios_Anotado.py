###  ADIVINAR UN NÚMERO ###
### Escribe un programa que elija al azar un número entre el uno y el diez, 
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
#### PAR O IMPAR ###
#### Crea un programa que pida un número entero y que devuelva si es par o impar

## Pedir número a usuario
numero=int(input("Elija un número entero: ")) 

## Verificar si número es par o impar
residual=numero%2
if residual==0:
    print("El número que eligió es un número par")
else:
    print("El número que eligió es un número impar")
    #Se utilizó la operación "%" ya que esta devuelve el residual de una división. Al dividir un número par entre 2 no existe residual.
#-----------------------------------------------------------------------------------------------------------------------------------------#
#### PALINDROMOS ####
### Escribe un programa que compruebe si una palabra es palindrómica o no

# Palindrómica= Se escribe igual al derecho y al revés

## Pedir palabra al usuario:
palabra=input("Escriba una palabra: ")

## Invertir palabra
palabra_inversa=reversed(palabra)
palabra_inversa= "".join(palabra_inversa)
    # "reversed" no genera una cadena de texto por lo que especificamos que la "palabra_inversa" sea una variable tipo
    # texto "" a la que agregamos ".join" el resultado de aplicar "reversed" a la palabra. 

## Comparar palabras
if palabra==palabra_inversa:
    print("La palabra es palindroma! :)", palabra, palabra_inversa)
else:
    print("La palabra no es palindroma :( ", palabra, palabra_inversa)
#-----------------------------------------------------------------------------------------------------------------------------------------#
### SITIO DE RESTRICCIÓN ###
### Busca el sitio de restricción en una secuencia de ADN

## Pedir secuencia al usuario
secuencia=input("Introduzca una secuencia de ADN: ")
secuencia=secuencia.upper()
    # Recordar que el método ".upper" debe ir seguido de un ()

## Pedir sitio de restricción al usuario
sitio_restriccion=input("Introduzca un sitio de restricción: ")
sitio_restriccion=sitio_restriccion.upper()

## Reconocer sitio de restricción
posicion=secuencia.find(sitio_restriccion)+1

## Imprimir posiciión de sitio de restricción si se encuentra
if posicion==0:
    print("No se encontró el sitio de restricción especificado en la secuencia :( ")
else:
    print("El primer sitio de restricción reconocido en la secuencia se encuentra en el nucleotido con posición:"
          ,posicion)
#-----------------------------------------------------------------------------------------------------------------------------------------#
