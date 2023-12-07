from Vertice import Vertice

class Grafo:

    vertices = {}
    tiempo = 0

    def __init__(self) -> None:
        self.vertices = {}
        self.tiempo = 0

    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False


    def agregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregarVecino(v)  
                # if key == v:  # Grafo dirigido
                #     value.agregarVecino(u) 
            return True
        else:
            return False

    
    def DFS(self):
        global tiempo
        tiempo = 0
        for u in sorted(list( self.vertices.keys() )):
            if self.vertices[u].color == "white":
                print("Se selecciono: ", self.vertices[u].nombre)
                self.dfsVisitar(self.vertices[u])

    
    def dfsVisitar(self, vert):
        global tiempo
        tiempo = tiempo + 1
        vert.d = tiempo
        vert.color = "gris"

        for v in vert.vecinos:
            if self.vertices[v].color == "white":
                self.vertices[v].pred = vert
                self.dfsVisitar(self.vertices[v])
        
        vert.color = "black"
        tiempo = tiempo + 1
        vert.f = tiempo

    
    def timesDFS(self):
        times = 0

        global tiempo
        tiempo = 0
        for u in sorted(list( self.vertices.keys() )):
            times += 1
            if self.vertices[u].color == "white":
                times += self.timesDfsVisitar(self.vertices[u])

        return times

    
    def timesDfsVisitar(self, vert):
        times = 0
        times += 1
        
        global tiempo
        tiempo = tiempo + 1
        vert.d = tiempo
        vert.color = "gris"

        for v in vert.vecinos:
            times += 1

            if self.vertices[v].color == "white":
                self.vertices[v].pred = vert
                times += self.dfsVisitar(self.vertices[v])
        
        vert.color = "black"
        tiempo = tiempo + 1
        vert.f = tiempo

        return times

    
    def imprimeGrafo(self):
        for key in sorted( list(self.vertices.keys()) ):
            print(f"Vertice: {key}")
            print(f"Descubierto/Termino: { str(self.vertices[key].d) } / { str( self.vertices[key].f ) }")
