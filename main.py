from App import App
from Requerimiento import *
from Recurso import *
from Barra import *

if __name__ == '__main__':

    requerimientos = Requerimiento.load_csv('C:/Users/Felipe Cabedo/Desktop/requerimientos.csv')
    almacen = Recurso.load_csv('C:/Users/Felipe Cabedo/Desktop/almacen.csv')
    barras = Barra.load_csv('C:/Users/Felipe Cabedo/Desktop/barras.csv')

    r = 0
    solucion = barras
    for i in range(len(barras) ** 2):
        beneficio = App.beneficio(barras, almacen[0])
        if beneficio > r:
            r = beneficio
            solucion = list(barras)
            print('{}'.format(beneficio))
        App.mutacion(barras)
