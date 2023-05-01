from entidades.animal import Animal
from telas.tela_animal import TelaAnimal


class ControladorAnimal:
    def __init__(self, controlador_sistema):
        self.__animais = []
        self.__codigo_id_animal = 0
        self.__tela_animal = TelaAnimal()
        self.__controlador_sistema = controlador_sistema

    def pegar_animal_por_codigo(self, codigo):
        for animal in self.__animais:
            if animal.codigo == codigo:
                return animal
        return None

    def incluir_animal(self):
        self.__codigo_id_animal += 1
        dados_animal = self.__tela_animal.cadastro_animal()
        animal = Animal(self.__codigo_id_animal, dados_animal["nome"],
                        dados_animal["tipo"], dados_animal["raca"],
                        dados_animal["tamanho"])
        self.__animais.append(animal)

    def listar_animais(self):
        for animal in self.__animais:
            self.__tela_animal.mostra_animal(animal)

    def retornar_para_menu_principal(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        self.__tela_animal.abre_tela()
