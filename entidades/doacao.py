from doador import Doador
from animal import Animal
from datetime import datetime


class Doacao:
    def __init__(
        self,
        data_doacao: datetime,
        animal: Animal,
        doador: Doador,
        motivo: str,
        id_doacao: int,
    ):
        self.__data_doacao = data_doacao
        self.__animal = animal
        self.__doador = doador
        self.__motivo = motivo
        self.__id_doacao = id_doacao

    @property
    def data_doacao(self):
        return self.__data_doacao

    @data_doacao.setter
    def data_doacao(self, data_doacao):
        self.__data_doacao = data_doacao

    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, animal):
        self.__animal = animal

    @property
    def doador(self):
        return self.__doador

    @doador.setter
    def doador(self, doador):
        self.__doador = doador

    @property
    def motivo(self):
        return self.__motivo

    @motivo.setter
    def motivo(self, motivo):
        self.__motivo = motivo

    @property
    def id_doacao(self):
        return self.__id_doacao
