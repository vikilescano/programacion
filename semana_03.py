import random

# Ejercicio 1: crear album con espacios para figus
def crear_album(figus_total):
    return [0] * figus_total

# Ejercicio 2
def album_incompleto(A):
    return 0 in A

# Ejercicio 3: comprar una figurita
def comprar_figu(figus_total):
    return random.randint(0, figus_total-1)

# Ejercicio 4: cuantas figus se deben comprar para completar el álbum
def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    contador_figus = 0
    while album_incompleto(album):
        figu = comprar_figu(figus_total)
        album[figu] += 1
        contador_figus += 1
    return contador_figus

#Ejercicio 5 al final (simulaciones)

# Ejercicio 6
def experimento_figus(n_repeticiones, figus_total):
    resultados = []
    for i in range(n_repeticiones):
        resultados.append(cuantas_figus(figus_total))
    promedio = sum(resultados) / n_repeticiones
    return promedio

#Ejercicio 7 al final (simulaciones)

# Ejercicio 8
def comprar_paquete(figus_total, figus_paquete):
    paquete = []
    for i in range(figus_paquete):
        figurita = random.randint(0, figus_total-1)
        paquete.append(figurita)
    return paquete

# Ejercicio 9
def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    contador_paquetes = 0
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for figu in paquete:
            album[figu] += 1
        contador_paquetes += 1
    return contador_paquetes

#Ejercicio 10 al final (simulaciones)

# Ejercicios con simulaciones
if __name__ == "__main__":
    # Ejercicio 5
    figus_total = 6
    n_repeticiones = 1000
    resultados = []
    for i in range(n_repeticiones):
        resultados.append(cuantas_figus(figus_total))
    promedio = sum(resultados) / n_repeticiones
    print(promedio)
    
    # Ejercicio 7 
    figus_total = 860
    figus_paquete = 5
    paquete = []
    for i in range(figus_paquete):
        figurita = random.randint(0, figus_total-1)
        paquete.append(figurita)
    print(paquete)
    
    # Ejercicio 10
    figus_total = 860
    figus_paquete = 5
    n_repeticiones = 100
    resultados = []
    for i in range(n_repeticiones):
        paquetes = cuantos_paquetes(figus_total, figus_paquete)
        resultados.append(paquetes)
    promedio_paquetes = sum(resultados) / n_repeticiones
    print(promedio_paquetes)