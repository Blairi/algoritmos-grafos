
class Vertice:

    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.vecinos = list()

        self.d = 0
        self.f = 0
        self.color = "white"
        self.pred = -1

    def agregarVecino(self, vecino) -> None:
        if vecino not in self.vecinos:
            self.vecinos.append(vecino)
            self.vecinos.sort()
