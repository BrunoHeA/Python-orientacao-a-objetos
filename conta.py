class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('O saldo do titular {} é de {}'.format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor
        print('Seu saldo foi de {} para {}'.format(self.__saldo - valor, self.__saldo))

    def pode_sacar(self, valor):
        valor_maximo = self.__saldo + self.__limite
        return valor <= valor_maximo

    def sacar(self, valor):
        if self.pode_sacar(valor):
            self.__saldo -= valor
            print('Saque efetuado com sucesso!')
        else:
            print('Saque malsucedido!')

    def transferir(self, valor, conta2):
        self.sacar(valor)
        conta2.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def numero_bancos():
        return 'BB: 001'
