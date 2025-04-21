from random import randint

def CountingSort(ListaNumeros,digito):
    ListaSalida=[0]*len(ListaNumeros)
    ListaDigito=[0]*10

    for numero in range(0,len(ListaNumeros)):
        ListaDigito[(ListaNumeros[numero]//digito)%10]+=1
    #separa en unidades el numero y cuenta cuantos numeros terminan en esa unidad
    
    for numero in range (1,10):
        ListaDigito[numero]+=ListaDigito[numero - 1]
    #va sumando de a dos casillas (indices) acumulando los numeros

    numero = len(ListaNumeros)-1
    while numero>=0:
        #ListaSalida[ListaDigito[(ListaNumeros[numero]//digito)%10]-1]=ListaNumeros[numero]
        #ListaDigito[ListaDigito[(ListaNumeros[numero]//digito)%10]]-=1
        indice=ListaNumeros[numero]//digito
        ListaSalida[ListaDigito[indice%10]-1]=ListaNumeros[numero]
        ListaDigito[indice%10]-=1
        numero-=1

    for numero in range(0,len(ListaNumeros)):
        ListaNumeros[numero]=ListaSalida[numero]

def OrdenamientoRadix(ListaNumeros):
    maximo=max(ListaNumeros)

    digito=1
    while (maximo//digito)>0:
        CountingSort(ListaNumeros,digito)
        digito*=10
    
    return ListaNumeros

if __name__ == "__main__":
    a,b,c=10000,99999,500
    ListaNumeros=[randint(a,b) for cantidad in range(c)]

    ListaOrdenada = OrdenamientoRadix(ListaNumeros)
    print(ListaOrdenada)
    