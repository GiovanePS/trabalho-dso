from entidades.animal import Animal
from entidades.vacina import Vacina
from datetime import datetime


class Vacinacao:
    def __init__(self, data_vacina: datetime,
                 vacina: Vacina, animal: Animal,
                 id_vacinacao: int):
        self.__data_vacina = data_vacina
        self.__vacina = vacina
        self.__animal = animal
        self.__id_vacinacao = id_vacinacao

    @property
    def data_vacina(self):
        return self.__data_vacina

    @data_vacina.setter
    def data_vacina(self, data_vacina):
        self.__data_vacina = data_vacina

    @property
    def vacina(self):
        return self.__vacina

    @vacina.setter
    def vacina(self, vacina):
        self.__vacina = vacina

    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, animal):
        self.__animal = animal

    @property
    def id_vacinacao(self):
        return self.__id_vacinacao
