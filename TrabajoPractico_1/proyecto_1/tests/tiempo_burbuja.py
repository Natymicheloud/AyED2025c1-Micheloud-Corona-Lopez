from random import randint
import time
from matplotlib import pyplot as plt
from modules.ordenamiento_burbuja import OrdenamientoBurbuja

tamano=[1, 10, 100, 200, 500, 700, 1000]
TiempoBurbuja=[]

plt.figure(figsize=(10,6))

for valor in tamano:
    datos=[randint(1,10000) for n in range(valor)]

    inicio=time.perf_counter()
    OrdenamientoBurbuja(datos.copy())
    fin=time.perf_counter
    TiempoBurbuja.append(fin-inicio)

plt.plot(tamano,TiempoBurbuja)

plt.xlabel("CANTIDAD DE NÚMEROS")
plt.ylabel("TIEMPO (s)")
plt.title("TIEMPO DE EJECUCIÓN")
plt.legend()
plt.grid()
plt.show()