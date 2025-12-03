import os

class Paciente:
    def __init__(self, nome, idade, telefone, cpf, rg, tipo_atendimento, agendamento, documentos, pagamento):
        self.nome = nome
        self.idade = int(idade)
        self.telefone = telefone
        self.cpf = cpf
        self.rg = rg
        self.tipo_atendimento = tipo_atendimento
        self.agendamento = agendamento
        self.documentos = documentos
        self.pagamento = pagamento

class Menu:
    def __init__(self):
        self.controle = True
        self.pacientes = []
        self.fila = []

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
                print("Nome invalido. Tente novamente.")
                self.read_key()
                self.limpar()
            else:
                loopNome = False

        self.limpar()
        loopIdade = True
        while loopIdade:
            idade = input("Digite a idade do novo paciente: ")
            if not idade.isdigit() or int(idade) <= 0:
                self.limpar()
                print("Idade invalida. Tente novamente.")
                self.read_key()
                self.limpar()
            else:
                loopIdade = False

        self.limpar()
        loopTelefone = True
        while loopTelefone:
            telefone = input("Digite o telefone do novo paciente (somente numeros): ")
            if not telefone.isdigit() or len(telefone) < 8 or len(telefone) > 15:
                self.limpar()
                print("Telefone invalido. Tente novamente.")
                self.read_key()
                self.limpar()
            else:
                loopTelefone = False

        self.limpar()
        loopCPF = True
        while loopCPF:
            cpf = input("Digite o CPF do novo paciente (somente numeros): ")
            if not cpf.isdigit() or len(cpf) != 11:
                self.limpar()
                print("CPF invalido. Tente novamente.")
                self.read_key()
                self.limpar()
            else:
                loopCPF = False

        self.limpar()
        loopRG = True
        while loopRG:
            rg = input("Digite o RG do novo paciente (somente numeros): ")
            if not rg.isdigit() or len(rg) < 7 or len(rg) > 9:
                self.limpar()
                print("RG invalido. Tente novamente.")
                self.read_key()
                self.limpar()
            else:
                loopRG = False

        self.limpar()
        loopAtendimento = True
        while loopAtendimento:
            atendimento = input("Digite se o atendimento eh normal ou prioritario: ")
            if atendimento.lower() not in ["normal", "prioritario"]:
                self.limpar()
                print("Opcao invalida. Tente novamente.")
                self.read_key()
                self.limpar()
            else:
                loopAtendimento = False

        self.limpar()
        loopAgendamento = True
        while loopAgendamento:
            agendamento = input("O paciente possui agendamento? (s/n): ")
            if agendamento.lower() not in ["s", "n"]:
                self.limpar()
                print("Opcao invalida. Tente novamente.")
                self.read_key()
                self.limpar()
            else:
                loopAgendamento = False

        self.limpar()
        loopDocumentos = True
        while loopDocumentos:
            documentos = input("O paciente possui todos os documentos em dia? (s/n): ")
            if documentos.lower() not in ["s", "n"]:
                self.limpar()
                print("Opcao invalida. Tente novamente.")
                self.read_key()
                self.limpar()
            else:
                loopDocumentos = False

        self.limpar()
        loopPagamento = True
        while loopPagamento:
            pagamento = input("O paciente esta com o pagamento em dia? (s/n): ")
            if pagamento.lower() not in ["s", "n"]:
                self.limpar()
                print("Opcao invalida. Tente novamente.")
                self.read_key()
                self.limpar()
            else:
                loopPagamento = False

        self.limpar()
        print("Paciente cadastrado com sucesso!")
        self.read_key()
        self.limpar()

        paciente = Paciente(nome, idade, telefone, cpf, rg, atendimento, agendamento, documentos, pagamento)
        self.pacientes.append(paciente)

    def estatisticas(self):
        self.limpar()

        if not self.pacientes:
            print("Nenhum paciente cadastrado!")
            self.read_key()
            self.limpar()
            return
        else:
            print("Estatisticas dos pacientes cadastrados:\n")

            total_pacientes = len(self.pacientes)
            idades = [int(p.idade) for p in self.pacientes]
            idade_media = sum(idades) / total_pacientes
            paciente_mais_novo = min(self.pacientes, key=lambda p: p.idade)
            paciente_mais_velho = max(self.pacientes, key=lambda p: p.idade)

            print(f"Total de pacientes cadastrados: {total_pacientes}")
            print(f"Idade media dos pacientes: {idade_media:.2f} anos")
            print(f"Paciente mais novo: {paciente_mais_novo.nome} ({paciente_mais_novo.idade} anos)")
            print(f"Paciente mais velho: {paciente_mais_velho.nome} ({paciente_mais_velho.idade} anos)")

        self.read_key()
        self.limpar()

    def buscar(self):
        self.limpar()

        if not self.pacientes:
            print("Nenhum paciente cadastrado!")
            self.read_key()
            self.limpar()
            return

        nome = input("Digite o nome do paciente que deseja buscar: ").strip().lower()

        encontrados = [p for p in self.pacientes if nome in p.nome.lower()]

        self.limpar()

        if encontrados:
            print("Pacientes encontrados:\n")
            for paciente in encontrados:
                print(f"Nome: {paciente.nome}, Idade: {paciente.idade}, "
                      f"Telefone: {paciente.telefone}, CPF: {paciente.cpf}, "
                      f"RG: {paciente.rg}")
        else:
            print("Nenhum paciente encontrado com esse nome.")

        self.read_key()
        self.limpar()

    def listar(self):
        self.limpar()

        if not self.pacientes:
            print("Nenhum paciente cadastrado!")
        else:
            print("Lista de pacientes cadastrados:\n")
            for i, paciente in enumerate(self.pacientes, start=1):
                print(
                    f"{i}. Nome: {paciente.nome}, Idade: {paciente.idade}, "
                    f"Telefone: {paciente.telefone}, CPF: {paciente.cpf}, RG: {paciente.rg}"
                )

        self.read_key()
        self.limpar()

    def gerenciar_fila(self):
        loopFila = True
        while loopFila:

            self.limpar()
            print("Gerenciamento de filas de atendimento:\n")
            print("1 - Adicionar paciente na fila;\n2 - Atender proximo paciente;"
            "\n3 - Listar fila de pacientes;\n4 - Voltar ao menu principal.\n")

            opcao = input("Digite a opcao desejada: ")

            if opcao == "1":
                self.limpar()
                print("Adicionar paciente a fila\n")

                medico = input("Ha um medico para atendimento? (s/n): ")        
                if medico.lower() != "s":
                    self.limpar()
                    print("Paciente nao pode ser atendido.")
                    self.read_key()
                    self.limpar()
                    continue

                medico_disponivel = True
                
                self.limpar()
                nome = input("Digite o nome do paciente: ").strip().lower()
                cpf = input("Digite o CPF do paciente: ").strip()

                if nome.strip() == "" or any(char.isdigit() for char in nome):
                    self.limpar()
                    print("Nome invalido!")
                    self.read_key()
                    self.limpar()
                    continue

                if not cpf.isdigit() or len(cpf) != 11:
                    self.limpar()
                    print("CPF invalido!")
                    self.read_key()
                    self.limpar()
                    continue

                paciente = next(
                    (p for p in self.pacientes if p.cpf == cpf and p.nome.lower() == nome),
                    None
                )

                if paciente is None:
                    self.limpar()
                    print("Paciente nao encontrado na base de dados!")
                    self.read_key()
                    self.limpar()
                    continue

                elif any(f["cpf"] == cpf for f in self.fila):
                    print("\nPaciente ja esta na fila!")
                    self.read_key()
                    self.limpar()
                    continue

                pode_atender = False

                if paciente.tipo_atendimento == "normal":
                    regra1 = (paciente.agendamento == "s" and paciente.documentos == "s" and medico_disponivel)
                    regra2 = (paciente.documentos == "s" and paciente.pagamento == "s" and medico_disponivel)

                    if regra1 or regra2:
                        pode_atender = True

                if paciente.tipo_atendimento == "prioritario":

                    if medico_disponivel and (paciente.documentos == "s" or paciente.pagamento == "s"):
                        pode_atender = True

                if not pode_atender:
                    self.limpar()
                    print("Paciente nao pode ser adicionado a fila devido a pendencias.")
                    self.read_key()
                    self.limpar()
                    continue

                else:
                    self.fila.append({"nome": paciente.nome, "cpf": paciente.cpf})
                    self.limpar()
                    print(f"Paciente {paciente.nome} adicionado a fila com sucesso!")
                    self.read_key()
                    self.limpar()

            elif opcao == "2":
                if not self.fila:
                    self.limpar()
                    print("A fila esta vazia.")
                    self.read_key()
                    self.limpar()
                    continue

                self.limpar()
                print("Chamando proximo paciente...\n")
                proximo = self.fila.pop(0)

                print(f"Paciente {proximo['nome']} (CPF: {proximo['cpf']}) atendido com sucesso!")

                self.read_key()
                self.limpar()

            elif opcao == "3":
                self.limpar()
                print("Fila de Atendimento:\n")

                if not self.fila:
                    print("A fila esta vazia.")
                    self.read_key()
                    self.limpar()
                else:
                    for i, p in enumerate(self.fila, start=1):
                        print(f"{i}. Nome: {p['nome']} | CPF: {p['cpf']}")

                    self.read_key()

            elif opcao == "4":
                loopFila = False
                self.limpar()

            else:
                self.limpar()
                print("Opcao invalida!")
                self.read_key()
                self.limpar()

    def sair(self):
        self.limpar()
        print("Obrigado por utilizar o Sistema Vida Mais!\n")
        self.controle = False

    def limpar(self):
        os.system('cls')

    def read_key(self):
        input("\nPressione ENTER para voltar ao menu...")

    def executar(self):
        while self.controle:
            self.limpar()
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
                print("Opcao invalida. Tente novamente.")
                self.read_key()
                self.limpar()

menu = Menu()
menu.executar()