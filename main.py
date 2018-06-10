from App import App
from Requerimiento import *
from Recurso import *
from Barra import *

if __name__ == '__main__':

    requerimientos = Requerimiento.load_csv('C:/Users/Felipe Cabedo/Desktop/requerimientos.csv')
    almacen = Recurso.load_csv('C:/Users/Felipe Cabedo/Desktop/almacen.csv')
    barras = Barra.load_csv('C:/Users/Felipe Cabedo/Desktop/barras.csv')

    solucion = App.random_sort(barras)
    solucion_aux = solucion[:]

    print('numero de barras: {}'.format(len(barras)))
    print('')
    print('creando poblacion inicial')
    print('-' * 80)

    beneficio_aux = 0
    for i in range(len(barras) * 100):
        beneficio, n_barras = App.beneficio(solucion, almacen[0])
        if beneficio > beneficio_aux:
            beneficio_aux = beneficio
            solucion_aux = list(solucion)
            print('[{}] beneficio: {} {}'.format(i, beneficio, n_barras))
        App.mutacion(solucion)
