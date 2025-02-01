import json

# Nome do arquivo JSON utilizado pelo programa
NomeDoArquivo = 'arquivo.json'


 # ------------------------------------------------------------------
def LerArquivo(nome):

    '''
    Realiza a leitura de um arquivo JSON e retorna os dados encontrados
        nome -> Nome do arquivo a ser aberto e lido
    '''

    try:
        with open(nome, 'r') as file:
            informacao = json.loads(file.read())
        return informacao
    except:
        return None


# ---------------------------------------------------------------------
def EscreverArquivo(nome, dados):
    
    '''
    Cria um arquivo JSON com o modelo de dados informado ou sobescreve os dados de um arquivo
    JSON já criado
        nome -> Nome do arquivo a ser criado ou sobescrito
        dados -> Toda a informação a ser armazenada
    '''

    try:
        with open(nome, 'w') as file:
            file.write(json.dumps(dados))
    except:
        return None


# --------------------------------------------------------------------
def CriarConjunto():
    
    '''
    No arquivo JSON utilizado pelo programa, cria um novo conjunto em um dicionário
    '''

    dado = LerArquivo(NomeDoArquivo)
    while True:
        nome = input('Digite o nome do conjunto (-v:voltar) ').strip()
        if nome == '-v':
            return None
        
        confirmacao = ''
        if len(nome) > 0:

            if nome not in dado.keys():
                while confirmacao.lower() != 's' and confirmacao.lower() != 'n':
                    confirmacao = input(f'O nome sera {nome}, confirmar? (s/n) ').strip()
                    if confirmacao.lower() != 's' and confirmacao.lower() != 'n':
                        print('Por favor, digite apenas S para sim ou N para não')

                    elif confirmacao.lower() == 's':
                        dado[nome] = {
                            'items' : []
                        }

                        EscreverArquivo(NomeDoArquivo, dado)
                        print('Confirmado, conjunto criado!')
                        return None

            else:
                print('Este nome já foi usado')

        else:
            print('Não pode conter apenas espaços vazios')


# ------------------------------------------------------------------------------
def AdicionarItem(Nome):
    
    '''
    Adiciona items em conjunto informado pelo usuário que esta armazenado no arquivo JSON utilizado pelo programa
    '''

    dado = LerArquivo(NomeDoArquivo)

    items = dado[Nome]['items']

    while True:
        NomeDoItem = input('Digite o item a ser adicionado (-v:voltar) ').strip()
        if NomeDoItem == '-v':
            return None
        
        confirmacao = ''
        if len(NomeDoItem) > 0:
            if NomeDoItem not in items:
                while confirmacao.lower() != 's' and confirmacao.lower() != 'n':
                    confirmacao = input(f'Adicionar o item {NomeDoItem} no conjunto {Nome}, confirmar? (s/n) ').strip()
                    if confirmacao.lower() != 's' and confirmacao.lower() != 'n':
                        print('Por favor, digite apenas S para sim ou N para não')

                    elif confirmacao.lower() == 's':
                        dado[Nome]['items'].append(NomeDoItem)
                        EscreverArquivo(NomeDoArquivo, dado)
                        print('Item adicionado, cofirmado!')
                        return None
            else:
                print('Este item já foi usado, não pode haver repetição')
        else:
            print('Não pode conter apenas espaços vazios')


# -----------------------------------------------------------------------------
def EditarItem(Nome):
    dado = LerArquivo(NomeDoArquivo)

    items = dado[Nome]['items']

    while True:
        NomeDoItem = input('Digite o item a ser editado (-v:voltar) ').strip()

        if NomeDoItem == '-v':
            return None
        
        confirmacao = ''
        if len(NomeDoItem) > 0:
            if NomeDoItem in items:
                while True:
                    NovoNomeDoItem = input('Digite o novo valor do item (-v:voltar) ').strip()
                    if NovoNomeDoItem == '-v':
                        return None
                    
                    
                    if len(NovoNomeDoItem) > 0:
                        if NovoNomeDoItem not in items:
                            
                            while confirmacao.lower() != 's' and confirmacao.lower() != 'n':
                                confirmacao = input(f'Mudar de {NomeDoItem} para {NovoNomeDoItem}, confirmar? (s/n) ').strip()
                                if confirmacao.lower() != 's' and confirmacao.lower() != 'n':
                                    print('Por favor, digite apenas s para SIM ou n para Não')

                            if confirmacao.lower() == 's':
                                items[items.index(NomeDoItem)] = NovoNomeDoItem
                                dado[Nome]['items'] = items
                                EscreverArquivo(NomeDoArquivo, dado)
                                print('Confirmado!')
                                return None
                        else:
                            print('Por favor, não pode ser um valor repetido')
                    else:
                        print('Por favor, não pode conter apenas espaços vazios')
            else:
                print('Por favor, digite um item que ja existe')
        else:
            print('Por favor, não pode conter apenas espaços vazios')


