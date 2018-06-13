from Recurso import *


class Barra:
    def __init__(self, id='', id_barra='', largo=0, diametro=0):
        self.id = id
        self.id_barra = id_barra
        self.largo = largo
        self.diametro = diametro

    @staticmethod
    def fn_heuristica_1(barras: list, recurso: Recurso) -> list:
        dic = Barra._get_order_dic_barras(barras)
        largos = list(dic.keys())
        if len(largos) == 0:
            return list()
        response = list()
        alive = True
        i_largo = 0
        barra_disponible = 0
        n_matches = 0
        sub_barras: list = None
        while alive:
            largo = largos[i_largo]
            if len(dic[largo]) > 0:
                if sub_barras is None:
                    barra_disponible = recurso.largo
                    sub_barras = list()
                    response.append(sub_barras)
                if largo <= barra_disponible:
                    i_largo = 0
                    sub_barras.append(dic[largo].pop(0))
                    barra_disponible = round(barra_disponible - largo, 4)
                    if barra_disponible == 0:
                        sub_barras = None
                    n_matches += 1
                    if n_matches == len(barras):
                        alive = False
                else:
                    i_largo += 1
            else:
                i_largo += 1
            if i_largo > len(largos) - 1:
                i_largo = 0
                sub_barras = None
        return response

    @staticmethod
    def _get_order_dic_barras(barras: list) -> dict:
        dic = dict()
        b: Barra
        for b in barras:
            if b.largo not in dic.keys():
                dic[b.largo] = list()
            dic[b.largo].append(b)
        return dic

    @staticmethod
    def create(requerimientos) -> list:
        l = list()
        id = 0
        for r in requerimientos:
            for c in range(r.cantidad):
                b = Barra(id, r.id, r.largo, r.diametro)
                l.append(b)
                id += 1
        return l

    @staticmethod
    def parse(values=['', '', '0', '0']):
        return Barra(
            values[0],
            values[1],
            float(values[3].replace(',', '.')),
            float(values[4].replace(',', '.')),
        )

    def __str__(self) -> str:
        return '<Barra id:{}, id_barra:{}, largo:{}, diametro:{}>'.format(self.id, self.id_barra,
                                                                          self.largo, self.diametro)

    def __repr__(self) -> str:
        return str(self)
