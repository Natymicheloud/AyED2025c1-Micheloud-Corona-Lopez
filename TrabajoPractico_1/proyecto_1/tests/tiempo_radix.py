from random import randint
import time
from matplotlib import pyplot as plt
from modules.ordenamiento_radix import OrdenamientoRadix

tamano=[1, 10, 100, 200, 500, 700, 1000]
TiempoRadix=[]

plt.figure(figsize=(10,6))

for valor in tamano:
    datos=[randint(1,10000) for n in range(valor)]

    inicio=time.perf_counter()
    OrdenamientoRadix(datos.copy())
    fin=time.perf_counter()
    TiempoRadix.append(fin-inicio)

plt.plot(tamano,TiempoRadix)

plt.xlabel("CANTIDAD DE NÚMEROS")
plt.ylabel("TIEMPO (s)")
plt.title("TIEMPO DE EJECUCIÓN (RADIX)")
plt.legend()
plt.grid()
plt.show()