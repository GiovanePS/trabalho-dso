from pessoa import Pessoa
from datetime import date


class Doador(Pessoa):
    def __init__(self, cpf: str, nome: str,
                 nascimento: date, endereco: str):
        super().__init__(cpf, nome, nascimento, endereco)
        self.__cpf = cpf
        self.__nome = nome
        self.__nascimento = nascimento
        self.__endereco = endereco

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nascimento: date):
        self.__nascimento = nascimento

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco
