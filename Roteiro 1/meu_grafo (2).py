from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        vna = set()

        for V1 in self.N:
            for V2 in self.N:
                achei = False
                for a in self.A:
                    if V1 != V2:
                        if (V1 == self.A[a].getV1() and V2 == self.A[a].getV2()) or ((V2 == self.A[a].getV1()) and V1 == self.A[a].getV2()):
                            achei = True
                if not achei and V1 != V2:
                    vna.add(f"{V1}-{V2}")
        return set(vna)

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in self.A:
            if self.A[i].getV1() == self.A[i].getV2():
                return True

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException("o vertice não é valido")
        grau = 0
        for i in self.A:
            if self.A[i].getV1() == V:
                grau += 1
            if self.A[i].getV2() == V:
                grau += 1
        return grau
    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        arestas = self.A

        for i in arestas:

            for j in arestas:
                if arestas[j] == arestas[i]:
                    continue
                if arestas[i].getV1() == arestas[j].getV1() and arestas[i].getV2() == arestas[j].getV2():
                    return True
                if arestas[i].getV1() == arestas[j].getV2() and arestas[i].getV2() == arestas[j].getV1():
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        lista = {}

        if V not in self.N:
            raise VerticeInvalidoException("O vertice não é valido")
        for i in self.A:
            if self.A[i].getV1() == V or self.A[i].getV2() == V:
                lista[i] = (self.A[i].getRotulo())
        return lista.keys()

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_paralelas() or self.ha_laco() or len(self.vertices_nao_adjacentes()) > 0:
            return False

        return True
