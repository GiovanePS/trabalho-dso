from entidades.animal import Animal
from telas.tela_animal import TelaAnimal
from DAOs.animal_dao import AnimalDAO


class ControladorAnimal:
    def __init__(self, controlador_sistema):
        self.__animal_DAO = AnimalDAO()
        self.__codigo = 0
        self.__tela_animal = TelaAnimal()
        self.__controlador_sistema = controlador_sistema

    @property
    def animais(self):
        return self.__animal_DAO.get_all()

    @property
    def animal_DAO(self):
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
        dados_animal = self.__tela_animal.pega_dados_animal()
        if dados_animal == None:
            return

        try:
            self.__codigo = int(list(self.__animal_DAO.get_all())[-1].codigo) + 1
        except IndexError:
            self.__codigo = 1
        animal = Animal(
            self.__codigo,
            dados_animal["nome"],
            dados_animal["tipo"],
            dados_animal["raca"],
            dados_animal["tamanho"],
        )
        self.__animal_DAO.add(animal)
        return animal.codigo

    def alterar_animal(self):
        if len(self.__animal_DAO.get_all()) != 0:
            codigo_selecionado = self.__tela_animal.seleciona_codigo_animal()
            animal = self.pegar_animal_por_codigo(codigo_selecionado)
            if isinstance(animal, Animal):
                novos_dados_animal = self.__tela_animal.pega_dados_animal()
                if novos_dados_animal == None:
                    self.__tela_animal.mensagem("Animal não alterado.")
                    return
                animal.nome = novos_dados_animal["nome"]
                animal.tipo = novos_dados_animal["tipo"]
                animal.raca = novos_dados_animal["raca"]
                animal.tamanho = novos_dados_animal["tamanho"]
                self.__animal_DAO.update(animal)
                self.__tela_animal.mensagem("Animal alterado com sucesso!")
            else:
                self.__tela_animal.mensagem("Animal inexistente no sistema.")
        else:
            self.__tela_animal.mensagem("Ainda não há animais no sistema.")

    def excluir_animal(self):
        if len(self.__animal_DAO.get_all()) != 0:
            codigo_selecionado = self.__tela_animal.seleciona_codigo_animal()
            animal = self.pegar_animal_por_codigo(codigo_selecionado)
            if isinstance(animal, Animal):
                self.__animal_DAO.remove(animal.codigo)
                self.__tela_animal.mensagem("Animal removido com sucesso!")
            else:
                self.__tela_animal.mensagem("Animal inexistente no sistema.")
        else:
            self.__tela_animal.mensagem("Ainda não há animais no sistema.")

    def listar_animais(self):
        if len(self.__animal_DAO.get_all()) != 0:
            dados_animais = []
            for animal in self.__animal_DAO.get_all():
                dados_animais.append({
                    "codigo": animal.codigo,
                    "nome": animal.nome,
                    "tipo": animal.tipo,
                    "raca": animal.raca,
                    "tamanho": animal.tamanho,
                    "vacinas": animal.vacinas,
                    "pode_ser_adotado": animal.pode_ser_adotado,
                    "foi_adotado": animal.foi_adotado
                })

            self.__tela_animal.mostra_animal(dados_animais)
        else:
            self.__tela_animal.mensagem("Ainda não há animais no sistema.")

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
