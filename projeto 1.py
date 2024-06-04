# ----------------------------------------------------------------------------------------
# IMPORTAÇÕES
# ----------------------------------------------------------------------------------------

import json
import os
from datetime import datetime

# ----------------------------------------------------------------------------------------
# FUNÇÕES AUXILIARES - JSON
# ----------------------------------------------------------------------------------------

# Função que recebe os dados de conserto do JSON e transforma suas chaves de "string" -> "tupla"
def carregar_chaves_conserto(dados):
    novos_dados = dict()
    for chave in dados:
        chave_string = chave.split("_")
        nova_chave = (chave_string[0], chave_string[1], chave_string[2])
        novos_dados[nova_chave] = dados[chave]
    return novos_dados

# Função que recebe os dados de conserto em memória e transforma suas chaves de "tupla" -> "string"
def salvar_chaves_conserto(dados):
    novos_dados = dict()
    for chave in dados:
        nova_chave = f"{chave[0]}_{chave[1]}_{chave[2]}"
        novos_dados[nova_chave] = dados[chave]
    return novos_dados

# Função para carregar os dados de um arquivo JSON
def carregar_dados(nome_arquivo):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r', -1, 'UTF-8') as f:
            if nome_arquivo == "consertos.json":
                dados = json.load(f)
                return carregar_chaves_conserto(dados)
            else:
                return json.load(f)
    else:
        return {}

# Função para salvar dados em um arquivo JSON
def salvar_dados(dados, nome_arquivo):
    with open(nome_arquivo, 'w', -1, 'UTF-8') as f:
        if nome_arquivo == "consertos.json":
            json.dump(salvar_chaves_conserto(dados), f, indent=4)
        else:
            json.dump(dados, f, indent=4)

# ----------------------------------------------------------------------------------------
# FUNÇÕES AUXILIARES
# ----------------------------------------------------------------------------------------

# Função que requisita dados de um conserto e retorna a chave primária
def entrada_chave_conserto():
    cpf = input("CPF do mecânico: ")
    placa = input("Placa do veículo: ")
    # TODO - Check if the date is after todays date
    data_entrada = input("Data de Entrada (dd/mm/aaaa): ")
    return (cpf, placa, data_entrada)

# Função para calcular a idade a partir da data de nascimento
def calcular_idade(data_nascimento):
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    hoje = datetime.today()
    return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

# ----------------------------------------------------------------------------------------
# MENUS & SUB-MENUS
# ----------------------------------------------------------------------------------------

# Função principal
def main():
    arquivo_mecanicos = 'mecanicos.json'
    arquivo_veiculos = 'veiculos.json'
    arquivo_consertos = 'consertos.json'
    
    mecanicos = carregar_dados(arquivo_mecanicos)
    veiculos = carregar_dados(arquivo_veiculos)
    consertos = carregar_dados(arquivo_consertos)

    menu_opcao = True

    while menu_opcao:
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
            print("\nFim do programa...")
            menu_opcao = False
        else:
            print("Opção inválida. Tente novamente.")

# ---------------------
# Submenu de Mecânicos
# ---------------------

def submenu_mecanicos(mecanicos, nome_arquivo):
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
            if not listar_todos(mecanicos, 'CPF'):
                print("\nDados não encontrados!")
        elif opcao == '2':
            cpf = input("CPF: ")
            if not listar_um(mecanicos, cpf, 'CPF'):
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

