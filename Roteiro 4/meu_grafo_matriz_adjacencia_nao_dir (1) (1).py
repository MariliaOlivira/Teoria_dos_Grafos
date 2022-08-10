from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        lista = []
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if (i < j and len(self.M[i][j]) == 0):
                    lista.append(f'{self.N[i]}-{self.N[j]}')
        return lista

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for passagem in range(len(self.M)):
            if len(self.M[passagem][passagem] != 0):
                return True
        return False



    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        graus = 0
        vertice = self.N.index(V)
        for passagem in range(len(self.M)):
            grau += len(self.M[vertice][passagem])
        return graus

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for linha in range(len(self.M)):
            for coluna in range(len(self.M)):
                if len(self.M[linha][coluna]) > 1:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException("O vértice passado como parâmetro não consta na lista de vértices existentes")
        lista = {}
        for linha in range(len(self.M)):
            for coluna in range(len(self.M)):
                aresta = self.M[linha][coluna]
                for arestas in aresta:
                    if arestas.getV1() == V or arestas.getV2() == V:
                        lista[arestas] = arestas
        return set(lista.keys())

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco():
            return False
        if self.ha_paralelas():
            return False
        if len(self.M) == 1 and len(self.M[0][0]) == 0:
            return True
        verificador = len(self.M)
        for linha in range(len(self.M)):
            grau = 0
            for coluna in range(len(self.M)):
                if coluna != linha:
                    grau += 1
            if grau != verificador - 1:
                return False
        return True
