from modulos.monticulo import MonticuloBinario

def prim(grafo, inicio): #algoritmo de prim que necesita el grafo de aldeas y el nodo inicio desde el cual se comienza a construir el árbol de expansión mínima (aem)
    aem = []  #lista para almacenar el árbol de expansión mínima
    visitados = set()  #conjunto para rastrear los vértices visitados (aldeas ya incluidas en el aem). se utiliza un conjunto (set()) porque no permite duplicados lo que hace que sea más eficiente la verificacion 
    monticulo = MonticuloBinario()  #montículo para seleccionar el siguiente vértice con la menor ponderación

    visitados.add(inicio)  #ponemos la aldea inicial como visitada para no volver a agregarla a la aem
    vertice_inicio = grafo.obtener_vertice(inicio)  #obtiene el objeto vértice del grafo (nodo inicio)
    
    if vertice_inicio: #verifica si el vértice de inicio existe en el grafo
        for vecino_clave in vertice_inicio.obtener_adyacentes():
            ponderacion = vertice_inicio.obtener_ponderacion(vecino_clave)  #obtiene la ponderación de la conexión al vecino
            monticulo.Insertar((ponderacion, inicio, vecino_clave))  #cada vertice vecino se inserta en el montículo con su ponderación, origen y destino

    while len(visitados) < len(grafo.obtener_vertices()): #mientras hayas aldeas sin visiar, se sigue expandiendo el aem
        if monticulo.tamañoactual == 0:  #verifica si el montículo está vacío, lo que significa que no hay más aldeas para visitar
            break  
        
        ponderacion, origen, destino = monticulo.eliminarMin()  #extrae la conexion con menor ponderacion del monticulo

        if destino not in visitados:  #verifica si el destino no ha sido visitado
            visitados.add(destino) #agrega el destino al conjunto de visitados
            aem.append((origen, destino, ponderacion)) #agrega la conexión al árbol de expansión mínima

            vertice_destino = grafo.obtener_vertice(destino)  #obtiene el objeto vértice del destino recién visitado
            if vertice_destino:  #verifica si el vértice de destino existe en el grafo
                for vecino_clave in vertice_destino.obtener_adyacentes():
                    if vecino_clave not in visitados: #verifica si el vecino no ha sido visitado
                        ponderacion = vertice_destino.obtener_ponderacion(vecino_clave)  #obtiene la ponderación de la conexión al vecino
                        monticulo.Insertar((ponderacion, destino, vecino_clave)) #inserta el vecino en el montículo con su ponderación, origen y destino

    return aem  #cuando todas las aldeas estan conectadas, devuelve el árbol de expansión mínima con las conexiones optimas