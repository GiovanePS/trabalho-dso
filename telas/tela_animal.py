import os
from exceptions.valor_invalido_exception import ValorInvalido


class TelaAnimal:
    def abre_tela(self):
        os.system('cls')
        print("Animais: ")
        print("Escolha uma opção:")
        print("[1] Cadastrar animal.")
        print("[0] Retornar para o menu principal.")
        opcao = int(input("Opção: "))
        return opcao

    def cadastro_animal():
        os.system('cls')
        print("Cadastro de animais:")
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
            except (ValorInvalido, TypeError):
                print("Digite uma das opções!")

        raca = input("\tRaça do animal: ")
        if opcao_tipo == 1:
            tamanho = input("\tTamanho do animal: ")
        else:
            tamanho = "Sem tamanho."

        return {"nome": nome, "tipo": tipos[opcao_tipo],
                "Raça": raca, "tamanho": tamanho}

    def mostra_animal(self, animal):
        print(f"{animal.codigo} - {animal.nome}, {animal.tipo}", end=' ')
        if animal.tipo == "Cachorro":
            print(f"de porte {animal.tamanho}.")
