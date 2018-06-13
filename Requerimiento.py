import csv


class Requerimiento:
    def __init__(self, id='', descripcion='', largo=0, diametro='', cantidad=0):
        self.id = id
        self.descripcion = descripcion
        self.largo = largo
        self.diametro = diametro
        self.cantidad = cantidad

    @staticmethod
    def load_csv(filepath):
        r = []
        with open(filepath, newline='') as f:
            sr = csv.reader(f, delimiter=',', quotechar='"')
            i = 0
            for row in sr:
                i += 1
                if i > 2:
                    r.append(Requerimiento.parse(row))
        return r

    @staticmethod
    def parse(values=['', '', '0', '0', '0']):
        return Requerimiento(
            values[0],
            values[1],
            float(values[2].replace(',', '.')),
            float(values[3].replace(',', '.')),
            int(values[4])
        )

    def __str__(self):
        return '<id:{}, descripcion:{}, largo:{}, diametro:{}, cantidad: {}>'.format(self.id, self.descripcion,
                                                                                     self.largo, self.diametro,
                                                                                     self.cantidad)
