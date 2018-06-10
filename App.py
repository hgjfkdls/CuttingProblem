import random
from Solucion import *


class App:
    def __init__(self):
        ''''''

    @staticmethod
    def nueva_generacion(poblacion, factor_cruce, factor_mutacion):
        for i in poblacion.individuos:
            print(i)
        aux = poblacion.clone()
        padres = list()
        for i in range(0, int(len(poblacion)/2)):
            index = aux.seleccionar_padre()
            seleccion = aux.individuos.pop(index)
            padres.append(seleccion)
            print('[{}] {} - {}'.format(i, index, seleccion))




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
