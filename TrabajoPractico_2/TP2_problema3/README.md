# Implementación de grafos y algoritmo Prim

Breve descripción del proyecto:
Para la resolución del problema, implementamos grafos y algoritmo de prim, este usa un montículo binario, con el objetivo de enviar una noticia desde una aldea "origen" hacia las 21 aldeas "destino", recorriendo la menor cantidad de leguas posible para completar el recorrido.  
El funcionamiento del AVL se comprueba con el test_avl y el test de la implementación con la base de datos en test.
.

## 🏗Arquitectura General

Explica brevemente cómo está organizado el código (funciones y/o clases)
La función que agrega los datos de las aldeas al grafo, la clase grafo, el montículo binario y el algoritmo prim están disponibles en la carpeta [modulos](./modulos) del problema.

La aplicación que resuelve el problema, muestra una lista ordenada alfabeticamente de las aldeas, imprime el recorrido más eficiente de las palomas y la distancia total recorrida, están disponibles en la carpeta [app](./app) del problema.

La lista original de aldeas con sus aldeas vecinas y la distancia entre las mismas (ponderación) está disponible en la carpeta [data](./data) del problema.

El informe completo está disponible en la carpeta [docs](./docs) del problema.

---
## 📑Dependencias

1. **Python 3.x**
2. **matplotlib** (`pip install matplotlib`)
3. listar dependencias principales
4. Dependencias listadas en requierements.txt

---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. **Crear y activar** un entorno virtual.

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` se encuentran en la carpeta [deps](./deps) del problema.

---
## 🙎‍♀️🙎‍♂️Autores

- Corona Abigail.
- López Lascurain Ema.
- Micheloud Natalí.

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.