# --------------------
# Submenu de Veículos
# --------------------

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
            if not listar_todos(veiculos, 'Placa'):
                print("\nDados não encontrados!")
        elif opcao == '2':
            placa = input("Placa: ")
            if not listar_um(veiculos, placa, 'Placa'):
                print("\nRegistro não encontrado!")
        elif opcao == '3':
            placa = input("Placa: ")
            if placa in veiculos:
                print("\nVeículo já registrado!")
            elif adicionar_veiculo(veiculos, placa):
                print("\nVeículo registrado com sucesso!")
                salvar_dados(veiculos, nome_arquivo)
        elif opcao == '4':
            if not alterar_veiculo(veiculos):
                print("\nPlaca não encontrada!")
            else:
                print("\nVeículo alterado com sucesso!")
                salvar_dados(veiculos, nome_arquivo)
        elif opcao == '5':
            if not excluir_veiculo(veiculos):
                print("\nPlaca não encontrada!")
            else:
                print("\nVeículo excluído com sucesso!")
                salvar_dados(veiculos, nome_arquivo)
        elif opcao == '6':
            continuar_menu = False
        else:
            print("Opção inválida. Tente novamente.")

# ---------------------
# Submenu de Consertos
# ---------------------

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
            if not listar_todos(consertos, 'Código'):
                print("\nDados não encontrados!")
        elif opcao == '2':
            chave_conserto = entrada_chave_conserto()
            if not listar_um(veiculos, chave_conserto, 'Código'):
                print("\nRegistro não encontrado!")
        elif opcao == '3':
            if not adicionar_conserto(consertos, mecanicos, veiculos):
                print("\nNão foi possível adicionar o conserto!")
            else:
                print("\nConserto registrado com sucesso!")
                salvar_dados(consertos, nome_arquivo)
        elif opcao == '4':
            chave_conserto = entrada_chave_conserto()
            if not alterar_conserto(consertos, chave_conserto):
                print("\nConserto não encontrado.")
            else:
                print("\nConserto alterado com sucesso!")
                salvar_dados(consertos, nome_arquivo)
        elif opcao == '5':
            chave_conserto = entrada_chave_conserto()
            if not excluir_conserto(consertos, chave_conserto):
                print("\nConserto não encontrado!")
            else:
                print("\nConserto excluído com sucesso!")
                salvar_dados(consertos, nome_arquivo)
        elif opcao == '6':
            continuar_menu = False
        else:
            print("Opção inválida. Tente novamente.")

# ----------------------
# Submenu de Relatórios
# ----------------------

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

# ----------------------------------------------------------------------------------------
# FUNÇÕES - MECÂNICOS
# ----------------------------------------------------------------------------------------

# Função que retorna um dicionário contendo as informações de um mecânico
def gerar_mecanico():
    nome = input("Nome: ")
    data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
    sexo = input("Sexo: ")
    salario = float(input("Salário: "))
    emails = input("E-mails (separados por vírgula): ").split(',')
    telefones = input("Telefones (separados por vírgula): ").split(',')

    return {
        "Nome": nome,
        "Data de Nascimento": data_nascimento,
        "Sexo": sexo,
        "Salário": salario,
        "E-mails": emails,
        "Telefones": telefones
    }

# Função que adiciona um mecânico
def adicionar_mecanico(mecanicos, cpf):
    mecanico = gerar_mecanico()
    mecanicos[cpf] = mecanico
    return True

# Função que altera um mecânico
def alterar_mecanico(mecanicos):
    cpf = input("Digite o CPF do mecânico que deseja alterar: ")
    if cpf not in mecanicos:
        return False
    else:
        return adicionar_mecanico(mecanicos, cpf)

# Função que exclui um mecânico
def excluir_mecanico(mecanicos):
    cpf = input("CPF do mecânico a ser removido: ")
    if cpf in mecanicos:
        confirmar = input(f"Você tem certeza que deseja remover o mecânico {mecanicos[cpf]['Nome']}? (s/n): ")
        if confirmar.lower() == 's':
            del mecanicos[cpf]
            return True
        else:
            print("Operação cancelada.")
    else:
        return False

# ----------------------------------------------------------------------------------------
# FUNÇÕES - VEÍCULOS
# ----------------------------------------------------------------------------------------

