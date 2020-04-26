import random
import PIL
from PIL import Image
import numpy as np


class mazo():
    """docstring for mazo."""

    def inicializa_mazo(self):
        self.cartas = list(range(1,40+1))
        self.baraja_cartas()

    def carga_mazo():
        pass

    def guarda_mazo():
        pass

    def baraja_cartas(self):
        random.shuffle(self.cartas)

    # def pon_cartas_en_el_mazo_desde_otro_mazo(self, otro_mazo, num_cartas):
    #     dadas = 0
    #     while (otro_mazo.cartas and (dadas != num_cartas)):
    #         self.cartas.append(otro_mazo.cartas.pop())
    #         dadas += 1
    #     return dadas
    #

    def da_cartas_del_mazo_a_otro_mazo(self, otro_mazo, num_cartas):
        dadas = 0
        while (self.cartas and (dadas != num_cartas)):
            otro_mazo.cartas.append(self.cartas.pop())
            dadas += 1
        # devuelve el numero total de cartas que se han podido dar
        # si no hay suficientes en el mazo, se dan hasta que se acaben
        return dadas

    def switch_mazo(self, otro_mazo):
        old_mazo = self.cartas
        self.cartas = otro_mazo.cartas
        otro_mazo.cartas = old_mazo

    def imprime_mazo(self):
        f'Cartas: {self.cartas!r}'

    # def da_cartas(otro_mazo, num_cartas=4):
    #     pass

    # def dame_cartas(otro_mazo,num_cartas):
    #     otro_mazo.cartas.push(self.cartas)

    def suelta_cartas(self, index_cartas):
        return(self.cartas.pop(index_cartas))



    def get_imagen_carta(self, index_carta):
        filename_carta = str('{0}c{1}.png'.format(self.cards_folder, self.cartas[index_carta]))
        # print(filename_carta)
        img = Image.open(filename_carta)
        # img.show()

        return img


    def imprime_cartas(self):
        imgs = [self.get_imagen_carta(i) for i in range(self.num_cartas())]
        #thanks
        min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
        imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
        imgs_comb = PIL.Image.fromarray(imgs_comb)
        imgs_comb.show()


    def num_cartas(self):
        num = len(self.cartas)

        return num


    def __init__(self, vars_folder=str("./vars6"), cards_folder=str("/Users/fernando/Dropbox/PERSONAL/MUS/fer/Fer.v2/fer/imgs/cartas/"), filename_mazo=str("mazo.var")):
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
