from random import randint

def OrdenamientoQuicksort(ListaNumeros):
    OrdenamientoQuicksortAuxiliar(ListaNumeros,0,len(ListaNumeros)-1)

def OrdenamientoQuicksortAuxiliar(ListaNumeros,PrimerNumero,UltimoNumero):
    if PrimerNumero<UltimoNumero:
        Pivote=particion(ListaNumeros,PrimerNumero,UltimoNumero)
        OrdenamientoQuicksortAuxiliar(ListaNumeros,PrimerNumero,Pivote-1)
        OrdenamientoQuicksortAuxiliar(ListaNumeros,Pivote+1,UltimoNumero)

def particion(ListaNumeros,PrimerNumero,UltimoNumero):
    ValorPivote=ListaNumeros[PrimerNumero]
    MarcaIzquierda=PrimerNumero+1
    MarcaDerecha=UltimoNumero

    ordenado=False
    while not ordenado:
        while MarcaIzquierda<=MarcaDerecha and ListaNumeros[MarcaIzquierda]<=ValorPivote:
            MarcaIzquierda=MarcaIzquierda+1

        while ListaNumeros[MarcaDerecha]>=ValorPivote and MarcaDerecha>=MarcaIzquierda:
            MarcaDerecha=MarcaDerecha-1

        if MarcaDerecha<MarcaIzquierda:
            ordenado=True
        
        else:
            cambio=ListaNumeros[MarcaIzquierda]
            ListaNumeros[MarcaIzquierda]=ListaNumeros[MarcaDerecha]
            ListaNumeros[MarcaDerecha]=cambio
    
    cambio=ListaNumeros[PrimerNumero]
    ListaNumeros[PrimerNumero]=ListaNumeros[MarcaDerecha]
    ListaNumeros[MarcaDerecha]=cambio

    return MarcaDerecha

if __name__ == "__main__":
    a,b,c=10000,99999,500
    ListaNumeros=[randint(a,b) for cantidad in range(c)]
    
    OrdenamientoQuicksort(ListaNumeros)
    print(ListaNumeros)