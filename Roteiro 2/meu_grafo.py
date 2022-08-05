from tkinter import N
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        FEITO
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        lista_final = []
        for passagem1 in self.N:
            lista_provisoria = []

            for passagem2 in self.A:
                if self.A[passagem2].getV1() == passagem1:
                    lista_provisoria.append(self.A[passagem2].getV2())
                elif self.A[passagem2].getV2() == passagem1:
                    lista_provisoria.append(self.A[passagem2].getV1())

            for passagem3 in self.N:
                if passagem1 != passagem3 and passagem3 not in lista_provisoria:
                    lista_final.append(f'{passagem1}-{passagem3}')
                    lista_final.append(f'{passagem3}-{passagem1}')
        return set(lista_final)

    def ha_laco(self):
        '''
        FEITO
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for passagem in self.A:
            if self.A[passagem].getV1() == self.A[passagem].getV2():
                return True
        return False


    def grau(self, V=''):
        '''
        FEITO
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException("O vértice passado como parâmetro não consta na lista de vértices existentes") 
        grau = 0
        for passagem in self.A:
            if self.A[passagem].getV1() == V:
                grau += 1
            if self.A[passagem].getV2() == V:
                grau += 1
        return grau

    def ha_paralelas(self):
        '''
        FEITO
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for passagem1 in self.A:
            vertice1, vertice2 = self.A[passagem1].getV1(), self.A[passagem1].getV2()
            for passagem2 in self.A:
                if passagem2 != passagem1:
                    if (vertice1 == self.A[passagem2].getV1() or vertice1 == self.A[passagem2].getV2()) and (vertice2 == self.A[passagem2].getV1() or vertice2 == self.A[passagem2].getV2()):
                        return True
        return False


    def arestas_sobre_vertice(self, V):
        '''
        FEITO
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException("O vértice passado como parâmetro não consta na lista de vértices existentes")
        lista = {}
        for passagem in self.A:
            if self.A[passagem].getV1() == V or self.A[passagem].getV2() == V:
                lista[passagem] = (self.A[passagem].getRotulo())
        return set(lista.keys())
        
            


    def eh_completo(self):
        '''
        FEITO
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco():
            return False
        if self.ha_paralelas():
            return False
        contador = 0
        if len(self.N) == 1 and len(self.A) == 0:
            return True
        verificador = len(self.N)
        for passagem1 in self.N:
            lista_provisoria = []
            for passagem2 in self.A:
                if self.A[passagem2].getV1() == passagem1:
                    lista_provisoria.append(self.A[passagem2].getV2())
                elif self.A[passagem2].getV2() == passagem1:
                    lista_provisoria.append(self.A[passagem2].getV1())
            if self.grau(passagem1) != verificador - 1:
                return False
        return True

    def bfs(self, V=''):
        novoGrafo = MeuGrafo([])
        return self.bfs_aux(novoGrafo, V)

    def bfs_aux(self, novoGrafo , V = '', lista = []):
        
        root = V
        if lista != []:
            root = lista[0]
            lista.pop(0)
        for a in self.A:
            if root not in novoGrafo.N:
                novoGrafo.adicionaVertice(root)
            if self.A[a].getV1() == root and self.A[a].getV2() not in novoGrafo.N:
                novoGrafo.adicionaVertice(self.A[a].getV2())
                lista.append(self.A[a].getV2())
                novoGrafo.adicionaAresta(a, root, self.A[a].getV2())
            elif self.A[a].getV2() == root and self.A[a].getV1() not in novoGrafo.N:
                novoGrafo.adicionaVertice(self.A[a].getV1())
                lista.append(self.A[a].getV1())
                novoGrafo.adicionaAresta(a, self.A[a].getV1(), root)

        if len(novoGrafo.N) == len(self.N):
            return novoGrafo
        else:
            novaroot = lista[0]
            self.bfs_aux(novoGrafo, novaroot, lista)
        return novoGrafo

    def dfs(self, V=''):
        novoGrafo = MeuGrafo([])
        return self.dfs_aux(novoGrafo, V)


    def dfs_aux(self,novoGrafo, V = ''):

        root = V
        for a in self.A:
            if root not in novoGrafo.N:
                novoGrafo.adicionaVertice(root)
            if self.A[a].getV1() == root and self.A[a].getV2() not in novoGrafo.N:
                novoGrafo.adicionaVertice(self.A[a].getV2())
                novoGrafo.adicionaAresta(a, root, self.A[a].getV2())
                self.dfs_aux(novoGrafo, self.A[a].getV2())
            if self.A[a].getV2() == root and self.A[a].getV1() not in novoGrafo.N:
                novoGrafo.adicionaVertice(self.A[a].getV1())
                novoGrafo.adicionaAresta(a, self.A[a].getV1(), root)
                self.dfs_aux(novoGrafo, self.A[a].getV1())

        return novoGrafo

    def dijkstra_drone(self, vi, vf, carga:int, carga_max:int, pontos_recarga:list()):
        pass