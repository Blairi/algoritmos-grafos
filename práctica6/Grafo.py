from Vertice import Vertice

class Grafo:
    vertices = {}

    def __init__(self) -> None:
        self.vertices = {}

    def agregarVertice(self, vertice : Vertice) -> bool:

        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False


    def agregarArista(self, u, v) -> bool:

        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregarVecino(v)
                if key == v:
                    value.agregarVecino(u)
            return True
        else:
            return False


    def BFS(self, vertice : Vertice) -> None:
        
        vertice.distancia = 0
        vertice.color = "gris"
        vertice.pred = -1

        lista = list()
        lista.append(vertice.nombre)

        while len(lista) > 0:
            u = lista.pop()

            node_u = self.vertices[u]
            
            for v in node_u.vecinos:
                node_v = self.vertices[v]

                if node_v.color == "blanco":
                    node_v.color = "gris"
                    node_v.distancia = node_u.distancia + 1
                    node_v.pred = node_u.nombre
                    lista.append(v)
            
            self.vertices[u].color = "black"

        for key in sorted(list(self.vertices.keys())):
            print(f"La distancia de {vertice.nombre} a { key } es {str(self.vertices[key].distancia)}")

    
    def timesBFS(self, vertice : Vertice) -> int:
        
        times = 0

        vertice.distancia = 0
        vertice.color = "gris"
        vertice.pred = -1

        lista = list()
        lista.append(vertice.nombre)


        while len(lista) > 0:

            times += 1

            u = lista.pop()

            node_u = self.vertices[u]
            
            for v in node_u.vecinos:

                times += 1

                node_v = self.vertices[v]

                if node_v.color == "blanco":
                    node_v.color = "gris"
                    node_v.distancia = node_u.distancia + 1
                    node_v.pred = node_u.nombre
                    lista.append(v)
            
            self.vertices[u].color = "black"

        # for key in sorted(list(self.vertices.keys())):
        #     print(f"La distancia de {vertice.nombre} a { key } es {str(self.vertices[key].distancia)}")

        return times

    
    def imprimirGrafo(self) -> None:
        for key in sorted(list(self.vertices.keys())):
            print(f"Vertice: { key } \nSus vecinos son: { str(self.vertices[key].vecinos) }")
