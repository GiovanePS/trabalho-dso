from entidades.animal import Animal
from telas.tela_animal import TelaAnimal


class ControladorAnimal:
    def __init__(self):
        self.__animais = []
        self.__id = 0
        self.__tela_animal = TelaAnimal()

    def pegar_animal_por_codigo(self, codigo):
        for animal in self.__animais:
            if animal.codigo == codigo:
                return animal
        return None

    def incluir_animal(self):
        self.__id += 1
        self.__tela_animal.mensagem("Cadastro de animal:")
        dados_animal = self.__tela_animal.pega_dados_animal()
        animal = Animal(self.__id, dados_animal["nome"],
                        dados_animal["tipo"], dados_animal["raca"],
                        dados_animal["tamanho"])
        self.__animais.append(animal)
        self.__tela_animal.mensagem("Animal cadastrado com sucesso.")

    def alterar_animal(self):
        self.__tela_animal.mensagem("Alteração cadastral de animal.")
        codigo_selecionado = self.__tela_animal.seleciona_animal()
        animal = self.pegar_animal_por_codigo(codigo_selecionado)
        if isinstance(animal, Animal):
            novos_dados_animal = self.__tela_animal.pega_dados_animal()
            animal.nome = novos_dados_animal["nome"]
            animal.tipo = novos_dados_animal["tipo"]
            animal.raca = novos_dados_animal["raca"]
            animal.tamanho = novos_dados_animal["tamanho"]
            self.__tela_animal.mensagem("Alteração realizada com sucesso!")
        else:
            self.__tela_animal.mensagem("Animal inexistente no sistema.")

    def excluir_animal(self):
        ...

    def listar_animais(self):
        for animal in self.__animais:
            self.__tela_animal.mostra_animal(animal)
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
