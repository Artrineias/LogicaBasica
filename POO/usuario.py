from ast import Return


class usuario:
    ## construtur
    def __init__(self,name,idade,senha,saldo):
        ##Atributos ou caracteristicas da class
        self.name = name
        self.idade = idade
        self.senha = senha
        self.saldo = saldo
    
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,valor):
        self._name = valor


    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self,valor):
        self._idade = valor


    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self,valor):
        self._saldo = valor

    @staticmethod
    def verificador(senha):
        for i in range(0,4,1):
            if i != 0:
                print(f"{i}°tentativa")
            s = input("Digite a senha: ")
            if senha == s:
                return True
        return False