from modulos.monticulo import MonticuloBinario
from modulos.grafo import Grafo

def cargar_desde_archivo(self, archivo="aldeas.txt"):
    """Carga el grafo directamente desde un archivo"""
    try:
        with open(archivo, 'r') as f:
            for linea in f:
                partes = linea.strip().split(', ')
                if len(partes) == 3:
                    aldea1, aldea2, distancia = partes[0], partes[1], int(partes[2])
                    self.agregar_arista(aldea1, aldea2, distancia)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'")
    
# --- Prueba ---
if __name__ == "__main__":
    grafo = Grafo()
    grafo.cargar_desde_archivo()  # Carga los datos desde "aldeas.txt"
    
    aldea_inicio = "Lomaseca"  # Puedes cambiar a cualquier aldea
    arbol, distancia_total = grafo.arbol_expansion_minima(aldea_inicio)
    
    print("Árbol de expansión mínima (MST):")
    for aldea, conexiones in arbol.items():
        print(f"{aldea} -> {conexiones}")
    print(f"\nDistancia total del MST: {distancia_total} km")
