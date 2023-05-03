import os
from exceptions.valor_invalido_exception import ValorInvalido
from entidades.animal import Animal


class TelaAnimal:
    def abre_tela(self):
        print("Animais: ")
        print("Escolha uma opção:")
        print("[1] Cadastrar animal.")
        print("[2] Alterar animal.")
        print("[3] Excluir animal.")
        print("[4] Listar animais.")
        print("[0] Retornar para o menu principal.")
        opcao = int(input("Opção: "))
        os.system('cls')
        return opcao

    def pega_dados_animal(self):
        nome = input("  Nome do animal: ")

        tipos = {1: "Cachorro", 2: "Gato"}
        while True:
            print("  [1] Cachorro.")
            print("  [2] Gato.")
            try:
                opcao_tipo = int(input("  Opção: "))
                if opcao_tipo != 1 and opcao_tipo != 2:
                    raise ValorInvalido
                else:
                    break
            except (ValorInvalido, ValueError):
                print("Digite uma das opções!")

        raca = input("  Raça do animal: ")
        if opcao_tipo == 1:
            tamanho = input("  Tamanho do animal: ")
        else:
            tamanho = None

        os.system('cls')
        return {"nome": nome, "tipo": tipos[opcao_tipo],
                "raca": raca, "tamanho": tamanho}

    def mostra_animal(self, animal: Animal):
        print(f"{animal.codigo} - {animal.nome}, {animal.tipo}", end='')
        print(f", {animal.tamanho}.") if animal.tipo == "Cachorro" \
            else print(".")

    def seleciona_animal(self):
        while True:
            try:
                codigo_selecionado = int(input("Digite o código do animal: "))
            except ValueError:
                print("Digite um valor inteiro válido.")
            else:
                break
        return codigo_selecionado

    def mensagem(self, mensagem: str):
        print(mensagem)
