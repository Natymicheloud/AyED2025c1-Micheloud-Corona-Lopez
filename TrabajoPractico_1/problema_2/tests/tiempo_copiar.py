from random import randint
import time
from matplotlib import pyplot as plt
from modules.ListaDobleEnlazada import ListaDobleEnlazada

tamano=[1, 10, 100, 200, 500, 700, 1000]
tiempo_copiar=[]

plt.figure(figsize=(10,6))

for valor in tamano:
    datos=ListaDobleEnlazada([randint(1,10000) for n in range(valor)])

    inicio=time.perf_counter()
    datos.copiar()
    fin=time.perf_counter()
    tiempo_copiar.append(fin-inicio)

plt.plot(tamano,tiempo_copiar)

plt.xlabel("CANTIDAD DE ELEMENTOS")
plt.ylabel("TIEMPO (s)")
plt.title("TIEMPO DE EJECUCIÓN (copiar)")
plt.legend()
plt.grid()
plt.show()