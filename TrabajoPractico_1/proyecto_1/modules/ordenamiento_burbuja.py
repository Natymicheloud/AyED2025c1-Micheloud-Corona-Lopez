from random import randint 

def OrdenamientoBurbuja(ListaNumeros):
    for CantidadPasadas in range(len(ListaNumeros)-1,0,-1):
        for Numero in range(CantidadPasadas):
            if ListaNumeros[Numero]>ListaNumeros[Numero+1]:
                ListaNumeros[Numero],ListaNumeros[Numero+1]=ListaNumeros[Numero+1],ListaNumeros[Numero]
    
    return ListaNumeros

if __name__ == "__main__":
    a,b,c=10000,99999,500
    ListaNumeros=[randint(a,b) for cantidad in range(c)]

    ListaOrdenada = OrdenamientoBurbuja(ListaNumeros)
    print(ListaOrdenada)