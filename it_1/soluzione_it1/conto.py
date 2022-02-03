from sys import settrace


class Conto:
    def __init__(self, numero_conto, cliente, saldo=0.00):
        self.__numero_conto = numero_conto
        self.__cliente = cliente
        self.__saldo = saldo

    def __repr__(self):
        return "Conto " + self.__numero_conto + " intestato a cliente " + self.__cliente  + " con saldo " + str(self.__saldo) + "€"
