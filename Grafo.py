from Vertice import *
from Excecao_Adicao_de_Vertice import *
from Excecao_Remocao_de_Vertice import *

class Grafo(object):
    def __init__(self):
        self._vertices = {}
        self._arestas = {}
    
    def adiciona_vertice(self, vertice):
        if not vertice.pega_nome() in self._vertices:
            if not vertice.e_orientado():
                self._vertices[vertice.pega_nome()] = vertice
            else:
                raise Excecao_Adicao_de_Vertice(0)
        else:
            raise Excecao_Adicao_de_Vertice(1)

    def remove_vertice(self, vertice):
        if vertice.pega_nome() in self._vertices:
            self.remove_vertice_por_nome(vertice.pega_nome())
        else:
            raise Excecao_Remocao_de_Vertice

    def conecta(self, vertice_1, vertice_2):
        if vertice_1.pega_nome() in self._vertices and vertice_2.pega_nome() in self._vertices:
            aresta = Aresta(vertice_1, vertice_2)
            chave = vertice_1.pega_nome() + vertice_2.pega_nome()
            if not chave in self._arestas:
                conseguiu = vertice_1.conecta(vertice_2, aresta)
                if conseguiu:
                    self._arestas[chave] = aresta
                else:
                    return False

    def desconecta(self, vertice_1, vertice_2):
        chave = vertice_1.pega_nome() + vertice_2.pega_nome()
        if chave in self._arestas:
            conseguiu = vertice_1.desconecta(vertice_2, self._arestas[chave])
            if conseguiu:
                del self._arestas[chave]
                return True
            else:
                return False
        return desconecta(vertice_2, vertice_1)

    def ordem(self):
        return len(self._vertices)

    def vertices(self):
        return self._vertices.values()

    def um_vertice(self):
        return self._vertices.get(self._vertices.keys()[random.randint(0,len(self._vertices) - 1)])

    def adjacentes(self, vertice):
        return vertice.pega_adjacentes()

    def grau(self, vertice):
        return vertice.grau()

    def adiciona_vertice_por_nome(self, nome):
        vertice = Vertice(nome, False)
        if not nome in self._vertices:
            if not vertice.e_orientado():
                self._vertices[vertice.pega_nome()] = vertice
            else:
                raise Excecao_Adicao_de_Vertice(0)
        else:
            raise Excecao_Adicao_de_Vertice(1)
        return vertice

    def remove_vertice_por_nome(self, nome):
        if not self._vertices is None:
            if nome in self._vertices:
                this = self._vertices[nome]
                for vertice in self._vertices:
                    v = self._vertices[vertice]
                    if v.esta_conectado(this):
                        v.desconecta(this)
            del self._vertices[nome]

    def busca_em_profundidade(self, atual, jv, obj):
        if atual == obj:
            return True
        jv.append(atual)
        for y in atual.pega_adjacentes():
            if not y in jv:
                if self.busca_em_profundidade(y, jv, obj):
                    return True
        return False

    def busca_em_largura(self, inicio, obj):
        l = []
        jv = []
        l.append(inicio)
        i = 0
        while i < len(l):
            j = l[i]
            print j.pega_nome()
            if j == obj:
                return True
            jv.append(j)
            for adj in j.pega_adjacentes():
                if not adj in jv:
                    l.append(adj)
            i = i+1
        return False

    def tem_ciclo(self, atual, jv, anterior):
        jv.append(atual)
        for y in atual.pega_adjacentes():
            if y in jv and not y == anterior:
                return True
            if self.tem_ciclo(y, jv, anterior):
                return True
        return False