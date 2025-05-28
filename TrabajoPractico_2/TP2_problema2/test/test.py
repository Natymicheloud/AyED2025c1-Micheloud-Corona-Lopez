from modulos.avl import AVL
from app.Temperaturas_DB import TemperaturasDB

temperaturas = TemperaturasDB()

temperaturas.guardar_temperatura(25.7, '24/05/2025')
temperaturas.guardar_temperatura(30, '25/05/2025')
temperaturas.guardar_temperatura(20.2, '26/05/2025')
temperaturas.guardar_temperatura(35, '27/05/2025')

print("Temperatura el 24/05/2025:", temperaturas.devolver_temperatura('24/05/2025'))

print("Temperatura máxima entre 24/05/2025 y 27/05/2025:", temperaturas.max_temp_rango('24/05/2025', '27/05/2025'))

print("Temperatura mínima entre 24/05/2025 y 27/05/2025:", temperaturas.min_temp_rango('24/05/2025', '27/05/2025'))

print("Temperaturas mínima y máxima entre 24/05/2025 y 27/05/2025:", temperaturas.temp_extremos_rango('24/05/2025', '27/05/2025'))

print("Lista de temperaturas entre 24/05/2025 y 27/05/2025:")
print(temperaturas.devolver_temperaturas('24/05/2025', '27/05/2025'))

temperaturas.borrar_temperatura('24/05/2025')
print("Temperatura el 24/05/2025 después de borrar:", temperaturas.devolver_temperatura('24/05/2025') or "No existe")

print("Cantidad de temperaturas guardadas:", temperaturas.cantidad_muestras())

print("Lista de temperaturas entre 24/05/2025 y 27/05/2025:")
print(temperaturas.devolver_temperaturas("24/05/2025", "27/05/2025"))


