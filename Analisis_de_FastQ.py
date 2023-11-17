### Programa para analizar un archivo fastq local especificado por el usuario. Devuelve Nombres de secuencias, largo, 
    # calidad media y %GC.
## Emanuele De Stefano- 17/11/2023

# Crear función "analizar_archivo_fastq"
def Analizar_archivo_fastq(archivo):
    # Crear diccionario "{}" en el que se almacenarán los 4 resultados. De momento vacía, se irá completando conforme se 
    # aplique la función.
    resultados = {"Name": [], "Length": [], "Qual": [], "%GC": []}

    # Abrir archivo y leerlo. "with" cerrará el archivo tras terminar, liberando memoria. "open" abre el archivo dentro
    # del parentesis. Argumento "r" especifíca que el archivo se leera (read). "archivo" será la variable asignada
    # al archivo.  "lineas" será una lista en la que se añade cada línea del archivo como una variable independiente
    # esto es útil porque cada linea del archivo fastq contiene información distinta. La 1 siempre es el nombre por ej
    # así que podemos referirnos a esa línea como la posición 0,4,8 etc... en la lista.
    with open(archivo, "r") as archivo:
        lineas = archivo.readlines()

    # Crear variable i (index) para que el ciclo a continuación se ejecute linea por linea. 
    i = 0
    # Importante recordar que el bucle solo se ejecute hasta terminar todas las líneas, para detenerlo. 
    # "len" (length) leera la cantidad de variables contenida en la lista "lineas"
    while i < len(lineas):

        # Obtener nombre ("Name") de secuencias. Si línea actual "lineas[i]" empieza con "@seq" corresponde a linea
        # del nombre. ".strip()" solo elimina todos los espacios en blanco y "[1:]" se utiliza para empezar a
        # agregar al nombre desde el segundo caracter, porque el nombre no debe incluir la @. Se agrega a la
        # variable "Name" de la cadena "resultados" la variable "nombre". 
        if lineas[i].startswith("@seq"):
            nombre = lineas[i].strip()[1:]
            resultados["Name"].append(nombre)

            # Obtener longitud de secuencia. Denominar a la linea siguiente de la actual como secuencia y remover 
            # espacios en blanco. Crear variable longitud  que cuente la length "len" de dicha linea y agregar a variable
            # "Length" de diccionario "resultados"
            secuencia = lineas[i + 1].strip()
            longitud = len(secuencia)
            resultados["Length"].append(longitud)

            # Calcular el porcentaje de GC. En esa misma línea, crear variable que cuente total de G y C. 
            # "sum" sumara, "nucleotido in "CG"" simplemente crea un TRUE que hará que lo siguiente solo aplique
            # si el nucleotido en esta línea "secuencia" es C o G. El resto se explica por si solo.
            conteo_gc = sum(nucleotido in "CG" for nucleotido in secuencia)
            porcentaje_cg = (conteo_gc / longitud)
            resultados["%GC"].append(porcentaje_cg)

            # Traducir información de calidad y obtener calidad media. La 3 línea despues del nombre corresponde al 
            # la línea de calidad. A cada caracter en esa linea se le asigna un valor numérico transformando el 
            # caracter ASCI en un número mediante la función "ord" y después restandole 64. Se obtiene la media, sumando
            # todos los valores y dividiendo por el número de valores (length de linea de valores).
            linea_calidad = lineas[i + 3].strip()
            valores_calidad = [ord(caracter) - 64 for caracter in linea_calidad]
            calidad_media = sum(valores_calidad) / len(valores_calidad)
            resultados["Qual"].append(calidad_media)

            # Incrementar el índice. Una vez se han analizado todos las líneas correspondientes a una secuencia se pasa 
            # a la siguiente secuencia, la cuál debería de estar 4 líneas después de la anterior, según el formato fastq.
            i += 4

    # Devolver lcomo output el diccionario "resultados"
    return resultados
#------------------------------------------------------------------------------------------------------------------#
# Pedir al usuario que ingrese el nombre del archivo fastq a analizar
archivo = input("Ingrese el nombre del archivo FastQ: ")

# Llamar a la función, aplicarla sobre el archivo y obtener los resultados
resultados = Analizar_archivo_fastq(archivo)

# Imprimir los resultados. 
print(resultados)
