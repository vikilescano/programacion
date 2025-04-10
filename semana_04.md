# Análisis del Arbolado en Espacios Verdes de Buenos Aires

Este documento presenta un análisis del arbolado en los espacios verdes de la Ciudad de Buenos Aires, utilizando datos oficiales proporcionados por el Ministerio de Ambiente y Espacio Públic en https://data.buenosaires.gob.ar/dataset/arbolado-espacios-verdes. A continuación, se hace un análisis de la base de datos que responden a algunas preguntas de interés. 


### 1. ¿Cuál es el parque con mayor cantidad de árboles?

Para responder esta pregunta, se desarrolló una función que cuenta la cantidad de árboles en cada parque y determina cuál tiene la mayor cantidad. Se excluyeron los registros marcados como "S/D" (sin datos) para obtener resultados más precisos.

```python
def parques_con_mas_arboles(nombre_archivo):
    parques = obtener_parques(nombre_archivo)
    conteo_arboles = {}
    
    for parque in parques:
        arboles = arboles_parque(nombre_archivo, parque)
        conteo_arboles[parque] = len(arboles)
    
    max_arboles = max(conteo_arboles.values())
    parques_max = [parque for parque, cantidad in conteo_arboles.items() 
                  if cantidad == max_arboles]
    
    return parques_max, max_arboles
```

**Resultado:**
```
Parque(s) con más árboles: ['INDOAMERICANO'] con 3099 árboles
```

### 2. ¿Cuál es el parque con los árboles más altos en promedio?

Para esta pregunta, se calculó la altura promedio de los árboles en cada parque y se identificó el parque que tiene el mayor promedio.

```python
def parques_con_arboles_mas_altos(nombre_archivo):
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
```

**Resultado:**
```
Parque(s) con árboles más altos en promedio: ['INFANTE DON ENRIQUE EL NAVEGANTE'] con 31.66 metros
```

### 3. ¿Cuál es el parque con mayor variedad de especies?

Para responder esta pregunta, se contabilizó la cantidad de especies diferentes presentes en cada parque.

```python
def parques_con_mas_especies(nombre_archivo):
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
```

**Resultado:**
```
Parque(s) con más variedad de especies: ['ROSEDAL'] con 109 especies
```

### 4. ¿Cuál es la especie que más ejemplares tiene en la ciudad?

Para esta pregunta, se contabilizó la cantidad de ejemplares de cada especie en todos los parques de la ciudad.

```python
def especie_mas_ejemplares(nombre_archivo):
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
```

**Resultado:**
```
Especie con más ejemplares: Eucalipto con 4112 ejemplares
```

### 5. ¿Cuál es la razón entre especies exóticas y autóctonas?

Finalmente, se calculó la razón entre la cantidad de árboles de especies exóticas y la cantidad de árboles de especies nativas (autóctonas).

```python
def razon_exoticas_autoctonas(nombre_archivo):
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
```

**Resultado:**
```
Razón entre especies exóticas y autóctonas: 1.89
```

Este valor indica que hay casi 2 árboles de especies exóticas por cada árbol de especie nativa en los espacios verdes de Buenos Aires.

## Conclusiones

Del análisis realizado, podemos concluir que:

1. El **Parque Indoamericanoo** es el que tiene la mayor cantidad de árboles (3099).
2. El **Parque Infante Don Enrique El Navegante**, en Puerto Madero, tiene los árboles más altos en promedio, con una altura media de 32 metros.
3. El **Rosedal** es el parque con más especies (109)
4. El **Eucalipto** es la especie más común en la ciudad, con 4,112 ejemplares.
5. Hay una predominancia de especies exóticas sobre las nativas, con una proporción de aproximadamente 2 a 1.
