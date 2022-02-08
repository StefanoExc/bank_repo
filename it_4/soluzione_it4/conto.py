from datetime import datetime

class Conto:
    def __init__(self, numero_conto, cliente, saldo=0.00,tassa_prelievo=1.00):
        self.__numero_conto = numero_conto
        self.__cliente = cliente
        self.__saldo = saldo
        self.__id=id(self)
        print(f'Istanza banca creata con id: {self.__id}')
        self.__tassa_prelievo=tassa_prelievo

    def id(self):
        return self.__id
    
     # Definizione di getter e setter #
    @property
    def numero_conto(self): 
        return self.__numero_conto
    
    @numero_conto.setter
    def numero_conto(self, numero_conto): 
        self.__numero_conto = numero_conto

    @property
    def cliente(self): 
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente): 
        self.__cliente = cliente

    @property
    def saldo(self): 
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo): 
        self.__saldo = saldo


    def __repr__(self):
        return "Conto " + self.numero_conto + " intestato a cliente " + self.cliente.nome_cliente  + " con saldo " + str(self.saldo) + "€"

    def versa_soldi(self,value):
        self.saldo += value

    def preleva_soldi(self,value):
        if self.__saldo < value + self.__tassa_prelievo: 
            print('Importo richiesto non presente sul conto')
        else: 
            self.__saldo -= value
            self.__saldo -= self.__tassa_prelievo
            print(f'Hai prelevato {value}. Nuovo saldo del conto: {self.__saldo}. Applicata una tassa di {self.__tassa_prelievo}')

class ContoSpecial(Conto):
    __tassa_prelievo = 2.00
    now = datetime.now()
    timestamp = datetime.timestamp(now)

    def __init__(self,data_inizio_debito=None):
        self.__data_inizio_debito = data_inizio_debito
        
    def preleva_soldi(self, value):
        self.__saldo-=self.__tassa_prelievo

        if self.__saldo < value + self.__tassa_prelievo:
            print (self.__data_inizio_debito == datetime.now() )

    def versa_soldi(self, value):
        super().versa_soldi(value)
        if self.__saldo > 0:
            self.__data_inizio_debito = None
            print ("Il conto è ora tornato disponibile")