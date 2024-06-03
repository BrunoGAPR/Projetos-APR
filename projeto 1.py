import json
import os
from datetime import datetime

# Função para carregar dados de um arquivo JSON
def carregar_dados(nome_arquivo):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as f:
            return json.load(f)
    return {}

# Função para salvar dados em um arquivo JSON
def salvar_dados(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

# Função para calcular a idade a partir da data de nascimento
def calcular_idade(data_nascimento):
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    hoje = datetime.today()
    return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

# Função principal
def main():
    arquivo_mecanicos = 'mecanicos.json'
    arquivo_veiculos = 'veiculos.json'
    arquivo_consertos = 'consertos.json'
    
    mecanicos = carregar_dados(arquivo_mecanicos)
    veiculos = carregar_dados(arquivo_veiculos)
    consertos = carregar_dados(arquivo_consertos)

    while True:
        print("\nMenu de Opções:")
        print("1. Submenu de Mecânicos")
        print("2. Submenu de Veículos")
        print("3. Submenu de Consertos")
        print("4. Submenu Relatórios")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            submenu_mecanicos(mecanicos, arquivo_mecanicos)
        elif opcao == '2':
            submenu_veiculos(veiculos, arquivo_veiculos)
        elif opcao == '3':
            submenu_consertos(consertos, mecanicos, veiculos, arquivo_consertos)
        elif opcao == '4':
            submenu_relatorios(mecanicos, veiculos, consertos)
        elif opcao == '5':
            return
        else:
            print("Opção inválida. Tente novamente.")

# Submenu de Mecânicos
def submenu_mecanicos(mecanicos, nome_arquivo):
    info = {
        "nome": "Nome",
        "data_nascimento": "Data de Nascimento",
        "sexo": "Sexo",
        "salario": "Salário",
        "emails": "E-mails",
        "telefones": "Telefones"
    }
    continuar_menu = True
    while continuar_menu:
        print("\nSubmenu de Mecânicos:")
        print("1. Listar todos")
        print("2. Listar um específico")
        print("3. Incluir")
        print("4. Alterar")
        print("5. Excluir")
        print("6. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            if not listar_todos(mecanicos, info):
                print("\nDados não encontrados!")
        elif opcao == '2':
            cpf = input("CPF: ")
            if not listar_um(mecanicos, cpf, info):
                print("\nRegistro não encontrado.")
        elif opcao == '3':
            cpf = input("CPF: ")
            if cpf in mecanicos:
                print("\nMecânico já registrado!")
            elif adicionar_mecanico(mecanicos, cpf):
                print("\nMecânico cadastrado com sucesso!")
                salvar_dados(mecanicos, nome_arquivo)
        elif opcao == '4':
            if alterar_mecanico(mecanicos):
                print("\nMecânico alterado com sucesso!")
                salvar_dados(mecanicos, nome_arquivo)
            else:
                print("\nCPF do mecânico não encontrado!")
        elif opcao == '5':
            if excluir_mecanico(mecanicos):
                salvar_dados(mecanicos, nome_arquivo)
                print("\nMecânico removido com sucesso.")
            else:
                print("\nMecânico não encontrado.")
        elif opcao == '6':
            continuar_menu = False
        else:
            print("Opção inválida. Tente novamente.")

# Submenu de Veículos
def submenu_veiculos(veiculos, nome_arquivo):
    continuar_menu = True
    while continuar_menu:
        print("\nSubmenu de Veículos:")
        print("1. Listar todos")
        print("2. Listar um específico")
        print("3. Incluir")
        print("4. Alterar")
        print("5. Excluir")
        print("6. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_todos(veiculos)
        elif opcao == '2':
            listar_um(veiculos)
        elif opcao == '3':
            adicionar_veiculo(veiculos)
            salvar_dados(veiculos, nome_arquivo)
        elif opcao == '4':
            alterar_veiculo(veiculos)
            salvar_dados(veiculos, nome_arquivo)
        elif opcao == '5':
            excluir_veiculo(veiculos)
            salvar_dados(veiculos, nome_arquivo)
        elif opcao == '6':
            continuar_menu = False
        else:
            print("Opção inválida. Tente novamente.")

def entrada_chave_conserto():
    cpf = input("CPF do mecânico: ")
    placa = input("Placa do veículo: ")
    data_entrada = input("Data de Entrada (dd/mm/aaaa): ")
    return (cpf, placa, data_entrada)

# Submenu de Consertos
def submenu_consertos(consertos, mecanicos, veiculos, nome_arquivo):
    continuar_menu = True
    while continuar_menu:
        print("\nSubmenu de Consertos:")
        print("1. Listar todos")
        print("2. Listar um específico")
        print("3. Incluir")
        print("4. Alterar")
        print("5. Excluir")
        print("6. Voltar")
        opcao = input("Escolha uma opção: ")

    if opcao == '1':
        listar_todos(consertos)
    elif opcao == '2':
        listar_um(consertos)
    elif opcao == '3':
        adicionar_conserto(consertos, mecanicos, veiculos)
        salvar_dados(consertos, nome_arquivo)
    elif opcao == '4':
        chave_conserto = entrada_chave_conserto()
        alterar_conserto(consertos, chave_conserto)
        salvar_dados(consertos, nome_arquivo)
    elif opcao == '5':
        chave_conserto = entrada_chave_conserto()
        excluir_conserto(consertos)
        salvar_dados(consertos, nome_arquivo)
    elif opcao == '6':
        continuar_menu = False
    else:
        print("Opção inválida. Tente novamente.")

# Submenu de Relatórios
def submenu_relatorios(mecanicos, veiculos, consertos):
    continuar_menu = True
    while continuar_menu:
        print("\nSubmenu Relatórios:")
        print("1. Mecânicos com mais de X anos")
        print("2. Veículos de determinada marca")
        print("3. Consertos entre datas X e Y")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")

    if opcao == '1':
        relatorio_mecanicos_por_idade(mecanicos)
    elif opcao == '2':
        relatorio_veiculos_por_marca(veiculos)
    elif opcao == '3':
        relatorio_consertos_por_data(mecanicos, veiculos, consertos)
    elif opcao == '4':
        continuar_menu = False
    else:
        print("Opção inválida. Tente novamente.")

# Funções auxiliares para Mecânicos
def gerar_mecanico():
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
    sexo = input("Sexo: ")
    salario = float(input("Salário: "))
    emails = input("E-mails (separados por vírgula): ").split(',')
    telefones = input("Telefones (separados por vírgula): ").split(',')

    return {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "salario": salario,
        "emails": emails,
        "telefones": telefones
    }

def adicionar_mecanico(mecanicos, cpf):
    mecanico = gerar_mecanico()
    mecanicos[cpf] = mecanico
    return True

def alterar_mecanico(mecanicos):
    cpf = input("Digite o CPF do mecânico que deseja alterar: ")
    if cpf not in mecanicos:
        return False
    else:
        return adicionar_mecanico(mecanicos, cpf)

def excluir_mecanico(mecanicos):
    cpf = input("CPF do mecânico a ser removido: ")
    if cpf in mecanicos:
        confirmar = input(f"Você tem certeza que deseja remover o mecânico {mecanicos[cpf]['nome']}? (s/n): ")
        if confirmar.lower() == 's':
            del mecanicos[cpf]
            return True
        else:
            print("Operação cancelada.")
    else:
        return False

# Funções auxiliares para Veículos
def adicionar_veiculo(veiculos):
    placa = input("Placa: ")
    if placa in veiculos:
        print("Veículo já cadastrado.")
        return

    tipo = input("Tipo: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    portas = int(input("Portas: "))
    combustivel = input("Combustível: ")
    cor = input("Cor: ")

    veiculos[placa] = {
        "Tipo": tipo,
        "Marca": marca,
        "Modelo": modelo,
        "Ano": ano,
        "Portas": portas,
        "Combustível": combustivel,
        "Cor": cor
    }
    print("Veículo adicionado com sucesso.")

def alterar_veiculo(veiculos):
    placa = input("Placa do veículo a ser alterado: ")
    if placa not in veiculos:
        print("Veículo não encontrado.")
        return

    tipo = input("Tipo: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    portas = int(input("Portas: "))
    combustivel = input("Combustível: ")
    cor = input("Cor: ")

    veiculos[placa] = {
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "portas": portas,
        "combustível": combustivel,
        "cor": cor
    }
    print("Veículo alterado com sucesso.")

def excluir_veiculo(veiculos):
    placa = input("Placa do veículo a ser removido: ")
    if placa in veiculos:
        confirmar = input(f"Você tem certeza que deseja remover o veículo {veiculos[placa]['marca']} - {veiculos[placa]['modelo']}? (s/n): ")
        if confirmar.lower() == 's':
            del veiculos[placa]
            print("Veículo removido com sucesso.")
        else:
            print("Operação cancelada.")
    else:
        print("Veículo não encontrado.")

# Funções auxiliares para Consertos
def adicionar_conserto(consertos, mecanicos, veiculos):
    cpf = input("CPF do mecânico: ")
    if cpf not in mecanicos:
        print("Mecânico não encontrado.")
        return

    placa = input("Placa do veículo: ")
    if placa not in veiculos:
        print("Veículo não encontrado.")
        return

    data_entrada = input("Data de Entrada (dd/mm/aaaa): ")
    data_saida = input("Data de Saída (dd/mm/aaaa): ")
    problemas = input("Descrição dos Problemas: ")
    valor_conserto = float(input("Valor do Conserto: "))

    chave_conserto = (cpf, placa, data_entrada)
    if chave_conserto in consertos:
        print("Conserto já cadastrado.")
        return False

    consertos[chave_conserto] = {
        "cpf": cpf,
        "placa": placa,
        "data_entrada": data_entrada,
        "data_saida": data_saida,
        "desc_problemas": problemas,
        "valor_conserto": valor_conserto
    }
    print("Conserto adicionado com sucesso.")

def alterar_conserto(consertos, chave_conserto):
    if chave_conserto not in consertos:
        print("Conserto não encontrado.")
        return

    data_saida = input("Data de Saída (dd/mm/aaaa): ")
    problemas = input("Descrição dos Problemas: ")
    valor_conserto = float(input("Valor do Conserto: "))

    consertos[chave_conserto] = {
        "cpf": chave_conserto[0],
        "placa": chave_conserto[1],
        "data_entrada": chave_conserto[2],
        "data_saida": data_saida,
        "desc_problemas": problemas,
        "valor_conserto": valor_conserto
    }
    print("Conserto alterado com sucesso.")

def excluir_conserto(consertos, chave_conserto):
    if chave_conserto in consertos:
        confirmar = input(f"Você tem certeza que deseja remover o conserto do veículo {consertos[chave_conserto]['placa']} realizado por {consertos[chave_conserto]['cpf']}? (s/n): ")
        if confirmar.lower() == 's':
            del consertos[chave_conserto]
            print("Conserto removido com sucesso.")
        else:
            print("Operação cancelada.")
    else:
        print("Conserto não encontrado.")

# Funções de listagem
def listar_todos(dados, info):
    if dados:
        for chave in dados:
            print()
            listar_um(dados, chave, info)
        return True
    else:
        return False

def listar_um(dados, chave, info):
    if chave in dados:
        print("-" * 25)
        for item in dados[chave]:
            if type(dados[chave][item]) == list:
                print(f"{info[item]}: {" - ".join(dados[chave][item])}")
            else:
                print(f"{info[item]}: {dados[chave][item]}")
        print("-" * 25)
        return True
    else:
        return False

# Funções de relatórios
def relatorio_mecanicos_por_idade(mecanicos):
    idade_limite = int(input("Informe a idade mínima: "))
    for cpf, mecanico in mecanicos.items():
        idade = calcular_idade(mecanico['data_nascimento'])
    if idade > idade_limite:
        print(f"{cpf}: {mecanico}")

def relatorio_veiculos_por_marca(veiculos):
    marca = input("Informe a marca do veículo: ")
    for placa, veiculo in veiculos.items():
        if veiculo['marca'].lower() == marca.lower():
            print(f"{placa}: {veiculo}")

def relatorio_consertos_por_data(mecanicos, veiculos, consertos):
    data_inicio = input("Data de início (dd/mm/aaaa): ")
    data_fim = input("Data de término (dd/mm/aaaa): ")

    data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y')
    data_fim = datetime.strptime(data_fim, '%d/%m/%Y')

    for chave, conserto in consertos.items():
        data_entrada = datetime.strptime(conserto['data_entrada'], '%d/%m/%Y')
    if data_inicio <= data_entrada <= data_fim:
            mecanico = mecanicos[conserto['cpf']]
            veiculo = veiculos[conserto['placa']]
            print(f"Mecânico: {conserto['cpf']}, {mecanico['nome']}")
            print(f"Veículo: {conserto['placa']}, {veiculo['marca']}, {veiculo['modelo']}, {veiculo['ano']}")
            print(f"Conserto: {conserto}")

if __name__ == '__main__':
    main()