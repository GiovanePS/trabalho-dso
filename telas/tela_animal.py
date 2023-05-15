import os
from exceptions.valor_invalido_exception import ValorInvalido
from entidades.animal import Animal


class TelaAnimal:
    def abre_tela(self):
        print("Escolha uma opção:")
        print("[1] Cadastrar animal.")
        print("[2] Alterar animal.")
        print("[3] Excluir animal.")
        print("[4] Listar animais.")
        print("[0] Retornar para o menu principal.")
        while True:
            try:
                opcao_escolhida = int(input("Opção: "))
                if 0 < opcao_escolhida > 4:
                    raise ValorInvalido
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite uma das opções.")
            else:
                break
        os.system("cls")
        return opcao_escolhida

    def pega_dados_animal(self):
        nome = input("  Nome do animal: ")

        tipos = {1: "Cachorro", 2: "Gato"}
        while True:
            print("  [1] Cachorro.")
            print("  [2] Gato.")
            try:
                opcao_tipo = int(input("  Opção: "))
                if 1 < opcao_tipo > 2:
                    raise ValorInvalido
                else:
                    break
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite uma das opções.")

        raca = input("  Raça do animal: ")
        if opcao_tipo == 1:
            tamanhos = {1: "Pequeno", 2: "Médio", 3: "Grande"}
            while True:
                print("  Tamanho do animal: ")
                print("  [1] Pequeno.")
                print("  [2] Médio.")
                print("  [3] Grande.")
                try:
                    opcao_tamanho = int(input("  Opção: "))
                    if 1 < opcao_tamanho > 3:
                        raise ValorInvalido
                except (ValorInvalido, ValueError):
                    print("Valor inválido! Digite uma das opções.")
                else:
                    break
            tamanho = tamanhos[opcao_tamanho]
        else:
            tamanho = None

        return {
            "nome": nome,
            "tipo": tipos[opcao_tipo],
            "raca": raca,
            "tamanho": tamanho,
        }

    def mostra_animal(self, animal: Animal):
        print(
            f"{animal.codigo} - {animal.nome}, "
            f"{animal.tipo}, {animal.raca}", end=""
        )

        print(f", {animal.tamanho}.") if animal.tipo == "Cachorro" else print(".")

        print("  Vacinas: ", end="")
        if len(animal.vacinas) > 0:
            vacinas = ", ".join(animal.vacinas)
            print(f"{vacinas}.")
        else:
            print("nenhuma vacina cadastrada.")
        print()

    def seleciona_codigo_animal(self):
        while True:
            try:
                codigo_selecionado = int(input("Digite o código do animal: "))
            except ValueError:
                print("Valor inválido! Digite um valor inteiro válido.")
            else:
                break
        return codigo_selecionado

    def mensagem(self, mensagem: str):
        print(mensagem)
