from Vertice import Vertice
from Grafo import Grafo

def main():

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


main()

        