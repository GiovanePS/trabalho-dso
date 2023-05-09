from entidades.pessoa import Pessoa
from datetime import date


class Adotante(Pessoa):
    def __init__(
        self,
        cpf: str,
        nome: str,
        data_nascimento: date,
        endereco: str,
        tipo_habitacao: str,
        tem_animais: bool,
    ):
        super().__init__(cpf, nome, data_nascimento, endereco)
        self.__tipo_habitacao = tipo_habitacao
        self.__tem_animais = tem_animais

    @property
    def tipo_habitacao(self):
        return self.__tipo_habitacao

    @tipo_habitacao.setter
    def tipo_habitacao(self, tipo_habitacao: str):
        self.__tipo_habitacao = tipo_habitacao

    @property
    def tem_animais(self):
        return self.__tem_animais

    @tem_animais.setter
    def tem_animais(self, tem_animais: bool):
        self.__tem_animais = tem_animais
