from Requerimiento import *
from Solucion import *


class App:
    __version__ = '0.001.001'
    filePath_requerimientos = None
    filePath_recursos = None
    requerimientos = None
    recursos = None
    barras = None

    @staticmethod
    def load_files(filePath_requerimientos: str, filePath_recursos: str):
        App.filePath_requerimientos = filePath_requerimientos
        App.filePath_recursos = filePath_recursos
        App.requerimientos = Requerimiento.load_csv(filePath_requerimientos)
        App.recursos = Recurso.load_csv(filePath_recursos)
        App.barras = Barra.create(App.requerimientos)

    @staticmethod
    def calcular_solucion(recurso: Recurso) -> Solucion:
        barras = [b for b in App.barras if b.diametro == recurso.diametro]
        barras = sorted(barras, key=lambda b: b.largo, reverse=True)
        requerimientos = [r for r in App.requerimientos if r.diametro == recurso.diametro]
        solucion = Solucion(requerimientos, Barra.fn_heuristica_1(barras, recurso), recurso)
        return solucion

    @staticmethod
    def print_soluciones():
        print('{}'.format(' soluciones de heurística 1 '.center(80, '-')))
        print('')
        for r in App.recursos:
            App.print_solucion(r)

    @staticmethod
    def print_solucion(recurso: Recurso):
        solucion = App.calcular_solucion(recurso)
        print('recurso     : {}'.format(recurso.id))
        print('descripción : {}'.format(recurso.descripcion))
        print('largo       : {}'.format(recurso.largo))
        print('diámetro    : {}'.format(recurso.diametro))
        print('beneficio   : {}'.format(solucion.beneficio))
        print('cortes      : {}'.format(solucion.num_cortes))
        print('barras      : {}'.format(solucion.num_barras))
        print('')
        App.print_tabla_requerimientos(solucion)
        print('- solución:')
        if len(solucion.barras) == 0:
            print('')
            print(' - No existen barras para este recurso.')
            print('')
            return
        print('#tipo,largo,uso total,uso barra,num barra,merma,merma_acumulada')
        n_barra = 0
        corte: Barra
        uso_total = 0
        merma_acumuladada = 0
        for barra in solucion.barras:
            uso_barra = 0
            n_barra += 1
            for corte in barra:
                uso_barra = round(uso_barra + corte.largo, 4)
                uso_total = round(uso_total + corte.largo, 4)
                merma = round(recurso.largo - uso_barra, 4)
                if corte == barra[-1]:
                    merma_acumuladada = round(merma_acumuladada + merma, 4)
                    print('#{},{},{},{},{},{},{}'.format(corte.id_barra,
                                                         corte.largo,
                                                         uso_total,
                                                         uso_barra,
                                                         n_barra,
                                                         merma,
                                                         merma_acumuladada
                                                         )
                          )
                else:
                    print('#{},{},{},{},{},{},{}'.format(corte.id_barra,
                                                         corte.largo,
                                                         uso_total,
                                                         uso_barra,
                                                         '',
                                                         '',
                                                         ''
                                                         )
                          )
        print('')

    @staticmethod
    def print_bienvenida():
        print('{}'.format(' Optimizador de Acero '.center(80, '=')))
        print('')
        print('- autor   : Felipe Cabedo')
        print('- mail    : fcabedov@gmail.com')
        print('- version : {}'.format(App.__version__))
        print('')

    @staticmethod
    def print_ficheros():
        print('{}'.format(' ficheros de lectura '.center(80, '-')))
        print('')
        print('- requerimiento : {}'.format(App.filePath_requerimientos))
        print('- recursos      : {}'.format(App.filePath_recursos))
        print('')

    @staticmethod
    def print_tabla_recursos():
        print('{}'.format(' tabla de recursos '.center(80, '-')))
        print('')
        print('#id,descripción,largo,diámetro')
        for r in App.recursos:
            print('#{},{},{},{}'.format(r.id, r.descripcion, r.largo, r.diametro))
        print('')

    @staticmethod
    def print_tabla_requerimientos(solucion: Solucion):
        print('- tabla de requerimientos:')
        if solucion.num_cortes == 0:
            print('')
            print('  - No existen requerimientos para este recurso.')
            print('')
            return
        print('#id,D,L,C,Lt,f1,f2,f3')
        L = solucion.recurso.largo
        Lt = L * solucion.num_cortes
        r: Requerimiento
        for r in solucion.requerimientos:
            l = r.largo
            d = r.diametro
            c = r.cantidad
            lt = l * c
            f1 = lt / Lt
            f2 = l / L
            f3 = f1 / f2
            print('#{},{},{},{},{},{},{},{}'.format(r.id, d, l, c, lt, f1, f2, f3))
        print('')
