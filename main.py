import re
import sys
from App import *

if __name__ == '__main__':
    fileName_1 = None
    fileName_2 = None

    App.print_bienvenida()

    for arg in sys.argv:
        if re.search('^--requerimientos:(.+)$', arg):
            fileName_1 = re.match('^--requerimientos:(.+)$', arg)[1]
        if re.search('^--recursos:(.+)$', arg):
            fileName_2 = re.match('^--recursos:(.+)$', arg)[1]

    if fileName_1 is None or fileName_2 is None:
        fileName_1 = 'C:/Users/Felipe Cabedo/Desktop/Optimizacion de Acero/requerimientos.csv'
        fileName_2 = 'C:/Users/Felipe Cabedo/Desktop/Optimizacion de Acero/recursos.csv'
        __extern_call__ = False

    App.load_files(fileName_1, fileName_2)
    App.print_ficheros()
    App.print_tabla_recursos()
    App.print_soluciones()