# ------------------------------------------------------------------------------------------
def ApagarItem(Nome):
    dado = LerArquivo(NomeDoArquivo)

    items = dado[Nome]['items']

    while True:
        NomeDoItem = input('Digite o item a ser excluído (-v:voltar) ').strip()

        if NomeDoItem == '-v':
            return None
        
        confirmacao = ''
        if len(NomeDoItem) > 0:
            if NomeDoItem in items:        
                while confirmacao.lower() != 's' and confirmacao.lower() != 'n':
                    confirmacao = input(f'Excluir item {NomeDoItem}, confirmar? (s/n) ').strip()
                    if confirmacao.lower() != 's' and confirmacao.lower() != 'n':
                        print('Por favor, digite apenas s para SIM ou n para Não')

                if confirmacao.lower() == 's':
                    del items[items.index(NomeDoItem)]
                    dado[Nome]['items'] = items
                    EscreverArquivo(NomeDoArquivo, dado)
                    print('Confirmado!')
                    return None
    
            else:
                print('Por favor, digite um item que ja existe')
        else:
            print('Por favor, não pode conter apenas espaços vazios')


# -----------------------------------------------------------------------------------------------
def RealizarSorteio(Nome):
    
    '''
    Transfere todos os itens de um conjunto e realiza um sorteio, mostrando apenas o valor sorteado
    '''

    from random import choice
    dado = LerArquivo(NomeDoArquivo)

    items = dado[Nome]['items']

    print('=' * 40)
    print(f'O item sorteado foi >>>>> | {choice(items)} |')
    print('=' * 40)


# ---------------------------------------------------------------------------------------------------
def ListaItens(Nome):
    
    '''
    Permite que o usuário visualize todos os itens disponiveis para sorteio
    '''

    dado = LerArquivo(NomeDoArquivo)
    item = dado[Nome]['items']

    print('=' * 30)
    for indice in item:
        print(indice)
    print('=' * 30)


# ---------------------------------------------------------------------------------------------------
def EntrarConjunto():
    
    '''
    Permite que o usuário entre em um conjunto, caso ele já esteja criado, e faça alterações e ações
    '''

    nome = ''
    dado = LerArquivo(NomeDoArquivo)
    while nome not in dado.keys():
        nome = input('Digite o nome do conjunto (-v:voltar) ').strip()
        if nome == '-v':
            return None
    
    mensagem = f' Conjunto: {nome} '
    while True:

        print(f'{mensagem:-^40}')
        print(' [ 1 - Adicionar item           ]')
        print(' [ 2 - Editar item              ]')
        print(' [ 3 - Apagar item              ]')
        print(' [ 4 - Realizar sorteio         ]')
        print(' [ 5 - Lista de itens           ]')
        print(' [ 6 - Voltar ao menu principal ]')
        print('-' * 40)

        opcao = input('Selecione uma opção >>> ').strip()

        if opcao == '1':
            AdicionarItem(nome)

        elif opcao == '2':
            if len(dado[nome]['items']) > 0:
                EditarItem(nome)
            else:
                print('Não existe item a ser editado')

        elif opcao == '3':
            if len(dado[nome]['items']) > 0:
                ApagarItem(nome)
            else:
                print('Não existe item a ser excluído')

        elif opcao == '4':
            if len(dado[nome]['items']) > 0:
                RealizarSorteio(nome)
            else:
                print('Não existe item a ser sorteado')

        elif opcao == '5':
            if len(dado[nome]['items']) > 0:
                ListaItens(nome)
            else:
                print('Não existe item a ser sorteado')

        elif opcao == '6':
            print('Retornando ao menu princiapal')
            break

        else:
            print('Por favor, digite um valor válido')


