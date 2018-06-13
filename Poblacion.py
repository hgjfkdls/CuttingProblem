import random
from Solucion import Solucion


class Poblacion:

    def __init__(self, individuos=None):
        if individuos is None:
            self.individuos = list()
        else:
            self.individuos = sorted(individuos, key=lambda s: s.beneficio, reverse=True)

    def ordenar(self):
        self.individuos = sorted(self.individuos, key=lambda s: s.beneficio, reverse=True)

    @staticmethod
    def crear_desde_solucion(solucion, soluciones_maximas, contador=1000):
        individuos = list()
        beneficio_aux = 0
        contador_1 = 0
        contador_2 = 0
        solucion_aux = Solucion(solucion.barras[:], solucion.recurso)
        while contador_1 < contador:
            contador_1 += 1
            contador_2 += 1
            if solucion_aux.beneficio >= beneficio_aux:
                individuos.append(Solucion(solucion_aux.barras[:], solucion_aux.recurso))
                individuos = sorted(individuos, key=lambda s: s.beneficio, reverse=True)
                if len(individuos) > soluciones_maximas:
                    individuos = individuos[:-1]
                beneficio_aux = individuos[-1].beneficio
                contador_1 = 0
            solucion_aux.mutar()
            solucion_aux.calcular_beneficio()
        return Poblacion(individuos)

    def seleccionar_padre(self):
        rango = self.mejor_individuo().beneficio - self.peor_individuo().beneficio
        rango = 1 if rango == 0 else rango
        lst = list()
        acumulado = 0
        index = len(self)
        for i in reversed(self.individuos):
            index -= 1
            ponderador = int((rango - (self.mejor_individuo().beneficio - i.beneficio)) / rango * 99) + 1
            acumulado += ponderador
            lst.append((acumulado, index))
        selector = random.randint(0, acumulado)
        for i in lst:
            if i[0] >= selector:
                break
        return i[1]

    def clone(self):
        return Poblacion(self.individuos[:])

    def __len__(self):
        return len(self.individuos)

    def mejor_individuo(self):
        return self.individuos[0]

    def peor_individuo(self):
        return self.individuos[-1]

    def __str__(self):
        return ''
