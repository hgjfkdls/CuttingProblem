from App import App
from Poblacion import Poblacion
from Requerimiento import *
from Recurso import *
from Barra import *
from Solucion import *

if __name__ == '__main__':
    requerimientos = Requerimiento.load_csv('C:/Users/Felipe Cabedo/Desktop/requerimientos.csv')
    almacen = Recurso.load_csv('C:/Users/Felipe Cabedo/Desktop/almacen.csv')
    barras = Barra.load_csv('C:/Users/Felipe Cabedo/Desktop/barras.csv')

    print('\nnumero de barras: {}'.format(len(barras)))
    solucion = Solucion(barras[:], almacen[0])
    print(' - Solucion de lectura inicial: {}'.format(solucion))
    solucion = Solucion(App.random_sort(barras[:]), almacen[0])
    print(' - Solucion de orden aleatorio: {}'.format(solucion))

    print('\ncreando poblacion inicial para:\n - recurso: {}\n - poblacion maxima: {}\n - factor: {}\n...'.format(
        almacen[0], 50, len(barras) * 10))
    poblacion = Poblacion.crear_desde_solucion(solucion, 50, len(barras))

    print('\npoblacion inicial creada con {} elementos:'.format(len(poblacion.individuos)))
    print(' - mejor individuo: {}'.format(poblacion.mejor_individuo()))

    print('\ncreando una nueva generacion de individuos:')

    solucion = None
    lista_aux = list()
    for i in range(0, 1000):
        mejor = poblacion.mejor_individuo()
        print('[{}] {}'.format(i, mejor))
        if solucion is None or mejor.beneficio > solucion.beneficio:
            solucion = Solucion(mejor.barras, almacen[0])
        lista_aux.append(mejor)
        if len(lista_aux) > 50:
            poblacion = Poblacion(lista_aux[0:49])
        poblacion = App.genetico(poblacion, 0.5, 0.2)

    print('-' * 50)
    print(solucion)
