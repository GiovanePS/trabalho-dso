from entidades.animal import Animal
from telas.tela_animal import TelaAnimal
from DAOs.animal_dao import AnimalDAO
import os


class ControladorAnimal:
    def __init__(self, controlador_sistema):
        self.__animal_DAO = AnimalDAO()
        if len(self.__animal_DAO.get_all()) == 0:
            self.__codigo = 0
        else:
            self.__codigo = list(self.__animal_DAO.get_all())[-1].codigo
        self.__tela_animal = TelaAnimal()
        self.__controlador_sistema = controlador_sistema

    @property
    def animais(self):
        return self.__animal_DAO
    
    @property
    def tela_animal(self):
        return self.__tela_animal

    def pegar_animal_por_codigo(self, codigo_animal: int):
        for animal in self.__animal_DAO.get_all():
            if animal.codigo == int(codigo_animal):
                return animal
        return None

    def incluir_animal(self):
        self.__tela_animal.mensagem("Cadastro de animal.")
        dados_animal = self.__tela_animal.pega_dados_animal()
        self.__codigo += 1
        animal = Animal(
            self.__codigo,
            dados_animal["nome"],
            dados_animal["tipo"],
            dados_animal["raca"],
            dados_animal["tamanho"],
        )
        self.__animal_DAO.add(animal)
        os.system("cls")
        self.__tela_animal.mensagem("Animal cadastrado com sucesso!")
        print()

    def alterar_animal(self):
        self.listar_animais()
        self.__tela_animal.mensagem("Alteração cadastral de animal.")
        codigo_selecionado = self.__tela_animal.seleciona_codigo_animal()
        animal = self.pegar_animal_por_codigo(codigo_selecionado)
        if isinstance(animal, Animal):
            novos_dados_animal = self.__tela_animal.pega_dados_animal()
            animal.nome = novos_dados_animal["nome"]
            animal.tipo = novos_dados_animal["tipo"]
            animal.raca = novos_dados_animal["raca"]
            animal.tamanho = novos_dados_animal["tamanho"]
            self.__animal_DAO.update(animal)
            os.system("cls")
            self.__tela_animal.mensagem("Alteração realizada com sucesso!")
        else:
            os.system("cls")
            self.__tela_animal.mensagem("Animal inexistente no sistema.")
        print()

    def excluir_animal(self):
        self.__tela_animal.mensagem("Exclusão de animal do sistema.")
        codigo_selecionado = self.__tela_animal.seleciona_codigo_animal()
        animal = self.pegar_animal_por_codigo(codigo_selecionado)
        os.system("cls")
        if isinstance(animal, Animal):
            self.__animal_DAO.remove(animal.codigo)
            self.__tela_animal.mensagem("Animal removido com sucesso!")
        else:
            self.__tela_animal.mensagem("Animal inexistente no sistema.")
        print()

    def listar_animais(self):
        if len(self.__animal_DAO.get_all()) != 0:
            self.__tela_animal.mensagem(
                "Lista de animais (código, nome, tipo, raça, tamanho):"
                )
            for animal in self.__animal_DAO.get_all():
                self.__tela_animal.mostra_animal(animal)
        else:
            self.__tela_animal.mensagem("Ainda não há animais no sistema.\n")

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_animal,
            2: self.alterar_animal,
            3: self.excluir_animal,
            4: self.listar_animais,
            0: "Retornar para menu principal",
        }

        while True:
            opcao = self.__tela_animal.abre_tela()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()
