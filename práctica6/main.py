from Grafo import Grafo
from Vertice import Vertice


def main():

    grafo = Grafo()

    # Creamos vertices o nodos
    verticeA = Vertice("A")
    verticeB = Vertice("B")

    grafo.agregarVertice( verticeA )
    grafo.agregarVertice( verticeB )

    # Creamos más vertices y los agregamos al grafo
    for letra in ['C', 'D', 'E', 'H', 'G', 'X']:
        grafo.agregarVertice( Vertice(letra) )

    # Definimos las conexiones entre los vertices
    edges = [ 'AB', 'BC', 'CD', 'DH', 'DE', 'DG', 'GX']

    # Partimos en 2 la cadena quedandonos : ['AB'] => grafo.agregarArista( 'A', 'B' )
    for edge in edges:
        grafo.agregarArista( edge[:1], edge[1:] )

    # Hacemos una búsqueda de como llegar al vertice "A" desde cualquier nodo
    grafo.BFS( verticeA )

main()