from modulos.grafo import Grafo
from modulos.aldeas import cargar_datos
from modulos.prim import prim

G = Grafo() #se crea una instancia del grafo para almacenar las aldeas y sus conexiones
cargar_datos(G, "data/aldeas.txt") #se cargan los datos del archivo de aldeas al grafo

aldeas_ordenadas = sorted(G.obtener_vertices()) #se obtienen las aldeas del grafo y se ordenan alfabéticamente
print("Aldeas en orden alfabético:") 
for aldea in aldeas_ordenadas: #se itera sobre las aldeas ordenadas y se imprime cada una
    print(f"- {aldea}")
print()

aem = prim(G, "Peligros") #se aplica el algoritmo de Prim para encontrar el árbol de expansión mínima, comenzando desde la aldea "Peligros". Devuelve una lista de aristas que forman el aem, donde cada arista tiene el formato (origen, destino, ponderacion)

quien_envia = {} # diccionario para rastrear quién envía noticias a quién
quien_recibe = {} # diccionario para rastrear quién recibe noticias de quién

for origen, destino, ponderacion in aem: #se recorre cada arista del aem
    quien_envia.setdefault(origen, []).append(destino) #se registra que la aldea origen envía noticias a la aldea destino
    quien_recibe[destino] = origen #se registra que la aldea destino recibe noticias de la aldea origen

for aldea in aldeas_ordenadas: #se recorre cada aldea ordenada alfabéticamente
    recibe_de = quien_recibe.get(aldea, None) #si la aldea está en el diccionario de quien_recibe, se obtiene quién le envía noticias; si no, se asigna None
    envia_a = quien_envia.get(aldea, []) #si la aldea está en el diccionario de quien_envia, se obtiene a quién envía noticias; si no, se asigna una lista vacía
    
    print(f"Aldea: {aldea}") 
    if recibe_de: 
        print(f"  Recibe noticia de: {recibe_de}")
    else:
        print("  Es la aldea origen del mensaje.")
    if envia_a:
        print(f"  Envía noticia a: {', '.join(envia_a)}") 
    else:
        print("  No envía noticia a ninguna otra aldea.")
    print()

total_distancia = sum(ponderacion for origen, destino, ponderacion in aem) # se calcula la distancia total recorrida por las palomas sumando las ponderaciones de todas las aristas en el aem
print(f"Distancia total recorrida por las palomas: {total_distancia} leguas") 