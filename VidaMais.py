from itertools import tee
import os

class Menu:
    def __init__(self):
        self.controle = True

        self.opcoes = {
            "1": self.cadastrar,
            "2": self.estatisticas,
            "3": self.buscar,
            "4": self.listar,
            "5": self.gerenciar_fila,
            "6": self.sair,
        }

    def cadastrar(self):
        self.limpar()
        loopNome = True
        while loopNome:
            nome = input("Digite o nome do novo paciente: ")
            if nome.strip() == "" or any(char.isdigit() for char in nome):
                self.limpar()
                print("Nome invalido. Tente novamente.\n")
            else:
                loopNome = False

        self.limpar()
        loopIdade = True
        while loopIdade:
            idade = input("Digite a idade do novo paciente: ")
            if not idade.isdigit() or int(idade) <= 0:
                self.limpar()
                print("Idade invalida. Tente novamente.\n")
            else:
                loopIdade = False

        self.limpar()
        loopTelefone = True
        while loopTelefone:
            telefone = input("Digite o telefone do novo paciente (somente numeros): ")
            if not telefone.isdigit() or len(telefone) < 8 or len(telefone) > 15:
                self.limpar()
                print("Telefone invalido. Tente novamente.\n")
            else:
                loopTelefone = False

        self.limpar()
        loopCPF = True
        while loopCPF:
            cpf = input("Digite o CPF do novo paciente (somente numeros): ")
            if not cpf.isdigit() or len(cpf) != 11:
                self.limpar()
                print("CPF invalido. Tente novamente.\n")
            else:
                loopCPF = False

        self.limpar()
        loopRG = True
        while loopRG:
            rg = input("Digite o RG do novo paciente (somente numeros): ")
            if not rg.isdigit() or len(rg) < 7 or len(rg) > 9:
                self.limpar()
                print("RG invalido. Tente novamente.\n")
            else:
                loopRG = False

        self.limpar()
        print("Paciente cadastrado com sucesso!")
        self.read_key()
        self.limpar()

    def estatisticas(self):
        self.limpar()
        print("estatistica")
        self.read_key()
        self.limpar()

    def buscar(self):
        self.limpar()
        print("busca")
        self.read_key()
        self.limpar()

    def listar(self):
        self.limpar()
        print("lista")
        self.read_key()
        self.limpar()

    def gerenciar_fila(self):
        self.limpar()
        print("fila")
        self.read_key()
        self.limpar()

    def sair(self):
        print("Obrigado por utilizar o Sistema Vida Mais!")
        self.controle = False

    def limpar(self):
        os.system('cls')

    def read_key(self):
        input("\nPressione ENTER para voltar ao menu...")

    def executar(self):
        while self.controle:
            print("Bem-vindo ao Sistema Vida Mais!\n")

            print("1 - Cadastrar paciente;\n2 - Ver estatisticas;\n3 - Buscar paciente;\n" 
                  "4 - Listar todos os pacientes;\n5 - Gerenciar filas de atendimento;\n"
                  "6 - Sair.\n")

            opcao = input("Digite a opcao desejada: ")
            acao = self.opcoes.get(opcao)

            if acao:
                acao()

            else:
                self.limpar()
                print("\nOpcao invalida. Tente novamente.\n")

menu = Menu()
menu.executar()