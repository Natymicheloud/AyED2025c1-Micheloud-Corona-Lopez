from modulos.monticulo import MonticuloBinario

class GrafoAldeas:
    def __init__(self):
        self.vertices = set()
        self.adyacencia = {}
        
    def agregar_arista(self, aldea1, aldea2, distancia):
        self.vertices.update([aldea1, aldea2])
        if aldea1 not in self.adyacencia:
            self.adyacencia[aldea1] = []
        if aldea2 not in self.adyacencia:
            self.adyacencia[aldea2] = []
        self.adyacencia[aldea1].append((aldea2, distancia))
        self.adyacencia[aldea2].append((aldea1, distancia))  # Grafo no dirigido


    def arbol_expansion_minima(self, inicio):
        visitados = set()
        monticulo = MonticuloBinario()
        monticulo.insertar((0, inicio, None))  # (distancia, aldea_actual, aldea_anterior)
        arbol = {}
        distancia_total = 0
        
        while not monticulo.esta_vacio() and len(visitados) < len(self.vertices):
            distancia, actual, anterior = monticulo.eliminar_min()
            
            if actual in visitados:
                continue
                
            visitados.add(actual)
            
            if anterior is not None:
                if anterior not in arbol:
                    arbol[anterior] = []
                arbol[anterior].append((actual, distancia))
                distancia_total += distancia
            
            for vecino, peso in self.adyacencia.get(actual, []):
                if vecino not in visitados:
                    monticulo.insertar((peso, vecino, actual))
        
        return arbol, distancia_total