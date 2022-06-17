# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 12:17:51 2022

@author: Timmers Arruda
"""

class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class FilaD:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def estaVazia(self):
        return self.quant == 0

    def getPrimeiro(self):
        return self.prim.info

    def getUltimo(self):
        return self.ult.info

    def getQuant(self):
        return self.quant

    def inserir(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.ult.prox = self.ult = No(valor, None)
        self.quant += 1

    def remover(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1

    def imprimir(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end =' ')
            aux = aux.prox
        print()