# ---------------------------------------------------------------------------------------------------
def ApagarConjunto():
    
    '''
    Permite que o usuário apague um conjunto do dicionário, ação que apaga todos os itens relacionados
    '''

    nome = ''
    dado = LerArquivo(NomeDoArquivo)
    while nome not in dado.keys():
        nome = input('Digite o nome do conjunto (-v:voltar) ').strip()
        if nome == '-v':
            return None
        
    confirmacao = ''
    while confirmacao.lower() != 's' and confirmacao.lower() != 'n':
        confirmacao = input(f'Apagar o conjunto {nome}, confirmar? (s/n) ').strip()
        if confirmacao.lower() != 's' and confirmacao.lower() != 'n':
            print('Por favor, digite apenas S para sim ou N para não')

    if confirmacao.lower() == 's':
        try:
            del dado[nome]
            EscreverArquivo(NomeDoArquivo, dado)
            print('Concluido!')
        except:
            print('Ocorreu um erro, não foi possivel excluir')


# ------------------------------------------------------------------------
def RenomearConjunto():
    
    '''
    Permite que o usuário mude o nome do conjunto, mantendo todos os seus itens
    '''

    nome = ''
    dado = LerArquivo(NomeDoArquivo)
    while nome not in dado.keys():
        nome = input('Digite o nome do conjunto (-v:voltar) ').strip()
        if nome == '-v':
            return None
        
    #NovoNome = ''
    #while len(NovoNome) == 0 or NovoNome in dado.keys():
    while True:
        NovoNome = input('Digite o novo nome do conjunto (-v:voltar) ').strip()
        if NovoNome == '-v':
            return None
        
        confirmacao = ''
        if len(NovoNome) > 0:
            if NovoNome not in dado.keys():

                while confirmacao.lower() != 's' and confirmacao.lower() != 'n':
                    confirmacao = input(f'Mudar de {nome} para {NovoNome}, confirmar? (s/n) ').strip()
                    if confirmacao.lower() != 's' and confirmacao.lower() != 'n':
                        print('Por favor, digite apenas s para SIM ou n para Não')

                if confirmacao.lower() == 's':
                    dado[NovoNome] = dado[nome]
                    del dado[nome]
                    EscreverArquivo(NomeDoArquivo, dado)
                    print('Confirmado!')
                    return None
            else:
                print('Por favor, não pode ser um nome já existente')
        else:
            print('Por favor, não pode conter apenas espaços vazios')


# ------------------------------------------------------------------------
def ListaConjunto():
    
    '''
    Permite que o usuário veja todos os nomes de conjuntos disponiveis
    '''

    dado = LerArquivo(NomeDoArquivo)

    print('=' * 30)
    for Nomes in dado.keys():
        print(Nomes)
    print('=' * 30)


# ------------------------------------------------------------------------
def MenuPrincipal():
    
    '''
    Função principal onde e gerenciado o menu de opções para direcionar o usuário 
    '''

    while True:

        dado = LerArquivo(NomeDoArquivo)

        print(f'{" Menu Principal ":-^40}')
        print(' [ 1 - Criar conjunto     ]')
        print(' [ 2 - Entrar conjunto    ]')
        print(' [ 3 - Apagar conjunto    ]')
        print(' [ 4 - Renomear conjunto  ]')
        print(' [ 5 - Lista de conjuntos ]')
        print(' [ 6 - Sair               ]')
        print('-' * 40)

        opcao = input('Selecione uma opção >>> ').strip()

        if opcao == '1':
            CriarConjunto()

        elif opcao == '2':
            if len(dado.keys()) > 0:
                EntrarConjunto()
            else:
                print('Não existe nenhum conjunto disponivel')

        elif opcao == '3':
            if len(dado.keys()) > 0:
                ApagarConjunto()
            else:
                print('Não existe nenhum conjunto disponivel')

        elif opcao == '4':
            if len(dado.keys()) > 0:
                RenomearConjunto()
            else:
                print('Não existe nenhum conjunto disponivel')

        elif opcao == '5':
            if len(dado.keys()) > 0:
                ListaConjunto()
            else:
                print('Não existe nenhum conjunto disponivel')

        elif opcao == '6':
            break

        else:
            print('Por favor, digite um valor válido')

# Verifica se o arquivo JSON utilizado no programa já foi criado
if LerArquivo(NomeDoArquivo) == None:
    modelo = {}
    # Senão, ele é criado com o modelo escolhido, nesta versão, sera um dicionário
    EscreverArquivo(NomeDoArquivo, modelo)

# Inicia o programa onde todas as ações podem ser administradas pelo usuário
MenuPrincipal()
