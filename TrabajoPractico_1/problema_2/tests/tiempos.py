from random import randint
import time
from matplotlib import pyplot as plt
from modules.ListaDobleEnlazada import ListaDobleEnlazada

tamano=[1, 10, 100, 200, 500, 700, 1000]
Tiempocopiar=[]
Tiempolen=[]
Tiempoinvertir=[]

plt.figure(figsize=(10,6))

for valor in tamano:
    datos=ListaDobleEnlazada([randint(1,10000) for n in range(valor)])

    inicio=time.perf_counter()
    datos.copiar()
    fin=time.perf_counter()
    Tiempocopiar.append(fin-inicio)

    inicio=time.perf_counter()
    datos.invertir()
    fin=time.perf_counter()
    Tiempoinvertir.append(fin-inicio)

    inicio=time.perf_counter()
    len(datos)
    fin=time.perf_counter()
    Tiempolen.append(fin-inicio)

plt.plot(tamano,Tiempocopiar)
plt.plot(tamano,Tiempolen)
plt.plot(tamano,Tiempoinvertir)

plt.xlabel("CANTIDAD DE NÚMEROS")
plt.ylabel("TIEMPO (s)")
plt.title("TIEMPO DE EJECUCIÓN")
plt.legend()
plt.grid()
plt.show()