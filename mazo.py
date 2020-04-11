class mazo():
    """docstring for mazo."""

    def inicializa_mazo():
        pass

    def carga_mazo():
        pass

    def guarda_mazo():
        pass

    def baraja_cartas():
        pass

    def pon_cartas_en_el_mazo_desde_otro_mazo(otro_mazo, num_cartas):
        pass

    def da_cartas_del_mazo_a_otro_mazo(otro_mazo, num_cartas):
        pass

    def switch_mazo(otro_mazo):
        pass

    def imprime_mazo():
        pass

    def da_cartas(otros_mazos, num_cartas):
        pass

    def dame_cartas(otro_mazo,num_cartas):
        pass

    def suelta_cartas(index_cartas):
        pass


    def __init__(self, vars_folder='./vars6', cards_folder='./imgs/small/', filename_mazo='mazo.var'):
        super(mazo, self).__init__()
        self.vars_folder = vars_folder
        self.cards_folder = cards_folder
        self.filename_mazo = vars_folder

        inicializa_mazo()
