from telas.tela_adocao import TelaAdocao
from entidades.adocao import Adocao
import os


class ControladorAdocao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema=controlador_sistema
        self.__adocoes = []
        self.__tela_adocao = TelaAdocao()
        self.__id=0
    
    def pega_adocao_por_id(self, id):
        for adocao in self.__adocoes:
            if int(adocao.id_adocao)==int(id):
                return adocao
        return None

    def incluir_adocao(self):
        self.__controlador_sistema.controlador_adotante.listar_adotantes()
        self.__controlador_sistema.controlador_animal.listar_animais()
        dados_adocao=self.__tela_adocao.pega_dados_adocao()


        adotante = self.__controlador_sistema.controlador_adotante.pega_adotante_por_cpf(dados_adocao["cpf_adotante"])
        animal = self.__controlador_sistema.controlador_animal.pegar_animal_por_codigo(dados_adocao["codigo_animal_adotado"])

        if (adotante is not None and animal is not None):
            self.__id+=1
            adocao=Adocao(dados_adocao["data_adocao"], animal, adotante, dados_adocao["assinatura"], self.__id )
            self.__adocoes.append(adocao)
            os.system('cls') 
            print("Adoção cadastrada com sucesso!")           
        else:
            self.__tela_adocao.mostra_mensagem("Dados inválidos!")

    def alterar_adocao(self):
        self.listar_adocoes()
        id_adocao= self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_id(id_adocao)

        if (adocao is not None):
            novos_dados_adocao = self.__tela_adocao.pega_dados_adocao()
            adocao.data_adocao = novos_dados_adocao["data_adocao"]
            # adocao.animal_adotado.nome = novos_dados_adocao["nome_animal"]
            adocao.animal_adotado.codigo = novos_dados_adocao["codigo_animal"]
            # adocao.adotante.nome = novos_dados_adocao["nome_adotante"]
            adocao.adotante.cpf = novos_dados_adocao["cpf_adotante"]
            adocao.assinatura = novos_dados_adocao["assinatura"]
            self.listar_adocoes()
        
        else:
            self.__tela_adocao.mostra_mensagem("Essa adoção NÃO EXISTE!")

    def excluir_adocao(self):
        self.listar_adocoes()
        id_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_id(id_adocao)

        if (adocao is not None):
            self.__adocoes.remove(adocao)
            os.system('cls') 
            self.__tela_adocao.mostra_mensagem("Adoção removida com sucesso!")
        else:
            self.__tela_adocao.mostra_mensagem("Esta adoção NÃO EXISTE.")

    def listar_adocoes(self):
        if len(self.__adocoes)==0:
            print("Não há nenhuma adoção cadastrada!")
            self.__controlador_sistema.menu_doacao()
        else:
            print('Adoções:')
            print()
            for adocao in self.__adocoes:
                self.__tela_adocao.mostra_adocao({"codigo_adocao": adocao.id_adocao, 
                                                    "data_adocao": adocao.data_adocao, 
                                                    "nome_animal":adocao.animal_adotado.nome, 
                                                    "codigo_animal":adocao.animal_adotado.codigo, 
                                                    "nome_adotante":adocao.adotante.nome, 
                                                    "cpf_adotante":adocao.adotante.cpf, 
                                                    "assinatura": adocao.assinatura})
                print()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_adocao, 2: self.alterar_adocao,
                        3: self.excluir_adocao, 4: self.listar_adocoes,
                        0: "Retornar para menu principal"}
        while True:
            opcao = self.__tela_adocao.tela_opcoes()
            if opcao == 0:
                return
            funcao_escolhida = lista_opcoes[opcao]
            funcao_escolhida()