import random
import matplotlib.pyplot as plt

from Vertice import Vertice
from Grafo import Grafo

def prueba():

    grafo = Grafo()

    for letra in ["u", "v", "w", "x", "y", "w", "z"]:
        grafo.agregarVertice( Vertice(letra) )

    # Definimos las conexiones entre los vertices
    edges = ["uv", "vy", "yx", "wz", "zz"]

    # Partimos en 2 la cadena quedandonos : ['AB'] => grafo.agregarArista( 'A', 'B' )
    for edge in edges:
        grafo.agregarArista( edge[:1], edge[1:] )

    grafo.DFS()

    grafo.imprimeGrafo()

def main():

    MAX = 1000

    # Mejor caso 
    grafo_mejor = Grafo()
    nodos_mejor = []
    times_mejor = []
    for _ in range(MAX):

        vertice = Vertice( str(random.randint(0, 99999)) )

        grafo_mejor.agregarVertice( vertice )

        nodos_mejor.append( len(grafo_mejor.vertices) )

        times = grafo_mejor.timesDFS()

        times_mejor.append( times )

    # Caso promedio
    grafo_promedio = Grafo()
    nodos_promedio = []
    times_promedio = []
    nombres = []
    for i in range(MAX):

        nombres.append( str(random.randint(0, 99999)) )
        nombres.append( str(random.randint(0, 99999)) )

        vertice = Vertice( nombres[i] )

        grafo_promedio.agregarVertice( vertice )

        nodos_promedio.append( len(grafo_promedio.vertices) )

        grafo_promedio.agregarArista( nombres[i], nombres[ random.randint(0, len(nombres) - 1) ] )

        times = grafo_promedio.timesDFS()

        times_promedio.append( times )

    # Peor caso
    grafo_peor = Grafo()
    nodos_peor = []
    times_peor = []
    nombres = []
    for i in range(MAX):

        nombres.append( str(random.randint(0, 99999)) )
        nombres.append( str(random.randint(0, 99999)) )
        vertice = Vertice( nombres[i] )

        grafo_peor.agregarVertice( vertice )

        nodos_peor.append( len(grafo_peor.vertices) )

        times = 0
        for j in range( len(nombres) ):
            grafo_peor.agregarArista(nombres[i], nombres[j])
            # grafo_peor.agregarArista(nombres[j], nombres[i])

        times = grafo_peor.timesDFS()

        times_peor.append( times )



    # Construyendo gráfica...
    fig, axes = plt.subplots(nrows=1, ncols=2)
    ax1, ax2 = axes.flatten()
    fig.subplots_adjust(hspace=0.5)

    ax1.plot(nodos_promedio, times_promedio, label = 'Caso promedio', marker = '*', color = 'b')
    ax1.plot(nodos_mejor, times_mejor, label = 'Mejor caso', marker = 'o', color = 'g')

    ax2.plot(nodos_peor, times_peor, label = 'Peor caso', marker = 'x', color = 'r')

    plt.title('DFS')
    ax1.set_xlabel('Nodos')
    ax1.set_ylabel('Veces que entra')
    ax1.grid(True)
    ax1.legend(loc=2)

    ax2.set_xlabel('Nodos')
    ax2.set_ylabel('Veces que entra')
    ax2.grid(True)
    ax2.legend(loc=2)

    plt.show()


main()        