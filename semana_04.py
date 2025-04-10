import csv
archivo = '/Users/vikilescano/Documents/doctorado/materias/programacion/arbolado-en-espacios-verdes.csv'


#Ejercicio 1
def arboles_parque(nombre_archivo, nombre_parque): 
    """
    Función que genera un diccionario con los árboles del parque indicado.
    Cada árbol se identifica por su id y contiene un diccionario con sus datos.
    
    Args:
        nombre_archivo: archivo
        nombre_parque: parque
        
    Returns:
        dic: Diccionario con los árboles del parque, donde la key es el id del árbol
    """
    arboles_dict = {}
    
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        
        for arbol in reader:
            if arbol['espacio_ve'] == nombre_parque:
                id_arbol = arbol['id_arbol']
                arboles_dict[id_arbol] = arbol
    
    return arboles_dict

#Ejercicio 2
def arbol_mas_popular(nombre_parque):
    """
    Función que devuelve el árbol más popular del parque indicado.
    
    Args:
        nombre_parque: parque (VA EN MAYUSCULA)
    Returns:
        arbol: árbol más nombrado
    """ 
    arboles = arboles_parque(archivo, nombre_parque)
    
    conteo_arboles = {}
    
    for arbol in arboles.values():
        especie = arbol['nombre_com']
        if especie in conteo_arboles:
            conteo_arboles[especie] += 1
        else:
            conteo_arboles[especie] = 1

    arbol_mas_popular = max(conteo_arboles, key=conteo_arboles.get)
    
    return arbol_mas_popular
#Ejercicio 3
def n_mas_altos(nombre_parque, n):
    """
    Devuelve los n árboles más altos del parque indicado.
    Args:
        nombre_parque: parque (VA EN MAYUSCULA)
        n: cantidad de árboles a devolver
    Returns:
        lista_arboles: lista con los IDs de los n árboles más altos
    """

    arboles = arboles_parque(archivo, nombre_parque)
    arboles_con_altura = [(id_arbol, float(arbol['altura_tot'])) 
                          for id_arbol, arbol in arboles.items()]    
    arboles_ordenados = sorted(arboles_con_altura, key=lambda x: x[1], reverse=True)

    lista_ids = [id_arbol for id_arbol, altura in arboles_ordenados[:n]]
    
    return lista_ids

#Ejercicio 4
def altura_promedio(nombre_parque, especie): 
    """
    Devuelve la altura promedio de una especie en un parque.
    
    Args:
        nombre_parque: parque (VA EN MAYUSCULA)
        especie: especie del árbol
    Returns:
        promedio: altura promedio de la especie
    """
    arboles = arboles_parque(archivo, nombre_parque)
    
    alturas = []
    
    for arbol in arboles.values():
        if arbol['nombre_com'] == especie:
            alturas.append(float(arbol['altura_tot']))
    
    if len(alturas) == 0:
        return None
    
    promedio = sum(alturas) / len(alturas)
    
    return promedio

#Ejercicio 5
def obtener_parques(nombre_archivo):
    """
    Obtiene la lista de todos los parques disponibles en el archivo,
    excluyendo 'S/D'.
    
    Args:
        nombre_archivo: ruta del archivo csv
    
    Returns:
        Conjunto con los nombres de todos los parques válidos
    """
    parques = set()
    
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        
        for arbol in reader:
            parque = arbol['espacio_ve']
            if parque != 'S/D':
                parques.add(parque)
    
    return parques

#Parques con mas arboles
def parques_con_mas_arboles(nombre_archivo):
    """
    Encuentra el/los parques con mayor cantidad de árboles.
    
    Args:
        nombre_archivo: ruta del archivo csv
    
    Returns:
        Lista con el/los parques con más árboles
        Cantidad de árboles
    """
    parques = obtener_parques(nombre_archivo)
    conteo_arboles = {}
    
    for parque in parques:
        arboles = arboles_parque(nombre_archivo, parque)
        conteo_arboles[parque] = len(arboles)
    
    max_arboles = max(conteo_arboles.values())
    parques_max = [parque for parque, cantidad in conteo_arboles.items() 
                  if cantidad == max_arboles]
    
    return parques_max, max_arboles
