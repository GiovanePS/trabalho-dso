from abc import ABC, abstractmethod
from datetime import date


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, cpf: str, nome: str,
                 nascimento: date, endereco: str):
        self.__cpf = cpf
        self.__nome = nome
        self.__nascimento = nascimento
        self.__endereco = endereco

    @property
    @abstractmethod
    def cpf(self):
        return self.__cpf

    @cpf.setter
    @abstractmethod
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    @abstractmethod
    def nome(self):
        return self.__nome

    @nome.setter
    @abstractmethod
    def nome(self, nome: str):
        self.__nome = nome

    @property
    @abstractmethod
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    @abstractmethod
    def nascimento(self, nascimento: date):
        self.__nascimento = nascimento

    @property
    @abstractmethod
    def endereco(self):
        return self.__endereco

    @endereco.setter
    @abstractmethod
    def endereco(self, endereco: str):
        self.__endereco = endereco
