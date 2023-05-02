from abc import ABC, abstractmethod
from datetime import datetime


class Pessoa:
    @abstractmethod
    def __init__(self, cpf: str, nome: str, nascimento: datetime, endereco: str):
        self.__cpf = cpf
        self.__nome = nome
        self.__nascimento = nascimento
        self.__endereco = endereco

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
