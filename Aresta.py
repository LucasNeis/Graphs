
class Aresta(object):
    def __init__(self, vertice_1, vertice_2):
        self._vertice_1 = vertice_1
        self._vertice_2 = vertice_2
        self._valores = {}

    def adiciona_valor(self, valor, nome_do_valor):
        self._valores[nome_do_valor] = valor
        
    def pega_valores(self):
        return self._valores.items()
    
    def remove_valor(self, nome_do_valor):
        try:
            del self._valores[nome_do_valor]
        except KeyError as e:
            print "Valor nao existe nesta aresta."

    def pega_vertices(self):
        return (self._vertice_1, self._vertice_2)

    def id(self):
        return self._vertice_1.pega_nome() + " conectado com " + self._vertice_2.pega_nome()

    def pega_valor(self, nome_do_valor):
        return self._valores.get(nome_do_valor)