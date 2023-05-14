from entidades.animal import Animal
from telas.tela_animal import TelaAnimal
import os


class ControladorAnimal:
    def __init__(self, controlador_sistema):
        self.__animais = []
        self.__id = 0
        self.__tela_animal = TelaAnimal()
        self.__controlador_sistema = controlador_sistema

    def pegar_animal_por_codigo(self, codigo_animal):
        for animal in self.__animais:
            if int(animal.codigo) == int(codigo_animal):
                return animal
        return None

    def incluir_animal(self):
        self.__id += 1
        self.__tela_animal.mensagem("Cadastro de animal.")
        dados_animal = self.__tela_animal.pega_dados_animal()
        animal = Animal(self.__id, dados_animal["nome"],
                        dados_animal["tipo"], dados_animal["raca"],
                        dados_animal["tamanho"])
        self.__animais.append(animal)
        os.system('cls')
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
            os.system('cls')
            self.__tela_animal.mensagem("Alteração realizada com sucesso!")
        else:
            os.system('cls')
            self.__tela_animal.mensagem("Animal inexistente no sistema.")
        print()

    def excluir_animal(self):
        self.__tela_animal.mensagem("Exclusão de animal do sistema.")
        codigo_selecionado = self.__tela_animal.seleciona_codigo_animal()
        animal = self.pegar_animal_por_codigo(codigo_selecionado)
        os.system('cls')
        if isinstance(animal, Animal):
            self.__animais.remove(animal)
            self.__tela_animal.mensagem("Animal removido com sucesso!")
        else:
            self.__tela_animal.mensagem("Animal inexistente no sistema.")
        print()

    def listar_animais(self):
        if len(self.__animais) != 0:
            self.__tela_animal.mensagem("Lista de animais:")
            for animal in self.__animais:
                self.__tela_animal.mostra_animal(animal)
        else:
            self.__tela_animal.mensagem(
                "Ainda não há animais no sistema. Voce deve cadastrar primeiro!")
            self.__controlador_sistema.abre_tela()
        print()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_animal, 2: self.alterar_animal,
                        3: self.excluir_animal, 4: self.listar_animais,
                        0: "Retornar para menu principal"}

        while True:
            opcao = self.__tela_animal.abre_tela()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()

    # def listar_animais_adocao(self):
    #     if len(self.__animais) != 0:
    #         self.__tela_animal.mensagem("Lista de animais disponíveis para adoção:")
    #         for animal in self.__animais:
    #             if animal.foi_adotado==False and animal.pode_ser_adotado==True:
    #                 self.__tela_animal.mostra_animal(animal)
    #     else:
    #         self.__tela_animal.mensagem(
    #             "Não há animais disponíveis no sistema. Voce deve cadastrar primeiro!")
    #         self.__controlador_sistema.abre_tela()
    #     print()