def gerar_veiculo():
    tipo = input("Tipo: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    portas = int(input("Portas: "))
    combustivel = input("Combustível: ")
    cor = input("Cor: ")

    return {
        "Tipo": tipo,
        "Marca": marca,
        "Modelo": modelo,
        "Ano": ano,
        "Portas": portas,
        "Combustível": combustivel,
        "Cor": cor
    }

# Função que adiciona um veículo
def adicionar_veiculo(veiculos, placa):
    veiculo = gerar_veiculo()
    veiculos[placa] = veiculo
    return True

# Função que altera um veículo
def alterar_veiculo(veiculos):
    placa = input("Placa do veículo a ser alterado: ")
    if placa not in veiculos:
        return False
    else:
        return adicionar_veiculo(veiculos, placa)

# Função que exclui um veículo
def excluir_veiculo(veiculos):
    placa = input("Placa do veículo a ser removido: ")
    if placa in veiculos:
        confirmar = input(f"Você tem certeza que deseja remover o veículo {veiculos[placa]['Marca']} - {veiculos[placa]['Modelo']}? (s/n): ")
        if confirmar.lower() == 's':
            del veiculos[placa]
            return True
        else:
            print("Operação cancelada.")
    else:
        return False

# ----------------------------------------------------------------------------------------
# FUNÇÕES - CONSERTOS
# ----------------------------------------------------------------------------------------

def gerar_conserto():
    data_saida = input("Data de Saída (dd/mm/aaaa): ")
    problemas = input("Descrição dos Problemas: ")
    valor_conserto = float(input("Valor do Conserto: "))
    
    return {
        "Data de Saída": data_saida,
        "Descrição dos Problemas": problemas,
        "Valor de Conserto": valor_conserto
    }

# Função que adiciona um conserto
def adicionar_conserto(consertos, mecanicos, veiculos):
    chave = entrada_chave_conserto()
    if chave[0] not in mecanicos: # CPF
        print("Mecânico não encontrado.")
        return False

    if chave[1] not in veiculos: # Placa
        print("Veículo não encontrado.")
        return False
    
    conserto = gerar_conserto()

    if chave in consertos:
        return False

    consertos[chave] = { 
        "CPF": chave[0],
        "Placa": chave[1],
        "Data de Entrada": chave[2],
        **conserto 
    }
    
    return True

# Função que altera um conserto
def alterar_conserto(consertos, chave_conserto):
    if chave_conserto not in consertos:
        return False

    conserto = gerar_conserto()

    consertos[chave_conserto] = {
        "CPF": chave_conserto[0],
        "Placa": chave_conserto[1],
        "Data de Entrada": chave_conserto[2],
        **conserto
    }
    
    return True

# Função que exclui um conserto
def excluir_conserto(consertos, chave_conserto):
    if chave_conserto in consertos:
        confirmar = input(f"Você tem certeza que deseja remover o conserto do veículo {consertos[chave_conserto]['Placa']} realizado por {consertos[chave_conserto]['CPF']}? (s/n): ")
        if confirmar.lower() == 's':
            del consertos[chave_conserto]
            return True
        else:
            print("Operação cancelada.")
    else:
        return False

# ----------------------------------------------------------------------------------------
# FUNÇÕES - LISTAGEM
# ----------------------------------------------------------------------------------------

# Lista todas as informações de um conjunto de dados
def listar_todos(dados, nome_chave='Código'):
    if dados:
        for chave in dados:
            listar_um(dados, chave, nome_chave)
        return True
    else:
        return False

# Dado uma chave, lista as informações específicas em conjunto de dados.
def listar_um(dados, chave, nome_chave='Código'):
    if chave in dados:
        print()
        print(f"{nome_chave}: {" - ".join(chave)}")
        for item in dados[chave]:
            if type(dados[chave][item]) == list:
                print(f"{item}: {" - ".join(dados[chave][item])}")
            else:
                print(f"{item}: {dados[chave][item]}")
        print("-" * 25)
        return True
    else:
        return False

# ----------------------------------------------------------------------------------------
# FUNÇÕES - RELATÓRIOS
# ----------------------------------------------------------------------------------------

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

# Execução do programa
if __name__ == '__main__':
    main()