#Parques con arboles mas altos
def parques_con_arboles_mas_altos(nombre_archivo):
    """
    Encuentra el/los parques con árboles más altos en promedio.
    
    Args:
        nombre_archivo: ruta del archivo csv
    
    Returns:
        list: Lista con el/los parques con árboles más altos en promedio
        float: Altura promedio máxima
    """
    parques = obtener_parques(nombre_archivo)
    alturas_promedio = {}
    
    for parque in parques:
        arboles = arboles_parque(nombre_archivo, parque)
        alturas = [float(arbol['altura_tot']) for arbol in arboles.values()]
        alturas_promedio[parque] = sum(alturas) / len(alturas)
    
    max_altura = max(alturas_promedio.values())
    parques_max = [parque for parque, altura in alturas_promedio.items() 
                  if altura == max_altura]
    
    return parques_max, max_altura

#Parques con mas especies
def parques_con_mas_especies(nombre_archivo):
    """
    Encuentra el/los parques con mayor variedad de especies.
    
    Args:
        nombre_archivo: ruta del archivo csv
    
    Returns:
        Lista con el/los parques con más variedad de especies
    """
    parques = obtener_parques(nombre_archivo)
    variedad_especies = {}
    
    for parque in parques:
        arboles = arboles_parque(nombre_archivo, parque)
        especies = {arbol['nombre_com'] for arbol in arboles.values()}
        variedad_especies[parque] = len(especies)
    
    max_variedad = max(variedad_especies.values())
    parques_max = [parque for parque, variedad in variedad_especies.items() 
                  if variedad == max_variedad]
    
    return parques_max, max_variedad

#Especie con más ejemplares
def especie_mas_ejemplares(nombre_archivo):
    """
    Encuentra la especie que más ejemplares tiene en toda la ciudad.
    
    Args:
        nombre_archivo: ruta del archivo csv
    
    Returns:
        Nombre de la especie con más ejemplares
        Cantidad de ejemplares
    """
    conteo_especies = {}
    
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        reader = csv.DictReader(archivo)
        
        for arbol in reader:
            especie = arbol['nombre_com']
            if especie in conteo_especies:
                conteo_especies[especie] += 1
            else:
                conteo_especies[especie] = 1
    
    especie_max = max(conteo_especies.items(), key=lambda x: x[1])
    
    return especie_max[0], especie_max[1]

#Razon entre exoticas y autoctonas
def razon_exoticas_autoctonas(nombre_archivo):
    """
    Calcula la razón entre especies exóticas y autóctonas.
    
    Args:
        nombre_archivo: ruta del archivo csv
    
    Returns:
        Razón entre especies exóticas y autóctonas
    """
    parques = obtener_parques(nombre_archivo)
    conteo_origen = {"Exótico": 0, "Nativo/Autóctono": 0}
    
    for parque in parques:
        arboles = arboles_parque(nombre_archivo, parque)
        for arbol in arboles.values():
            origen = arbol['origen']
            if origen == "Exótico":
                conteo_origen["Exótico"] += 1
            elif origen == "Nativo/Autóctono":
                conteo_origen["Nativo/Autóctono"] += 1
    
    if conteo_origen["Nativo/Autóctono"] == 0:
        return "No hay especies nativas"
    
    razon = conteo_origen["Exótico"] / conteo_origen["Nativo/Autóctono"]
    
    return razon

### Pruebas
if __name__ == "__main__":
    with open(archivo, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            print(', '.join(row[:5]))  
            if i == 4:  
                break



arboles_parque(archivo, "CENTENARIO")
arbol_mas_popular("CENTENARIO")
arbol_mas_popular("BARRANCAS de BELGRANO")
n_mas_altos("CENTENARIO", 5)
n_mas_altos("BARRANCAS de BELGRANO", 4)
n_mas_altos("RIVADAVIA", 5)
altura_promedio("RIVADAVIA", "Eucalipto")
altura_promedio("CENTENARIO", "Eucalipto")
altura_promedio("RIVADAVIA", "Gomero")
altura_promedio("CENTENARIO", "Gomero")
parques_con_mas_arboles(archivo)
parques_con_arboles_mas_altos(archivo)
parques_con_mas_especies(archivo)
especie_mas_ejemplares(archivo)
razon_exoticas_autoctonas(archivo)
