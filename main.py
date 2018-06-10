from App import App
from Requerimiento import *
from Almacen import *
from Barra import *

if __name__ == '__main__':

    requerimientos = Requerimiento.load_csv('C:/Users/Felipe Cabedo/Desktop/requerimientos.csv')
    recursos = Almacen.load_csv('C:/Users/Felipe Cabedo/Desktop/almacen.csv')
    barras = Barra.load_csv('C:/Users/Felipe Cabedo/Desktop/barras.csv')

    r = 0
    for i in range(100):
        beneficio = App.beneficio(barras, recursos[0])
        if beneficio > r:
            r = beneficio
            print('{}'.format(beneficio))
        App.mutacion(barras)
