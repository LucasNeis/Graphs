from Digrafo import *
class Digrafo_Valorado(Digrafo):
    def __init__(self):
        Digrafo.__init__(self)

    def adiciona_valor_em_aresta(self, vertice_1, vertice_2, valor, nome_do_valor):
        chave = vertice_1.pega_nome() + vertice_2.pega_nome()
        if chave in self._arestas:
            self._arestas[chave].adiciona_valor(valor, nome_do_valor)
            return True
        return False

    def pega_valor_de_aresta(self, vertice_1, vertice_2, nome_do_valor):
        chave = vertice_1.pega_nome() + vertice_2.pega_nome()
        if chave in self._arestas:
            return self._arestas[chave].pega_valor(nome_do_valor)
        return None

    def remove_valor_de_aresta(self, vertice_1, vertice_2, nome_do_valor):
        chave = vertice_1.pega_nome() + vertice_2.pega_nome()
        if chave in self._arestas:
            self._arestas[chave].remove_valor(nome_do_valor)
            return True
        return False