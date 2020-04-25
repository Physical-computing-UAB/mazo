import random


class mazo():
    """docstring for mazo."""

    def inicializa_mazo(self):
        self.cartas = list(range(1,40+1))

        # ahora lo guardo
        pass

    def carga_mazo():
        pass

    def guarda_mazo():
        pass

    def baraja_cartas(self):
        random.shuffle(self.cartas)

    def pon_cartas_en_el_mazo_desde_otro_mazo(self, otro_mazo, num_cartas):
        self.cartas.push(otro_mazo.cartas.pop(num_cartas))

    def da_cartas_del_mazo_a_otro_mazo(self, otro_mazo, num_cartas):
        otro_mazo.cartas.push(self.cartas.pop(num_cartas))

    def switch_mazo(self, otro_mazo):
        old_mazo = self.cartas
        self.cartas = otro_mazo.cartas
        otro_mazo.cartas = old_mazo

    def imprime_mazo():
        f'Cartas: {self.cartas!r}'

    def da_cartas(otros_mazos, num_cartas=4):
        pass

    def dame_cartas(otro_mazo,num_cartas):
        otro_mazo.cartas.push(self.cartas)

    def suelta_cartas(index_cartas):
        return(self.cartas.pop(index_cartas))
        


    def __init__(self, vars_folder='./vars6', cards_folder='./imgs/small/', filename_mazo='mazo.var'):
        # super(mazo, self).__init__()

        # folders
        self.vars_folder = vars_folder
        self.cards_folder = cards_folder
        self.filename_mazo = vars_folder

        # instance variables
        self.cartas = []

        self.inicializa_mazo()


    def __repr__(self):
        return f'Cartas: {self.cartas!r}'
