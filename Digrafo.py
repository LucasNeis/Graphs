from Grafo import *

class Digrafo(Grafo):
    def __init__(self):
        Grafo.__init__(self)

    def adiciona_vertice(self, vertice):
        if vertice.e_orientado():
            self._vertices[vertice.pega_nome()] = vertice
        else:
            raise Exception("Um dos vertice não é do tipo desde grafo")

    def adiciona_vertice_por_nome(self, nome):
        vertice = Vertice(nome, True)
        self._vertices[vertice.pega_nome()] = vertice
        return vertice

    def grau_de_emissao(self, vertice):
        return self.grau(vertice)

    def grau_de_recepcao(self, vertice):
        return vertice.grau_de_recepcao()

    def antecessores(self, vertice):
        return vertice.pega_antecessores()
