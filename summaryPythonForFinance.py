# -*- coding: utf-8 -*-
"""
Python para finanzas - RIC
Andres F Molina Navia
Resumen.

En la sesión del 6 de octubre resaltamos puntualmente que para ser programadores
partimos de la forma en la que "piensa"una máquina y que se resumen en tres etapas:
    
    Input ----> Processing ----> Output 
    
El fin de todo algoritmo está en generar un resultado como calcular tus impuestos,
ordenar las imágenes en tu feed de instagram, sugerir una canción en tu lista de reproducción,
el resultado de una busqueda, poner una orden de compra, pedir un domicilio, etc.


En una escala mucho más pequeña replicamos esta lógica suministrando datos de
diferente fuente y tipo, posteriormente realizamos operaciones con ellos y generamos un output
que sea de nuestra utilidad.

En este sentido los inputs pueden que ingresan a nuestro algoritmo pueden venir
de forma interna o de forma externa. En esta primera etapa exploramos la forma interna,
realizamos operaciones con estos inputs y generamos resultados utiles en un contexto. 

Con input o entrada de datos, también es sinonimo de variable. En python existen dos gropus grandes 

* Tipos de datos simples: numeros, string, bool, char.
* Tipos de datos compuestos: Listas, tuplas,  diccionarios, arrays. 



Nota 1: con el propósito de llevar un order y con sigo una fácil interpretación del código,
cada variable declarada seráde la forma camelCase ejemplo

ingresoUno = ...
cantidadZapatos = ...
nombreEstudiante = ....

Nota 2: Para visualizar el resultado de nuestros procesamiento de datos en consola ==>
utilizamos la función print()
"""
###############################################################################
###Inputos - tipos de variables
##Tipos de datos simples.
###############################################################################
#Numericos

edad=18
pesoKg = 80

print(edad)
#Con la función type podemos retornar el tipo de dato
print(type(edad))
"""
Operaciones con números.
+ suma.
- resta.
* multiplicación.
/ División.
% Residuo.
"""
print("Operación suma: ",edad+1)
print("Operación Resta: ",edad-1)
print("Operación multiplicación: ",edad*2)
print("Operación división: ",edad/2)
print("Operación residuo: ",edad%2)

#String
nobresEstudiante = "Maria Antonia"
apellidosEstudiante = " Molina Navia"
a = '''Utilizando triple comilla podemos generar parrafós, 
la forma en la que se defina literalmente la variable será almacenada.'''

print("######################################################################")
print(nobresEstudiante)
print(apellidosEstudiante)
print(a)
print(type(a))

"""
Operaciones con string.
cortar un string
Convertir en mayúsculas o minúsculas.
reemplazar letras
concatenar 
https://www.w3schools.com/python/python_strings_exercises.asp 
"""
intro = "Hello world"
print("Cortar un string: ", intro[0:3])
print("Convertir en mayúscula:", intro.upper())
print("Convertir en mayúscula:", intro.lower())
print("Reemplazar valores:", a.replace("a","4"))
print("Concatenar:", nobresEstudiante + apellidosEstudiante)



#Bool - siempre inician por mayúscula
mayorEdad = False
hombre = True
print("######################################################################")
print(mayorEdad)
print(hombre)

"""
Operaciones con bool.
and
or
not
"""
print("and: ",mayorEdad and hombre )
print("or: ",mayorEdad or hombre )
print("not: ",not hombre )


###############################################################################
###Inputos - tipos de variables
##Tipos de datos compuestos.
###############################################################################
#Listas

datosEstudiante = ["Andres", "Molina", 24,"Universidad del Rosario"]

print("Acceder a cada dato de forma individual: ", datosEstudiante[1])
"""
Operaciones con listas.
Agregar elementos a la lista       .append()
insertar en determinda posición    .insert(posición,elemento)
Remover element                    .remove()
Ordenar                            .sort()
"""

datosEstudiante.append("Bogotá")
datosEstudiante.insert(0, "Finanzas y comercio")
datosEstudiante.remove("Andres")
print(datosEstudiante)
#Tuplas
tupleEjemplo = ("apple", "banana", "cherry")

print(tupleEjemplo)

#Diccionario
dic = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(dic)
print(len(dic))

"""
Operaciones de un diccionario
Cambiar valores: 
Actualizar:
Agregar valores:

"""

#Matrices

array = [[1,2,3,4,5],[5,4,3,2,1]]
print(array)



###############################################################################
###Cragar inputs desde la consola
##
###############################################################################

nombrePersona = input("Ingresa tu nombre: " )
edadPersona = int(input("Ingresa tu edad: "))
esttura = float(input("Ingresa tu estatura: "))


###############################################################################
###Sentencias de control de flujo
##
###############################################################################


""""
De esta forma  podemos ingresar variables de forma manualmente, también es
cierto que podemos cargar archivos de excel, imágenes, textos, etc, pero esto
lo veremos más adelante.

Antes de esto debemos conocer las fariables de flujo, en el diagrama:
    
    Input ----> Processing ----> Output 
 
los controles de flujo junto a las operaciones son la parte de procesamiento 
que nuestro algoritmo va a realizar. Las declaraciones son las siguientes.

for, if, while

"""

# For es una forma de acceder a cada elemento, su significado es literal

frutas = ["apple", "banana", "cherry","Piña"]

for x in frutas:
    print(x)

#If es un condicinal en donde se verifica una condición

if edadPersona > 18:
    print("Sos mayor de edad")
else:
    print("Sos menor de edad")
    
#While es una herramienta para ejecutar una función una determinada cantidad de veces
    
count = 0

while count < 10:
    print("Hola mundo")
    count+=1

