Link de problemas: https://bioinf.comav.upv.es/courses/intro_python/soluciones.html

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
    # El método ".find" sirve para encontrar la posición en la que se encuentra un objeto dentro de otro. Agregamos "+1"
    # porque python empieza con la primera posición como "0" lo cuál no hace sentido para nosotros.

## Imprimir posiciión de sitio de restricción si se encuentra
if posicion==0:
    print("No se encontró el sitio de restricción especificado en la secuencia :( ")
    # Cuando ".find" no encuentra el objeto regresa valor "0"
else:
    print("El primer sitio de restricción reconocido en la secuencia se encuentra en el nucleotido con posición:"
          ,posicion)
    # Lamentablemente ".find" solo regresa la primer posición que encuentre.
#-----------------------------------------------------------------------------------------------------------------------------------------#
### FRIO O CALIENTE ###
### Escribe un programa que pregunte al usuario la temperatura actual y que responda diciendo si hace frío o calor

## Preguntar temperatura actual a usuario
temperatura=int(input("¿Cuál es la temperatura actual en °C?"))

## Comparar temperatura actual con calor o frio
if temperatura>= 40:
    print("¡Vaya! Hace mucho calor")
elif temperatura>= 30:
    print("Hace calor :(")
elif temperatura>= 20:
    print("¡Qué agradable! La temperatura actual es templada")
elif temperatura>= 10:
    print("Está haciendo frio!")
elif temperatura < 10:
    print("¡Está haciendo muchisimo frío! Hay que abrigarse")
else:
    print("Disculpa, la temperatura que ingresaste sale de ims registros :(")
    # Es importante poner las temperaturas en orden ya que python revisa una condición una por una
#-----------------------------------------------------------------------------------------------------------------------------------------#
### DIVIDIR CADENA DE TEXTO ###
### Escribe un programa que elimine un número determinado de letras, el que se le pida en una variable, 
### de una cadena de texto e imprima el resultado.

## Pedir cadena de texto al usuario
texto=input("Introduzca un texto: ")

## Preguntar al usuario cuántas letras desea eliminar
eliminar=int(input("¿Cuántas letras y espacios dese eliminar del texto? "))

## Crear nuevo texto recortado
texto_recortado=texto[:-eliminar]
    # Los cochetes "[]" indican la posición del objeto "texto" a los que nos queremos referir. El ":" indica TODO y "-" contará desde la
    # posisción final. "eliminar" indicará cuantas letras o espacios desde el final. Es decir conservaremos todo el texto menos lo borrado
print(texto_recortado)
#-----------------------------------------------------------------------------------------------------------------------------------------#
### ESCRIBE ASTERISCOS ###
### Escribe un programa que pida un número e imprima ese mismo número de asteriscos “*”. 
### (Puedes utilizar la función range)

## Pedir número de asteriscos a escribir a ususario
numero=int(input("¿Cuántos asteriscos deseas que el programa escriba? "))

## Imprimir numero de asteriscos (pero poniendo un límite para no tronar la computadora)
if numero <= 100:
    print("*"*numero)
else:
    print("Número demasiado grande :( ")
    # Multiplicamos el caracter a escribir ""*"" por el número solicitado "* numero"
#-----------------------------------------------------------------------------------------------------------------------------------------#
### ELIMINA LETRAS ### 
### Escribe un programa que elimine algunas letras de una cadena de texto, las que le des en una lista, 
### utilizando un bucle for.

## Pedir texto a usuario
texto_original=input("Introduzca el texto: ")

## Pedir a usuario palabras a eliminar
eliminar=input("Introduzca la lestras que desea eliminar del texto anterior: ")

## Crear un nuevo texto a partir "texto" que omita las letras contenidas en "eliminar"
nuevo_texto=""
for letras in texto_original:
    if letras not in(eliminar):
        nuevo_texto+=letras
    # Analisamos letra por letra del "texto_original" mediante el "for" "in". Si esa "letra" NO se encuentra en las 
    # letras a "eliminar" entonces la añadimos al "nuevo_texto" mediante el operador "+=". 
    
## Imprimir texto nuevo
print(nuevo_texto)
#-----------------------------------------------------------------------------------------------------------------------------------------#
### ESCRIBE NUMERO REVERSO ###
### Escribe un programa que genere el número con las cifras al revés separadas por espacios. 
### Por ejemplo, si le das “7563” el resultado debería ser “3 6 5 7”.

## Pedir número al usuario:
numero=input("Introduzca un número: ")

## Revertir el número
numero_reverso=" ".join(reversed(numero))
print(numero_reverso)
    # El "numero_reverso" se crea añadiendo carácteres separados por espacio " " (Ojo, hay un espacio dentro de las 
    # comillas). Los caracteres a añadir son los mismos que los del "numero" original pero revertidos "reversed". 
#-----------------------------------------------------------------------------------------------------------------------------------------#
