from pessoa import Pessoa
from datetime import datetime


class Doador(Pessoa):
    def __init__(self, cpf: str, nome: str, nascimento: datetime, endereco: str):
        super().__init__(cpf, nome, nascimento, endereco)
