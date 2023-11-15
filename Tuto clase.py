string = 'ejemplo'
#Un string es una variable tal cual, pueden ser numeros, una palabra, una frase o lo que sea. Si son numeros, y queremos que se comporten
#como tal, tenemos que decirselo, porque si no no lo identificara como tal. Un ejemplo es "int" (entero). 
numero = int(8)
#Todo lo que queramos que se ponga tal cual, tenemos que ponerlo entre comillas (''), si no el programa piensa que es una variable a la que 
#estas haciendo referencia, a excepcion de los numeros, como el ejemplo de arriba.

#Luego tenemos las listas, que se hacen con los corchetes []. Lo mismo, hay que usar las comillas siempre que queramos algo tal cual. 
lista = ['a', 'b', 'c']

#La diferencia es que esta segmentado, tenemos 3 "apartados" a los que podemos llamar independientemente o todas a la vez.

#Para pedir tanto un string como una lista se usa el comando "print()". Si ponemos "print(lista)" nos va mostrar la variable que hemos
#definido arriba como "lista". Si pusiesemos "print('lista')" literalmente devolveria "lista" porque las comillas hacen que nos de algo tal
#cual. Para ver el ejemplo copiad y pegad esto en https://pythontutor.com/render.html#mode=edit :
ejemplo_lista = ['Esto', 'es', 'un', 'ejemplo']

print(ejemplo_lista)

print('ejemplo_lista')

#Si queremos solo una letra de un string, o una de las palabritas que hay en una lista, tenemos que anadir los corchetes al final de la
#variable que estamos llamando. Ejemplo: print(ejemplo[0]). Ademas de pedir una posicion en concreto, podemos decirle que nos diga de la
#segunda palabra a la tercera. Ejemplo: print(ejemplo[1:3]). Si os fijais, para llamar de la segunda a la tercera, uso "1" y "3". Esto es
#porque la primera posicion siempre corresponde al 0, de forma que la segunda posicion seria el 1. Como quiero que solo llegue hasta la
#tercera posicion, el segundo numero que pongo es un "3". Si contamos desde el 0, esto corresponde a la cuarta posicion en la lista, y como
#NO va a coger lo que haya en esta posicion, cogera la posicion 2 y 3 solo. Para ver un ejemplo copiar y pegar lo siguiente en
# https://pythontutor.com/render.html#mode=edit .

ejemplo_lista = ['Esto', 'es', 'un', 'ejemplo']
print(ejemplo_lista[1:3])

#Si queremos hacer lo mismo para un string en el que queremos que nos diga solo el caracter que hay en una posicion en concreto o en unas
#posiciones en concreto, se hace exactamente igual:

ejemplo_string = 'Ejemplo'

print(ejemplo_string[3:6])

#Para anadir algo a un string se usa el simbolo de suma (+). Para ver un ejemplo poner lo siguiente en https://pythontutor.com/render.html#mode=edit .
ejemplo_string = 'Ejemplo'
print(ejemplo_string)
ejemplo_string = ejemplo_string+' esto lo anado ahora'
print(ejemplo_string)

#Para hacer esto en una lista, tenemos que usar el comando "append()". Para ver un ejemplo poner lo siguiente en https://pythontutor.com/render.html#mode=edit .
ejemplo_lista = ['Esto', 'es', 'un', 'ejemplo']
print(ejemplo_lista)
ejemplo_lista.append('Esto lo anado ahora')
print(ejemplo_lista)

#Los diccionarios son como listas organizadas. Utilizamos llaves "{}". Tenemos 2 columnas, la de la izquierda son las "keys" y las de la derecha son "valores", y
#estan relacionados. Para que nos diga un valor, en este caso, tenemos que pedirle la "key" correspondiente, otra vez usando los corchetes. Es
#decir, tenemos los valores vinculados a sus 'keys', por lo que para ver un valor, le pedimos una 'key'. Para ver un ejemplo poner lo siguiente en 
# https://pythontutor.com/render.html#mode=edit .
ejemplo_diccionario = {
  'primero': 1,
  'segundo': 2,
  'tercero': 3
}
print(ejemplo_diccionario['primero'])

#Para anadir es muy sencillo, solo teneis que poner el nombre del diccionario con la nueva 'key' y decirle a que es igual:
ejemplo_diccionario['cuarto'] = 4

#Eso son todos los grupos que vamos a ver en clase (creo). 
#If es solo una condicion. Le dices al programa que SI se cumple una condicion, haga algo. Todo lo que este tabulado o indentado
#(que este movido hacia la derecha) esta dentro del if, y solo se lee si se cumple la condicion. Ademas de esto, podemos poner un
#'else', que literalmente significa que si no se cumple la otra, se lea esta por defecto. Tambien esta el 'elif', por si queremos 
#poner 2 condiciones distintas.
# Para ver un ejemplo poner lo siguiente en https://pythontutor.com/render.html#mode=edit .

numero = int(3) 
if numero == 1 :
  print('el numero es uno')
elif numero == 2:
  print('el numero es 2')
else :
  print('el numero no es uno')

#Luego estan 'for' y 'while', que son bucles. Mientras se cumplan, seguira haciendo lo que haya dentro. 
# Para ver un ejemplo poner lo siguiente en https://pythontutor.com/render.html#mode=edit .

ejemplo = 'ABCDEF'

for letra in ejemplo : #esto basicamente le dice que por CADA letra que hay en la variable, haga algo.
  print(letra) #como cada vez que se cumpla el bucle, esta haciendo referencia a una letra, cada vez imprime la letra por la que vamos (en orden).

#Si en vez de un string tuviesemos una lista, el 'for' se haria con cada cosa que haya dentro de la lista. Ejemplo:

lista = ['a', 'b', 'c']

for elemento in lista : 
  print(elemento)

#El 'strip' que no se entendio en clase el otro dia lo unico que hace es quitar elementos no visibles (espacios, tabulaciones, intros)
#que haya al principio y al final de una variable. Ejemplo:

variable = '       hola           ' #veis que hay un monton de espacios delante y detras de la palabra?
print(variable)
variable = variable.strip() #lo ponemos asi porque quita los espacios pero NO los guarda. Si ponemos variable = a la variable pero sin los espacios, guarda la nueva variable sobre la que ya tenemos, la sobreescribe.
print(variable)
