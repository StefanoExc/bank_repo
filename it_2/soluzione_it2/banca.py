class Banca: 
    def __init__(self, nome_banca): 
        self.__nome_banca = nome_banca
        self.__clienti = []
        self.__conti_correnti = []

    @property
    def nome_banca(self):
        return self.__nome_banca

    @nome_banca.setter
    def nome_banca(self,nome_banca):
        self.__nome_banca=nome_banca

    @property
    def clienti(self):
        return self.__clienti

    @clienti.setter
    def clienti(self,clienti):
        self.__clienti=clienti

    @property
    def conti_correnti(self): 
        return self.__conti_correnti

    @conti_correnti.setter
    def numero_telefono(self, conti_correnti): 
        self.__conti_correnti = conti_correnti

    def __repr__(self):
        return "Nome banca " + self.__nome_banca + " numero totale di clienti " + str(len(self.__clienti)) + " numero totale di conti correnti: " + str(len(self.__conti_correnti))


    