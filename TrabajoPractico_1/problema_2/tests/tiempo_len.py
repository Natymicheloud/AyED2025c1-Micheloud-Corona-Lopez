from random import randint
import time
from matplotlib import pyplot as plt
from modules.ListaDobleEnlazada import ListaDobleEnlazada

tamano=[1, 10, 100, 200, 500, 700, 1000]
tiempo_len=[]

plt.figure(figsize=(10,6))

for valor in tamano:
    datos=[randint(1,10000) for n in range(valor)]

    inicio=time.perf_counter()
    len(datos.copy())
    fin=time.perf_counter()
    tiempo_len.append(fin-inicio)

plt.plot(tamano,tiempo_len)

plt.xlabel("CANTIDAD DE ELEMENTOS")
plt.ylabel("TIEMPO (s)")
plt.title("TIEMPO DE EJECUCIÓN (len)")
plt.legend()
plt.grid()
plt.show()