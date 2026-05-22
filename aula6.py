#classe com atributo encapsulado
class Conta:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial # Atributo privado
    #métodos de acesso
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor} realizado.")
        else:
            print("Operação inválida!")

    def consultar_saldo(self):
        return self.__saldo

# Testando
conta_bruno = Conta(100)
conta_bruno.depositar(50)
#print(conta_bruno.__saldo)
print(f"Saldo atual: R$ {conta_bruno.consultar_saldo()}")



class Produto:
    def __init__(self, preco):
        self.__preco = preco

    def get_preco(self):
        return self.__preco

    def set_preco(self, valor):
        if valor >= 0:
            self.__preco = valor