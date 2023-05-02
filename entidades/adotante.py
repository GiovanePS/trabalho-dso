from pessoa import Pessoa
from datetime import datetime


class Adotante(Pessoa):
    def __init__(
        self,
        cpf: str,
        nome: str,
        nascimento: datetime,
        endereco: str,
        tipo_habitacao: str,
        tem_animais: bool,
    ):
        super().__init__(cpf, nome, nascimento, endereco)
        self.__tipo_habitacao = tipo_habitacao
        self.__tem_animais = tem_animais

    @property
    def tipo_habitacao(self):
        return self.__tipo_habitacao

    @tipo_habitacao.setter
    def tipo_habitacao(self, tipo_habitacao):
        self.__tipo_habitacao = tipo_habitacao

    @property
    def tem_animais(self):
        return self.__tem_animais

    @tem_animais.setter
    def tem_animais(self, tem_animais):
        self.__tem_animais = tem_animais
