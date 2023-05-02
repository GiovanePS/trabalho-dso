from adotante import Adotante
from animal import Animal
from datetime import datetime


class Adocao:
    def __init__(
        self,
        data_adocao: datetime,
        animal_adotado: Animal,
        adotante: Adotante,
        assinatura: bool,
        id_adocao: int,
    ):
        self.__data_adocao = data_adocao
        self.__animal_adotado = animal_adotado
        self.__adotante = adotante
        self.__assinatura = assinatura
        self.__id_adocao = id_adocao

    @property
    def data_adocao(self):
        return self.__data_adocao

    @data_adocao.setter
    def data_adocao(self, data_adocao):
        self.__data_adocao = data_adocao

    @property
    def animal_adotado(self):
        return self.__animal_adotado

    @animal_adotado.setter
    def animal_adotado(self, animal_adotado):
        self.__animal_adotado = animal_adotado

    @property
    def adotante(self):
        return self.__adotante

    @adotante.setter
    def adotante(self, adotante):
        self.__adotante = adotante

    @property
    def assinatura(self):
        return self.__assinatura

    @assinatura.setter
    def assinatura(self, assinatura):
        self.__assinatura = assinatura

    @property
    def id_adocao(self):
        return self.__id_adocao
