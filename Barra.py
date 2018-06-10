import csv


class Barra:
    def __init__(self, id='', id_barra='', largo=0, diametro=0):
        self.id = id
        self.id_barra = id_barra
        self.largo = largo
        self.diametro = diametro

    @staticmethod
    def load_csv(filepath):
        r = []
        with open(filepath, newline='') as f:
            sr = csv.reader(f, delimiter=';', quotechar='"')
            i = 0
            for row in sr:
                i += 1
                if i > 2:
                    r.append(Barra.parse(row))
        return r

    @staticmethod
    def parse(values=['', '', '0', '0']):
        return Barra(
            values[0],
            values[1],
            float(values[3].replace(',', '.')),
            float(values[4].replace(',', '.')),
        )

    def __str__(self):
        return '<id:{}, id_barra:{}, largo:{}, diametro:{}>'.format(self.id, self.id_barra,
                                                                    self.largo, self.diametro)
