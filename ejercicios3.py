--------------------------cristian---------------------------
# 1. Crear una variable que contenga tu nombre y mostrarlo.
nombre = "Alexis"
print(f'Tu Nombre: "{nombre}"')

# 2. Crear una variable que contenga tu edad y mostrarla.
a = 25
edad = a
print(edad)

# 3. Comprobar si tu edad es mayor de 18 y mostrar un mensaje.
edad = 19
if  edad > 18 :
    resultado = "Eres mayor de edad"
else:
    resultado = "Eres menor de edad"
print(resultado)

# 4. Comprobar si tu edad es igual a 18 y mostrar un mensaje.
edad = 18
if edad == 18 :
    resultado = "Tienes 18 años"
else:
    resultado = "error"
print(resultado)

# 5. Crear una lista de números del 1 al 5 y mostrarla.
numeros = [1, 2, 3, 4, 5]
print( numeros)

# 6. Sumar todos los números de la lista y mostrar el resultado.
suma_numeros = sum(numeros)
print(suma_numeros)

# 7. Crear un diccionario con información personal y mostrarlo.
informacion_personal = {"nombre": "Alexis clemente", "edad": 25}
print(informacion_personal)

# 8. Acceder a un valor en el diccionario y mostrarlo.
nombre = informacion_personal["nombre"]
print(nombre)

# 9. Crear un bucle que imprima los números del 1 al 10.
for i in range(1, 11):
    print(i, end=", ")
print() 

# 10. Crear un bucle que imprima solo los números pares del 1 al 10.
for i in range(1, 11):
    if i % 2 == 0:
        print(i, end=", ")
print() 

# 11. Crear una lista de frutas y mostrar solo las que empiezan con 'a'.
frutas = ["manzana", "pera", "aguacate", "banana"]
frutas_a = [fruta for fruta in frutas if fruta.startswith('a')]
print(f'{", ".join(frutas_a)}')

# 12. Crear un bucle que imprima los elementos de una lista con su índice.
lista = ['0: "manzana", 1: "pera", 2: "aguacate", 3: "banana"']
menu = lista
print(menu)

#13. Crear un conjunto de números y mostrarlo.
conjunto = {1, 2, 3, 4, 5}
print(conjunto)

# 14. Comprobar si un número está en el conjunto (set) y mostrar un mensaje.
numero = 3
if numero in conjunto:
    print(f"{numero} está en el conjunto.")
else:
    print(f"{numero} no está en el conjunto.")


#15. Crear un bucle que imprima los números del 10 al 1 en orden descendente.
for i in range(10, 0, -1):
    print(i, end=", " if i > 1 else "\n")

## 16. Crear una función que reciba dos números y devuelva su suma.
def suma(a, b):
    return a + b

resultado = suma(3, 5)
print(f"suma(3, 5) devuelve {resultado}.")



-----------------------------nelly----------------------------
# 17. Crear una función que reciba una lista y devuelva su longitud.
def longitud_lista(lista):
    return len(lista)


# 18. Crear una función que determine si un número es par.
def es_par(numero):
    return numero % 2 == 0
print(es_par(4))
print(es_par(3))

# 19. Crear una función que reciba un diccionario y devuelva solo sus claves.
def obtener_claves(diccionario):
    return list(diccionario.keys())
mi_diccionario = {"nombre": "juan", "edad": 30}
print(obtener_claves(mi_diccionario))

# 20. Crear una lista de números y mostrar solo los que son mayores que 5.
numeros = [1, 4, 5, 7, 9, 2]
mayores_que_5 = [num for num in numeros if num > 5]
print(mayores_que_5)

# 21. Crear una lista de palabras y mostrar su longitud total.
palabras = ["hola", "mundo", "python"]
longitud_total = sum(len(palabra) for palabra in palabras)
print(longitud_total)

# 22. Contar cuántas veces aparece un elemento en una lista.
elementos = ["a", "b", "a", "c"]
conteo_a = elementos.count("a")
print(conteo_a)

# 23. Crear una lista de números y calcular el promedio.
numeros = [1, 2, 3, 4, 5]
promedio = sum(numeros) / len(numeros)
print("promedio")


# 24. Crear un diccionario y agregar un nuevo elemento.
mi_diccionario = {"nombre": "Juan"}
mi_diccionario = ["edad"] = 25
print(mi_diccionario)

#25
diccionario = {"nombre": "Juan", "edad": 30}
del diccionario["edad"]
print(diccionario)

#26
for i in range(1, 6):
    print(i**2, end=", ")


#27
fibonacci = [0, 1]
for i in range(2, 10):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print(fibonacci)


#28
lista = [1, 2, 3, 4, 5]
if 3 in lista:
    print("3 está en la lista.")
else:
    print("3 no está en la lista.")


#29
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


#30
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

print(es_primo(7))  # Resultado esperado: True


#31
for i in range(1, 21):
    if i == 3:
        print("Fizz")
    elif i == 5:
        print("Buzz")
    else:
        print(i)



#32
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
----------------------------maricruz---------------------------
#ejercicio 33
numeros = [1, 2, 3, 4, 5]
resultado = list(map(lambda x: x * 2, numeros))
print(resultado)

