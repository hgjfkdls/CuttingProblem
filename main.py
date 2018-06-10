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

    print('\ncreando poblacion inicial para:\n - recurso: {}\n poblacion maxima: {}\n - factor: {}\n...'.format(
        almacen[0], 20, len(barras) * 10))
    poblacion = Poblacion.crear_desde_solucion(solucion, 20, len(barras) * 10)

    print('\npoblacion inicial creada con {} elementos:'.format(len(poblacion.individuos)))
    print(' - mejor individuo: {}'.format(poblacion.mejor_individuo()))

    print('\ncreando una nueva generacion de individuos:')
    App.nueva_generacion(poblacion, 0.2, 0.2)
