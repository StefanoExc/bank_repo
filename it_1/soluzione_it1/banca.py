class Banca: 
    def __init__(self, nome_banca): 
        self.__nome_banca = nome_banca
        self.__clienti = []
        self.__conti_correnti = []

    def __repr__(self):
        return "Nome banca " + self.__nome_banca + " numero totale di clienti " + str(len(self.__clienti)) + " numero totale di conti correnti: " + str(len(self.__conti_correnti)) 