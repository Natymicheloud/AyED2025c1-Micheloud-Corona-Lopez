def cargar_datos(aldeas_txt):
    """Carga los datos del archivo y los devuelve como lista de tuplas"""
    datos = []
    try:
        with open(aldeas_txt, 'r') as f:
            print(f"\nLeyendo archivo: {aldeas_txt}")  # Debug
            for i, linea in enumerate(f, 1):
                linea = linea.strip()
                if not linea:  # Si la línea está vacía
                    continue
                
                partes = linea.split(', ')
                print(f"Línea {i}: {linea}")  # Debug
                
                if len(partes) == 3:
                    try:
                        origen = partes[0]
                        destino = partes[1]
                        distancia = int(partes[2])
                        datos.append((distancia, origen, destino))
                        print(f"Añadido: {(distancia, origen, destino)}")  # Debug
                    except ValueError as e:
                        print(f"Error en línea {i}: {e} - {linea}")
                else:
                    print(f"Formato incorrecto en línea {i}: {linea}")
                    
    except FileNotFoundError:
        print(f"Error: Archivo '{aldeas_txt}' no encontrado")
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    print(f"\nTotal de datos cargados: {len(datos)}")  # Debug
    return datos

print(cargar_datos('aldeas_txt'))