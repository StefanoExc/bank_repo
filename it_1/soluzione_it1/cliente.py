class Cliente: 
    def __init__(self, nome_cliente, numero_telefono):
        self.__nome_cliente = nome_cliente
        self.__numero_telefono = numero_telefono

    def __repr__(self):
        return "Cliente " + self.__nome_cliente + " telefono " + self.__numero_telefono