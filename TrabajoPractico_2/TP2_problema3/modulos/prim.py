from modulos.monticulo import MonticuloBinario
from modulos.grafo import Grafo

def prim(grafo, inicio): #algoritmo de prim que necesita el grafo de aldeas y el nodo inicio desde el cual se comienza a construir el árbol de expansión mínima (aem)
    aem = []  #lista para almacenar el árbol de expansión mínima
    visitados = set()  #conjunto para rastrear los vértices visitados (aldeas ya incluidas en el aem)
    monticulo = MonticuloBinario()  #montículo para seleccionar el siguiente vértice con la menor ponderación

    if not grafo.obtener_vertice(inicio):  #verifica si el nodo de inicio existe en el grafo
        print(f"La aldea '{inicio}' no existe en el grafo.")
        return []

    visitados.add(inicio)  #ponemos la aldea inicial como visitada para no volver a agregarla a la aem
    vertice_inicio = grafo.obtener_vertice(inicio)  #obtiene el objeto vértice del grafo (nodo inicio)
    if vertice_inicio: #verifica si el vértice de inicio existe en el grafo
        for vecino, ponderacion in vertice_inicio.obtener_adyacentes().items(): #itera sobre los vecinos del vértice de inicio y obtiene sus conexiones adyacentes 
            monticulo.Insertar((ponderacion, inicio, vecino.obtener_clave()))  #cada vertice vecino se inserta en el montículo con su ponderación, origen y destino

    print("Estado inicial del montículo:", monticulo.listamonticulo)  #imprime el estado inicial del montículo para depuración

    while len(visitados) < len(grafo.obtener_vertices()): #mientras hayas aldeas sin visiar, se sigue expandiendo el aem
        if monticulo.tamañoactual == 0:  #verifica si el montículo está vacío, lo que significa que no hay más aldeas para visitar
            print("El montículo está vacío antes de visitar todas las aldeas.")
            break
       
        print("\n🛠️ Montículo antes de eliminar:", monticulo.listamonticulo)
        ponderacion, origen, destino = monticulo.eliminarMin()  #extrae la conexion con menor ponderacion del monticulo
        print(f"🔍 Extracción del montículo: {origen} -> {destino} ({ponderacion} leguas)")

        if destino not in visitados:  #verifica si el destino no ha sido visitado
            visitados.add(destino) #agrega el destino al conjunto de visitados
            aem.append((origen, destino, ponderacion)) #agrega la conexión al árbol de expansión mínima

            for vecino, ponderacion in grafo.obtener_vertice(destino).obtener_adyacentes().items(): #obtiene los vecinos del destino recién visitado (recien agregado al aem)
                if vecino.obtener_clave() not in visitados: #verifica si el vecino no ha sido visitado
                    monticulo.Insertar((ponderacion, destino, vecino.obtener_clave())) #inserta el vecino en el montículo con su ponderación, origen y destino
        print("🛠️ Montículo después de eliminar:", monticulo.listamonticulo)

    return aem  #cuando todas las aldeas estan conectadas, devuelve el árbol de expansión mínima con las conexiones optimas

G = Grafo()
mst = prim(G, "Peligros")

if mst:
    print("Árbol de expansión mínima:")
    for origen, destino, peso in mst:
        print(f"{origen} -> {destino} ({peso} leguas)")
else:
    print("No se generó un árbol de expansión mínima.")

