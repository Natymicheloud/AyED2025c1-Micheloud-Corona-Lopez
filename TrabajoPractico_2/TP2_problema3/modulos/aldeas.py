from modulos.grafo import Grafo

archivo = "test/aldeas.txt"

def cargar_datos(grafo, archivo):
    with open(archivo, 'r') as f:
        for linea in f:
            datos = linea.strip().split(',')
            if len(datos) == 3:
                origen, destino, ponderacion = datos[0], datos[1], int(datos[2])
                grafo.agregar_arista(origen, destino, ponderacion)

G = Grafo()
cargar_datos(G, 'test/aldeas.txt')

print("Aldeas en el grafo:", list(G.obtener_vertices()))
print()