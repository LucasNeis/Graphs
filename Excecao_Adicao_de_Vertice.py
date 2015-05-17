class Excecao_Adicao_de_Vertice(Exception):
    def __init__(self, problema):
        self.problema = problema

    def __str__(self):
        if self.problema == 0:
            return "O vertice não é do tipo desde grafo"
        if self.problema == 1:
            return "Este vertice já foi adicionado"
        return "Erro desconhecido"