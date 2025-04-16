
from random import randint

if __name__ == "__main__":
    a,b,c=10000,99999,500
    ListaNumeros=[randint(a,b) for cantidad in range(c)]

    ListaOrdenada = sorted(ListaNumeros)
    print(ListaOrdenada)

from random import randint
import time
from matplotlib import pyplot as plt

tamano=[1, 10, 100, 200, 500, 700, 1000]
TiempoSorted=[]

plt.figure(figsize=(10,6))

for valor in tamano:
    datos=[randint(1,10000) for n in range(valor)]

    inicio=time.perf_counter()

    fin=time.perf_counter()
    TiempoSorted.append(fin-inicio)

plt.plot(tamano,TiempoSorted)

plt.xlabel("CANTIDAD DE NÚMEROS")
plt.ylabel("TIEMPO (s)")
plt.title("TIEMPO DE EJECUCIÓN (SORTED)")
plt.legend()
plt.grid()
plt.show()
