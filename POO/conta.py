class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            print("O saldo não pode ser negativo")

conta = Conta(1200)
print(conta.get_saldo())

conta.set_saldo(2000)
print(conta.get_saldo())
conta.set_saldo(-50)



