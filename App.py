import random

from Poblacion import Poblacion
from Solucion import *


class App:
    def __init__(self):
        ''''''

    @staticmethod
    def genetico(poblacion, factor_cruce, factor_mutacion):
        aux = poblacion.clone()
        nueva_generacion = list()
        # SELECCION NATURAL
        for i in range(0, int(len(poblacion) / 2)):
            index_1 = aux.seleccionar_padre()
            padre_1 = aux.individuos.pop(index_1)
            index_2 = aux.seleccionar_padre()
            padre_2 = aux.individuos.pop(index_2)
            # CRUZAMIENTO
            if (App.dardo() < factor_cruce):
                hijo_1, hijo_2 = App.cruzar(padre_1, padre_2)
                # MUTACION
                if (App.dardo() < factor_mutacion):
                    hijo_1.mutar()
                if (App.dardo() < factor_mutacion):
                    hijo_2.mutar()
                nueva_generacion.append(hijo_1)
                nueva_generacion.append(hijo_2)
            else:
                nueva_generacion.append(padre_1)
                nueva_generacion.append(padre_2)
        return Poblacion(nueva_generacion)

    @staticmethod
    def cruzar(solucion_1, solucion_2):
        count = len(solucion_1)
        hijo_1 = Solucion(solucion_1.barras[0:int(count * 0.5)], solucion_1.recurso)
        hijo_2 = Solucion(solucion_2.barras[0:int(count * 0.5)], solucion_2.recurso)
        for barra in solucion_2.barras:
            if barra not in hijo_1.barras:
                hijo_1.barras.append(barra)
        for barra in solucion_1.barras:
            if barra not in hijo_2.barras:
                hijo_2.barras.append(barra)
        hijo_1.calcular()
        hijo_2.calcular()
        return hijo_1, hijo_2

    @staticmethod
    def cruzar1(solucion_1, solucion_2):
        s1 = solucion_1.clone()
        s2 = solucion_2.clone()
        hijo_1 = Solucion(list(), solucion_1.recurso)
        hijo_2 = Solucion(list(), solucion_2.recurso)
        for i in range(0, len(solucion_1)):

            if i % 2 == 0:
                hijo_1.barras.append(s1.pop(i))
                hijo_2.barras.append(s1.pop(i))
            else:
                ''''''
        hijo_1.calcular()
        hijo_2.calcular()
        return hijo_1, hijo_2


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

    @staticmethod
    def dardo():
        return float(random.randint(0, 100) / 1000)
