# Para crear textos largos o en distintas lìneas usar 3 comillas. Todo lo que este dentro de esas tres comillas 
# al inicio y al final se guardara en una misma cadena de texto.
Texto= """ Hola

Caracola """
print(Texto)

# Funciones
s= "Hola"

def saluda_al_usuario(usuario):
    print(s, usuario[0], usuario[1])

usuario= ["Jose", "Perez"]
saluda_al_usuario(usuario)
print(usuario)

#Metodos van despues de un objeto, despues de "."
print("Metodos")
print(s.upper())
print(s.lower())
print(s.strip())
print(s.count("o"))
print(s.replace("o","0"))
print(s.find("l"))
print(s.split())

#Indexado. Sirve igual en cadenas de texto y listas
print("Indexado")
print(s[2])
print(s[1:3])
print(s[:]) #Todo
print(s[:-1])#Solo ultimo
print(s[::3])#Saltandose de 3 en 3
print(s[::-1])#Bro esto hace el reverso sin tener que usar funcion "reversed"

#Dato extra, ciualquier objeto vacio es False y si contiene algo es TRUE

#Append . Una lista puede contener otras listas. Allgo parecido a una lista pero inmutable es la tupla (,,,)
l= [1, "hola", True, None]
print(l)

l.append(3)
# NO ASI l=l.append(3) porque te daria NONE ya que una lista es mutable
#f string. Esto te imprime Nombre y luego la variable a Apellido y la variable b. Y asi...
#d= f"Nombre:{a}, Apellido: {b}"
#print(d)

# Reversed no devuelve una lista sino uno iterador, asi que de ahuevo hay que especificarle que el output te lo de
# como lista
print(list(reversed(l)))
#con cadena de texto hay que pasarlo a texto 
print("".join(reversed("Hola")))
# Clase- nuevo objeto que junto los datos con la aciòn que se hara sobre lso datos. Porgramacion orientada a objetos.