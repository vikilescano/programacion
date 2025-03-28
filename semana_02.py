#Ejercicio 1: Invertir una lista
numeros = [1, 2, 3, 4, 5]
ciudades = ['Bogotá', 'Rosario', 'San Fernando', 'San Miguel']

def invertir_lista(lista):
    return list(reversed(lista))

print(invertir_lista(numeros))
print(invertir_lista(ciudades))



#Ejercicio 2: Conjetura de Collatz

def collatz(nro):
    nro = int(nro)
    if nro <= 0:
        print(f"el número debe ser mayor a 0")
    else:
         lista_numeros = [nro]
         while  nro != 1:
            if nro % 2 == 0: 
                nro = nro//2
            else:
                nro = nro * 3 + 1
            lista_numeros.append(nro)  
    return lista_numeros  

print(collatz(20)) 



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
