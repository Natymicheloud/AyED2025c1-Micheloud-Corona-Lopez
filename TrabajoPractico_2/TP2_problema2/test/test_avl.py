from modulos.avl import AVL

def balance(nodo): #funcion para mostrar el factor de equilibrio del arbol
    if nodo:
        print(f"Fecha: {nodo._fecha}, Altura: {nodo._altura}, Equilibrio: {nodo._equilibrio}")
        balance(nodo._hijoizquierdo)
        balance(nodo._hijoderecho)

avl = AVL() #se inicializa el árbol

#se insertan temperaturas en ciertas fechas
avl.insertar("24/05/2025", 25.7)
avl.insertar("25/05/2025", 30)
avl.insertar("26/05/2025", 20.2)
avl.insertar("27/05/2025", 35)
avl.insertar("23/05/2025", 18.0) #este al ser una fecha anterior a las demas (clave menor), debería probocar una rotación y balanceo

#prueba de busqueda
fechas = ["24/05/2025", "25/05/2025", "26/05/2025", "28/05/2025"]
for fecha in fechas:
    temperatura = avl.buscar(fecha)
    print(f"Fecha: {fecha}, Temperatura: {temperatura} °C")

print()

print("Estado del factor de equilibrio:")
balance(avl._raiz) #se llama a la funcion para ver si luego de la insercion el equilibrio es el correcto

#se insertan mas datos
avl.insertar("22/05/2025", 15.0)
avl.insertar("28/05/2025", 40.0)
avl.insertar("29/05/2025", 45.0)

print()

balance(avl._raiz) #se vuelve a corroborar el balance