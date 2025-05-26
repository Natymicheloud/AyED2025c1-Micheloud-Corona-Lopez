from modulos.grafo import Grafo

archivo = "test/aldeas.txt" 

def cargar_datos(grafo, archivo): #carga los datos del archivo y los agrega al grafo
    with open(archivo, 'r') as f: #abre el archivo en modo lectura
        for linea in f: #itera sobre cada linea del archivo
            datos = linea.strip().split(',') #divide la linea en partes usando la coma como separador
            if len(datos) == 3: #verifica que la linea tenga exactamente 3 partes (origen, destino, ponderacion)
                origen, destino, ponderacion = datos[0].strip(), datos[1].strip(), int(datos[2]) #asigna las partes a las variables correspondientes, convirtiendo la ponderacion a entero
                grafo.agregar_arista(origen, destino, ponderacion) #agrega la arista al grafo usando los datos cargados

G = Grafo()
cargar_datos(G, 'test/aldeas.txt') 
for clave, vertice in G._Grafo__vertices.items():
    print(f"Aldea: {clave} -> Objeto: {vertice}")


if "Peligros" not in G.obtener_vertices():
    print("Error: 'Peligros' no está en el grafo después de cargar los datos.")

print("Aldeas en el grafo:", list(G.obtener_vertices()))
print(f"Aldea: Peligros - Conexiones: {list(G.obtener_vertice('Peligros').obtener_adyacentes())}")
