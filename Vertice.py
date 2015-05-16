from Aresta import *

class Vertice(object):
    
    def __init__(self, nome, e_direcionado):
        self.__nome = nome
        self.__e_direcionado = e_direcionado
        self.__adjacentes = {}
        self.__antecessores = {}

    def conecta(self, adjacente, aresta):
        if not self.__e_direcionado:
            aresta_prv = Aresta(adjacente, self)
            if not aresta.id() in self.__adjacentes and not aresta_prv.id() in self.__adjacentes:
                self.__adjacentes[aresta.id()] = adjacente
                if not adjacente.esta_conectado(self):
                    adjacente.conecta(self, aresta)
                return True
            return False
        if not aresta.id() in self.__adjacentes:
            self.__adjacentes[aresta.id()] = adjacente
            djacente.__add_antecessor(self, aresta)
            return True
        return False

    def __add_antecessor(self, antecessor, aresta):
        self.__antecessores[aresta.id] = antecessor
        
    def desconecta(self, adjacente, aresta):
        conseguiu = False
        if aresta.id() in self.__adjacentes:
            del self.__adjacentes[aresta.id()]
            conseguiu = True
            if not self.__e_direcionado and adjacente.esta_conectado(self):
                adjacente.desconecta(self, aresta)
        return conseguiu

    def e_orientado(self):
        return self.__e_direcionado
        
    def grau(self):
        return len(self.__adjacentes)

    def grau_de_recepcao(self):
        return len(self.__antecessores)
    
    def pega_nome(self):
        return self.__nome
    
    def esta_conectado(self, adjacente):
        aresta = Aresta(self, adjacente)
        if self.__e_direcionado:
            return aresta.id() in self.__adjacentes 
        nome = aresta.id()
        aresta = Aresta(adjacente, self)
        return  aresta.id() in self.__adjacentes or nome in self.__adjacentes

    def pega_adjacentes(self):
        return self.__adjacentes.values()

    def pega_antecessores(self):
        if self.__e_direcionado:
            return self.__antecessores.values()
        else:
            return self.__adjacentes.values()
