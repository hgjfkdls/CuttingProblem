import random


class App:
    def __init__(self):
        ''''''

    @staticmethod
    def beneficio(solucion, barra_almacen):
        uso_barra = 0
        uso_total = 0
        n_barras = 0
        for barra in solucion:
            if uso_barra + barra.largo > barra_almacen.largo:
                if uso_barra == 0:
                    return 0
                uso_barra = 0
                n_barras += 1
            uso_barra += barra.largo
            uso_total += barra.largo
        beneficio = (uso_total * 100) / ((n_barras + 1) * barra_almacen.largo)
        return beneficio, n_barras

    @staticmethod
    def mutacion(solucion):
        index_1 = random.randint(0, len(solucion) - 1)
        index_2 = random.randint(0, len(solucion) - 1)
        while index_1 == index_2:
            index_2 = random.randint(0, len(solucion) - 1)
        solucion[index_1], solucion[index_2] = solucion[index_2], solucion[index_1]
        return solucion

    @staticmethod
    def permutacion(solucion):
        for i in range(len(solucion)):
            if i % 2 == 0:
                solucion[i], solucion[i + 1] = solucion[i + 1], solucion[i]

    @staticmethod
    def random_sort(solucion):
        s = list()
        rng = list(range(0, len(solucion)))
        c = len(rng)
        for i in range(c):
            a = len(rng) - 1
            index = random.randint(0, a)
            s.append(solucion[rng.pop(index)])
        return s
