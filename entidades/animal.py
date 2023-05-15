class Animal:
    def __init__(self, codigo: int, nome: str,
                 tipo: str, raca: str, tamanho: str = ''):
        self.__codigo = codigo
        self.__nome = nome
        self.__tipo = tipo
        self.__raca = raca
        self.__tamanho = tamanho
        self.__vacinas = []
        self.__foi_adotado = False
        self.__pode_ser_adotado = False

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca: str):
        self.__raca = raca

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho: str):
        self.__tamanho = tamanho

    @property
    def vacinas(self):
        return self.__vacinas

    @property
    def foi_adotado(self):
        return self.__foi_adotado

    @foi_adotado.setter
    def foi_adotado(self, foi_adotado: bool):
        self.__foi_adotado = foi_adotado

    @property
    def pode_ser_adotado(self):
        return self.__pode_ser_adotado

    @pode_ser_adotado.setter
    def pode_ser_adotado(self, pode_ser_adotado: bool):
        self.__pode_ser_adotado = pode_ser_adotado
