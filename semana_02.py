#Ejercicio 1: Invertir una lista
numeros = [1, 2, 3, 4, 5]
ciudades = ['Bogotá', 'Rosario', 'San Fernando', 'San Miguel']
lista_vacia = [42]

def invertir_lista(lista):
    return list(reversed(lista))

print(invertir_lista(numeros))
print(invertir_lista(ciudades))
print(invertir_lista(lista_vacia))

#%%
#otra opcion
def invertir_lista(lista):
    l = lista.copy()
    res = []
    for i in range(len(lista)):
        res.append(l[len(l)-1-i])
    return res
print(invertir_lista(numeros))

#Ejercicio 2: Conjetura de Collatz

#version recursiva (llama de nuevo a la función), distinto a versión iterativa (bucle)
def collatz(n):
    if n == 1: 
        return 0
    else: 
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
        respuesta = collatz(n)
        return respuesta + 1
print(collatz(4))

#otra opción iterativa
def collatz(n):
    contador = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        contador += 1
    return contador
print(collatz(4))

#otra opción recursiva usando factorial
def factorial(n):
    if n == 1:
        res = 1
    else:
        res = n * factorial(n-1)
    return res
print(factorial(5)) 


#Ejercicio 3: Diccionarios

materias = {
        "Programación": ["Jueves", "19:00", "Aula 105", "Matías"],
        "Estadística": ["Sábado", "10:00", "Aula 300", "Victoria"],
        "Matemática": ["Martes", "20:00", "Aula 210", "Juan", "Viernes", "18:00"],
        "Economía": ["Lunes", "17:30", "Aula 305"],
        "Lengua": ["Miércoles", "10:30", "Aula 305"]
    }

def contar_definiciones(d):
    """
    dado un diccionario devuelve otro diccionario con las mismas claves y 
    para cada una de ellas la cantidad de definiciones que tiene.
    """
    resultado = {}
    for clave in d:
        valor = d[clave]
        resultado[clave] = len(valor)
    
    return resultado

contar_definiciones(materias)

def cantidad_de_claves_letra(d, l):
    """
    dado el diccionario d devuelve la cantidad de entradas (claves) que comienzan con la letra l.
    """
    entradas_l = 0
    for clave in d:
        if clave[0] == l:
            entradas_l += 1
    return entradas_l
cantidad_de_claves_letra(materias,"E")

#Ejercicio 4: Propagación

def propagar(L):

    n = len(L)
    
    for i in range(n):
        if L[i] == 1:
            j = i + 1  # verificar a la derecha
            while j < n and L[j] == 0: #no contamos más allá del límite de la lista y el fósforo tiene que estar apagado para propagarse
                L[j] = 1
                j += 1
            
            j = i - 1 # verificar a la izquierda
            while j >= 0 and L[j] == 0: #no contamos más allá del límite izq de la lista  y el fósforo tiene que estar apagado para propagarse
                L[j] = 1
                j -= 1
    
    return L


    # Ejemplo 1:
    lista1 = [0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
    resultado1 = propagar(lista1)
    print(f"Resultado: {resultado1}")
  
    # Ejemplo 2:
    lista2 = [0, 0, 0, 1, 0, 0]
    resultado2 = propagar(lista2)
    print(f"Resultado: {resultado2}")
