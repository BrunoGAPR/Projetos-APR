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
            
def salvar_dados_relatorios(dados, nome_arquivo, valor):
    nome_relatorios = { 'relatorio_mecanicos.txt': f'Mecânicos com idade mínima de "{valor}"', 'relatorio_veiculos.txt': f'Veículos da marca "{valor}"', 'relatorio_consertos.txt': f'Consertos entre "{valor}"' }
    
    with open(nome_arquivo, 'w', -1, 'UTF-8') as f:
        titulo = f"Relatório de '{nome_relatorios[nome_arquivo]}'"
        f.write("-" * 20 + " " + titulo + " " + "-" * 20 + "\n")
        for chave in dados:
            for item in dados[chave]:
                if type(dados[chave][item]) == list:
                    f.write(f"{item}: {" - ".join(dados[chave][item])}\n")
                else:
                    f.write(f"{item}: {dados[chave][item]}\n")
            f.write("-" * 45 + "#" + "\n")
        f.close()

# ----------------------------------------------------------------------------------------
# FUNÇÕES AUXILIARES
# ----------------------------------------------------------------------------------------

# Função que requisita dados de um conserto e retorna a chave primária
def entrada_chave_conserto():
    cpf = input("CPF do mecânico: ")
    placa = input("Placa do veículo: ")
    data_entrada = input("Data de Entrada (dd/mm/aaaa): ")
    return (cpf, placa, data_entrada)

# Função para calcular a idade a partir da data de nascimento
def calcular_idade(data_nascimento):
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    hoje = datetime.today()
    idade = hoje.year - data_nascimento.year
    return idade

def verifica_chave_conserto(entrada, dados):
    find = False
    for chave in dados:
        if entrada[0] == chave[0] and entrada[1] == chave[1] and entrada[2] == chave[2]:
            find = True
    return find

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
            if not listar_um(consertos, chave_conserto, 'Código'):
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
            idade_minima = int(input("Idade mínima: "))
            resultado, dados = relatorio_mecanicos_por_idade(mecanicos, idade_minima)
            if not resultado:
                print(f"\nMecânicos com idade mínima de {idade_minima} anos não encontrados!")
            else:
                salvar_dados_relatorios(dados, 'relatorio_mecanicos.txt', idade_minima)
                print("\nRelatório salvo com sucesso!")   
        elif opcao == '2':
            marca = input("Digite a marca do veículo: ")
            resultado, dados = relatorio_veiculos_por_marca(veiculos, marca)
            if not resultado:
                print(f"\nVeículos da marca '{marca}' não encontrados!")
            else:
                salvar_dados_relatorios(dados, 'relatorio_veiculos.txt', marca)
                print("\nRelatório salvo com sucesso!")
        elif opcao == '3':
            data_inicio = input("Data de início (dd/mm/aaaa): ")
            data_fim = input("Data de término (dd/mm/aaaa): ")  
            resultado, dados = relatorio_consertos_por_data(mecanicos, veiculos, consertos, data_inicio, data_fim)
            if not resultado:
                print(f"\nConsertos registrados entre '{data_inicio}' - '{data_fim}' não encontrados!")
            else:
                salvar_dados_relatorios(dados, 'relatorio_consertos.txt', data_inicio + ' - ' + data_fim)
                print("\nRelatório salvo com sucesso!")
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
        if type(chave) is list or type(chave) is tuple:
            print(f"\n{nome_chave}: {" - ".join(chave)}")
        else:
            print(f"\n{nome_chave}: {chave}")
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

def relatorio_mecanicos_por_idade(mecanicos, idade_minima):
    mecanicos_idade = {}
    for cpf in mecanicos:
        if calcular_idade(mecanicos[cpf]['Data de Nascimento']) > idade_minima:
            mecanicos_idade[cpf] = mecanicos[cpf]
    return listar_todos(mecanicos_idade, 'CPF'), mecanicos_idade

def relatorio_veiculos_por_marca(veiculos, marca):
    veiculos_marca = {}
    for placa in veiculos:
        if veiculos[placa]['Marca'].lower() == marca.lower():
            veiculos_marca[placa] = veiculos[placa]
    return listar_todos(veiculos_marca), veiculos_marca

def relatorio_consertos_por_data(mecanicos, veiculos, consertos, data_inicio, data_fim):
    data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y')
    data_fim = datetime.strptime(data_fim, '%d/%m/%Y')
    conserto_data = {}
    for chave in consertos:
        data_entrada = datetime.strptime(chave[2], '%d/%m/%Y')
        if data_inicio <= data_entrada <= data_fim:
            cpf, nome = chave[0], mecanicos[chave[0]]['Nome'],
            placa, marca, modelo, ano = veiculos[chave[1]], veiculos[chave[1]]['Marca'], veiculos[chave[1]]['Modelo'], veiculos[chave[1]]['Ano']
            conserto_data[chave] = { "CPF": cpf, "Nome": nome, "Placa": placa, "Marca": marca, "Modelo": modelo, "Ano": ano, **consertos[chave] }
    return listar_todos(conserto_data), conserto_data
            

# Execução do programa
if __name__ == '__main__':
    main()