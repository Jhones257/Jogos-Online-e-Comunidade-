from terminaltables import AsciiTable

# Dicionário para armazenar informações dos usuários
usuarios = {}

# E-mail do usuário logado (global)
usuario_logado = None

def fazer_login():
    global usuario_logado
    
    print("Login")
    print("-----")
    
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    
    # Verifica se o e-mail e senha correspondem a um usuário registrado
    if email in usuarios and usuarios[email]['Senha'] == senha:
        usuario_logado = email
        print("\nLogin bem-sucedido!\n")
        menu_secundario()
    else:
        print("\nE-mail ou senha incorretos. Tente novamente.\n")

def registrar_conta():
    print("Registro de Conta")
    print("-----------------")
    
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    
    # Verificar se o e-mail já está registrado
    if email in usuarios:
        print("E-mail já registrado. Tente novamente.")
        return
    
    # Adicionar usuário ao dicionário
    usuarios[email] = {
        'Nome': nome,
        'Senha': senha,
        'Amigos': []
    }
    
    print("\nRegistro concluído com sucesso!\n")

def menu_principal():
    print("Plataforma de Comunidades de Jogos Online")
    print("----------------------------------------")
    
    table_data = [
        ["Opção", "Descrição"],
        ["1", "Login"],
        ["2", "Registrar Conta"],
        ["3", "Sair"]
    ]
    
    # Criar e exibir tabela de opções
    table = AsciiTable(table_data)
    print(table.table)
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == '1':
        fazer_login()
    elif opcao == '2':
        registrar_conta()
    elif opcao == '3':
        print("Saindo...")
        return
    else:
        print("Opção inválida. Tente novamente.\n")
    
    # Voltar ao menu principal após a execução da opção selecionada
    menu_principal()

def mostrar_usuarios():
    print("Lista de Usuários Registrados")
    print("-----------------------------")
    
    # Cabeçalho da tabela
    table_data = [["E-mail", "Nome"]]
    
    # Preencher dados da tabela
    for email, info in usuarios.items():
        table_data.append([email, info['Nome']])
    
    # Criar e exibir tabela
    table = AsciiTable(table_data)
    print(table.table)

def mostrar_amigos():
    print("Lista de Amigos")
    print("---------------")
    
    # Verifica se o usuário tem amigos
    if not usuarios[usuario_logado]['Amigos']:
        print("Você não tem amigos adicionados ainda.")
        return
    
    table_data = [["E-mail", "Nome"]]
    
    # Preenche dados da tabela com os amigos do usuário logado
    for email in usuarios[usuario_logado]['Amigos']:
        table_data.append([email, usuarios[email]['Nome']])
    
    table = AsciiTable(table_data)
    print(table.table)

def adicionar_amigo():
    print("Adicionar Amigo")
    print("---------------")
    
    email_amigo = input("Digite o e-mail do amigo: ")
    
    # Verifica se o e-mail do amigo é válido
    if email_amigo not in usuarios:
        print("E-mail de amigo inválido. Tente novamente.")
        return
    
    # Verifica se o amigo já está na lista de amigos
    if email_amigo in usuarios[usuario_logado]['Amigos']:
        print("Este usuário já está na sua lista de amigos.")
        return
    
    # Adicionar amigo à lista de amigos do usuário
    usuarios[usuario_logado]['Amigos'].append(email_amigo)
    
    print("\nAmigo adicionado com sucesso!\n")

def menu_secundario():
    global usuario_logado
    
    print(f"Bem-vindo, {usuarios[usuario_logado]['Nome']}!")
    print("Menu Secundário")
    print("----------------")
    
    # Dados para a tabela de opções
    table_data = [
        ["Opção", "Descrição"],
        ["1", "Ver Lista de Usuários Registrados"],
        ["2", "Ver Lista de Amigos"],
        ["3", "Adicionar Amigo"],
        ["4", "Deslogar"],
        ["5", "Sair"]
    ]
    
    # Criar e exibir tabela de opções
    table = AsciiTable(table_data)
    print(table.table)
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == '1':
        mostrar_usuarios()
    elif opcao == '2':
        mostrar_amigos()
    elif opcao == '3':
        adicionar_amigo()
    elif opcao == '4':
        usuario_logado = None
        print("\nDeslogado com sucesso!\n")
        menu_principal()
    elif opcao == '5':
        print("Saindo...")
        return
    else:
        print("Opção inválida. Tente novamente.\n")
    
    menu_secundario()

menu_principal()
