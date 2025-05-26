from modulos.monticulo import MonticuloBinario

def cargar_datos(aldeas):
    """Carga los datos del archivo y los devuelve como lista de tuplas"""
    datos = []
    with open("aldeas.txt", 'r') as f:
        for linea in f:
            partes = linea.strip().split(', ')
            if len(partes) == 3:  # Asegurarse que tiene origen, destino y distancia
                origen = partes[0]
                destino = partes[1]
                distancia = int(partes[2])
                datos.append((distancia, origen, destino))
    return datos


def probar_monticulo():
    """Función para probar el montículo con los datos de aldeas"""
    # Cargar datos desde el archivo
    conexiones = cargar_datos('aldeas_txt')
    
    print("Primeras 5 conexiones cargadas:")
    for conexion in conexiones[:5]:
        print(conexion)
    
    # Crear montículo vacío
    monticulo = MonticuloBinario()
    
    # Insertar todas las conexiones
    for conexion in conexiones:
        monticulo.insertar(conexion)
    
    print(f"\nTotal de conexiones insertadas: {monticulo.tamañoactual}")
    
    # Extraer las 5 conexiones con menor distancia
    print("\n5 conexiones más cortas:")
    for _ in range(5):
        print(monticulo.eliminar_min())
    
    # Reconstruir el montículo con todos los datos
    monticulo.construir_monticulo(conexiones)
    
    # Extraer todas las conexiones en orden
    print("\nTodas las conexiones ordenadas por distancia:")
    while not monticulo.esta_vacio():
        conexion = monticulo.eliminar_min()
        print(f"{conexion[1]} -> {conexion[2]}: {conexion[0]} km")

if __name__ == "__main__":
    probar_monticulo()