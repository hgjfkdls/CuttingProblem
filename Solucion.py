from App import *


class Solucion:
    def __init__(self, barras, recurso):
        self.barras = barras
        self.recurso = recurso
        self.beneficio, self.n_barras = self.calcular()

    def calcular(self):
        uso_barra = 0
        uso_total = 0
        n_barras = 0
        for barra in self.barras:
            if uso_barra + barra.largo > self.recurso.largo:
                if uso_barra == 0:
                    return 0
                uso_barra = 0
                n_barras += 1
            uso_barra += barra.largo
            uso_total += barra.largo
        return (uso_total * 100) / ((n_barras + 1) * self.recurso.largo), n_barras

    def mutar(self):
        index_1 = random.randint(0, len(self.barras) - 1)
        index_2 = random.randint(0, len(self.barras) - 1)
        while index_1 == index_2:
            index_2 = random.randint(0, len(self.barras) - 1)
        self.barras[index_1], self.barras[index_2] = self.barras[index_2], self.barras[index_1]

    def __str__(self):
        return '<Solucion [beneficio: {}, barras: {}]>'.format(self.beneficio, self.n_barras)
