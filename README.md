# Sistema Vida Mais 🏥

Sistema de gerenciamento de pacientes e filas de atendimento, desenvolvido em **Python** e executado diretamente no terminal. O projeto permite cadastrar e consultar pacientes, visualizar estatísticas e organizar uma fila de atendimento com base em regras de elegibilidade.

## Objetivo

Simular atividades básicas de recepção e organização de atendimentos em uma unidade de saúde, aplicando conceitos de **programação orientada a objetos**, **validação de entradas**, **estruturas de dados** e **lógica condicional**.

## Tecnologias utilizadas

- **Python 3**
- Biblioteca padrão `os` (para limpeza do terminal)

O código não utiliza bibliotecas externas nem exige instalação de pacotes adicionais.

## Funcionalidades

### Cadastro de pacientes

Permite registrar:

- Nome;
- Idade;
- Telefone;
- CPF e RG;
- Tipo de atendimento (`normal` ou `prioritario`);
- Existência de agendamento (`s` ou `n`);
- Regularidade dos documentos (`s` ou `n`);
- Situação do pagamento (`s` ou `n`).

O cadastro valida entradas obrigatórias e formatos básicos: nome não vazio e sem números, idade positiva, telefone com 8 a 15 dígitos, CPF com 11 dígitos, RG com 7 a 9 dígitos e respostas limitadas às opções previstas.

> **Observação:** as verificações de CPF e RG são apenas de formato; não há validação de dígitos verificadores, autenticidade ou duplicidade de cadastro.

### Estatísticas

Exibe:

- Quantidade total de pacientes cadastrados;
- Idade média dos pacientes;
- Paciente mais novo;
- Paciente mais velho.

### Busca e listagem

- Busca pacientes por nome ou parte do nome, sem diferenciar maiúsculas e minúsculas;
- Lista todos os pacientes cadastrados, apresentando nome, idade, telefone, CPF e RG.

### Gerenciamento de fila

Permite:

1. Adicionar um paciente previamente cadastrado à fila;
2. Atender o próximo paciente;
3. Visualizar a fila atual;
4. Retornar ao menu principal.

Para entrar na fila, o paciente deve ser identificado por **nome e CPF**, haver confirmação de médico disponível e as regras de atendimento devem ser satisfeitas. O sistema também impede que o mesmo CPF seja adicionado duas vezes à fila simultaneamente.

## Regras de atendimento

A entrada na fila depende do tipo de atendimento cadastrado:

| Tipo | Condições para inclusão na fila |
| --- | --- |
| **Normal** | Médico disponível **e** documentos em dia **e** (agendamento confirmado **ou** pagamento em dia). |
| **Prioritário** | Médico disponível **e** (documentos em dia **ou** pagamento em dia). |

Se o paciente não atender às condições, o sistema informa que não pode incluí-lo na fila por pendências.

**Importante:** o atendimento prioritário possui regras próprias de elegibilidade, mas **não altera a posição do paciente na fila**. A ordem utilizada é FIFO (*First In, First Out*): o primeiro paciente adicionado é o primeiro chamado.

## Como executar

### Pré-requisitos

- Python 3 instalado;
- Terminal ou prompt de comando.

### Passo a passo

1. Salve o código Python em um arquivo, por exemplo `main.py`.
2. Abra o terminal na pasta onde o arquivo está salvo.
3. Execute:

```bash
python main.py
```

Em ambientes que utilizam o comando `python3`:

```bash
python3 main.py
```

> O comando de limpeza de tela do projeto é `cls`, utilizado no Windows. Para executar com a limpeza correta em Linux ou macOS, adapte o método `limpar()` para utilizar `clear` nesses sistemas.

## Menu principal

```text
Bem-vindo ao Sistema Vida Mais!

1 - Cadastrar paciente;
2 - Ver estatisticas;
3 - Buscar paciente;
4 - Listar todos os pacientes;
5 - Gerenciar filas de atendimento;
6 - Sair.

Digite a opcao desejada:
```

### Exemplo de utilização

1. Selecione `1` para cadastrar um paciente e informe os dados solicitados.
2. Selecione `4` para conferir os cadastros ou `2` para visualizar as estatísticas.
3. Selecione `5` para acessar o gerenciamento da fila.
4. Escolha `1`, confirme a disponibilidade de médico e informe o nome e o CPF de um paciente cadastrado.
5. Se as condições forem atendidas, o paciente será incluído na fila.
6. Escolha `3` para consultar a ordem da fila ou `2` para chamar o próximo paciente.

## Organização do código

O projeto enviado reúne a implementação em um único script Python, organizado em duas classes principais:

| Componente | Responsabilidade |
| --- | --- |
| `Paciente` | Representa um paciente e armazena seus dados cadastrais e de atendimento. |
| `Menu` | Controla a interface no terminal, os cadastros, as consultas, as estatísticas e a fila. |

Métodos relevantes da classe `Menu`:

- `cadastrar()` — coleta e valida os dados de um novo paciente;
- `estatisticas()` — calcula indicadores básicos;
- `buscar()` — pesquisa pacientes por nome;
- `listar()` — apresenta os pacientes cadastrados;
- `gerenciar_fila()` — adiciona, chama e lista pacientes da fila;
- `limpar()` e `read_key()` — oferecem funções auxiliares de interação no terminal;
- `sair()` — encerra o sistema;
- `executar()` — mantém o menu principal em funcionamento.

Os pacientes ficam armazenados na lista `self.pacientes`. A fila de atendimento é mantida na lista `self.fila`, com nome e CPF de cada paciente incluído.