#Ejercicio 34
numeros = [1, 2, 3, 4, 5, 6]
resultado = list(filter(lambda x: x % 2 == 0, numeros))
print(resultado)

#Ejercicio 35 
palabras = ["Hola", "mundo"]
resultado = " ".join(palabras)
print(resultado) 

#ejercicio 36
numeros = [1, -2, 3, -4, 5]
resultado = [x for x in numeros if x < 0]
print(resultado)

#Ejercicio 37
conjunto1 = {'a', 'b', 'c'}
conjunto2 = {'c', 'd', 'e'}
resultado = sorted(conjunto1.union(conjunto2))
print(resultado)

#Ejercicio 38
conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}
resultado = conjunto1.intersection(conjunto2)
print(resultado)

#Ejercicio 39
mi_diccionario = {"a": 1, "b": 2}
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}", end=" ")

#Ejercicio 40
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in cadena if letra in vocales)
print(contar_vocales("Hola"))

#Ejercicio 41
import random
numeros_aleatorios = [random.randint(1, 100) for _ in range(10)]
print(numeros_aleatorios)

#Ejercicio 42
numeros = [5, 3, 1, 4, 2]
numeros.sort()
print(numeros)

#Ejercicio 43
mi_diccionario = {"a": 1, "b": 2}
clave = "a"
if clave in mi_diccionario:
    print(f"La clave '{clave}' existe.")

#Ejercicio 44
numeros = [1, 2, 3]
for numero in reversed(numeros):
    
    print(numero, end=" ")

#Ejercicio 45
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(factorial(5))

#Ejercicio 46
tuplas = [(1, 'a'), (2, 'b')]
for numero, letra in tuplas:
    print(f"{numero}: {letra}", end=" ") 
    
#Ejercicio 47
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
resultado = list(zip(lista1, lista2))
print(resultado, end=" ")

#Ejercicio 48
def convertir_lista_a_mayusculas(lista):
    return [cadena.upper() for cadena in lista]
print(convertir_lista_a_mayusculas(["hola"]))
---------------------------fernando----------------------------
# 49. Crear una lista de números y devolver la suma de los números negativos.
numeros = [1, -2, 3, -4, 5]

suma_negativos = sum(num for num in numeros if num < 0)
print(suma_negativos)

# 50. Crear un programa que imprima los números del 1 al 100, pero resalte los múltiplos de 3 y 5.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    elif i % 3 == 0:
        print(f"3:{i}")
    elif i % 5 == 0:
        print(f"6:{i}")
    else:
        print(i)


#Ejercicio 51
nombres = ["Juan", "Alejandro", "Maria"]
contador = sum(1 for nombre in nombres if len(nombre) > 5)
print(contador)

#Ejercicio 52
for i in range(1, 6):
    print(f"Tabla del {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

#Ejercicio 53
def invertir_lista(lista):
    return lista[::-1]

print(invertir_lista([1, 2, 3]))

#Ejercicio 54
suma_pares = sum(i for i in range(1, 101) if i % 2 == 0)
print(suma_pares)

#Ejercicio 55
mi_diccionario = {"a": 5, "b": 15, "c": 20}
resultado = {k: v for k, v in mi_diccionario.items() if v > 10}
print(resultado)

#Ejercicio 56
from functools import reduce
numeros = [1, 2, 3, 4]
resultado = reduce(lambda x, y: x * y, numeros)
print(resultado) 

#Ejercicio 57
def maximo(lista):
    return max(lista)
print(maximo([1, 2, 3]))

#ejercicio 58
cadena = "Hola"
for char in cadena:
    print(char, end=" ")

#Ejercicio 59 
numeros = [10, 20, 30]
suma = sum(numeros)
resultado = suma > 50
print(resultado) 


#Ejercicio 60
def contar_consonantes(cadena):
    consonantes = "bcdfghjklmnpqrstvwxyz"
    return sum(1 for letra in cadena.lower() if letra in consonantes)

print(contar_consonantes("Hola"))
#Ejercicio 61
numeros = [5, 1, 3, 4, 2]
segundo_mayor = sorted(set(numeros))[-2]
print(segundo_mayor)

#Ejercicio 62
palabras = ["mesa", "silla", "ventana", "puerta"]
contador = sum(1 for palabra in palabras if 'e' in palabra)
print(contador)

#Ejercicio 63. Crear una lista de enteros y devolver una nueva lista con los elementos únicos.
numeros = [1, 2, 2, 3, 4, 4, 5]
# Resultado: [1, 2, 3, 4, 5]

def eliminar_duplicados(lista):
    return tuple(set(lista))

print(eliminar_duplicados(numeros))

#Ejercicio 64. Crear una función que reciba una lista y devuelva una lista con los elementos duplicados.
def duplicados(lista):
    duplicados = set()
    vistos = set()
    
    for elemento in lista:
        if elemento in vistos:
            duplicados.add(elemento)
        else:
            vistos.add(elemento)
    
    return list(duplicados)

resultado = duplicados([1, 2, 2, 3])
print(resultado) 