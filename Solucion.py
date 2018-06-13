from Barra import *


class Solucion:
    def __init__(self, requerimientos: list, barras: list, recurso: Recurso):
        self.requerimientos = requerimientos
        self.barras = barras
        self.recurso = recurso
        self.num_barras = len(barras)
        self.beneficio = self.calcular_beneficio()

    def calcular_beneficio(self) -> float:
        uso_total = 0
        corte: Barra
        self.num_cortes = 0
        for barra in self.barras:
            uso_barra = 0
            for corte in barra:
                self.num_cortes += 1
                uso_barra = round(uso_barra + corte.largo, 4)
                uso_total = round(uso_total + corte.largo, 4)
        return 0 if self.num_barras == 0 else (uso_total * 100) / (self.num_barras * self.recurso.largo)

    def __len__(self):
        return len(self.barras)

    def __str__(self):
        return '<Solucion [beneficio: {}, barras: {}]>'.format(self.beneficio, self.num_barras)
