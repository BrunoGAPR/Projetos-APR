#Bibliotecas

from mecanicos import *
from veiculos import *
from conserto import *
from auxiliares import *

#banco de dado 

BD_mecanicos = {}
BD_veiculos = {}
BD_conserto = {}

#recuperando Arquivos

recupera_mecanicos(BD_mecanicos)
recupera_veiculos(BD_veiculos)
recupera_conserto(BD_conserto)

#Menu Principal

c = 0 
while c < 5:
    print("--" * 12)
    print("Menu")
    print("--" * 12)
    print("1 - Submenu de Mecânicos")
    print("2 - Submenu de Veículo")
    print("3 - Submenu de Consertos")
    print("4 - Relatório")
    print("5 - Sair")
    print("--" * 12)

c = int(input("\nOpção: "))
print()
if c == 1:
    menu_mecânico(BD_mecanicos)
    print("\nVoltando para o menu...\n")
elif c == 2:
    menu_veículos(BD_veiculos)
    print("\nVoltando para o menu...\n")
elif c == 3:
    menu_conserto(BD_conserto)
    print("\nVoltando para o menu...\n")
elif c == 4:
    DI = input("data inicial: ")
    DF = input("data final: ")
    relatorio(BD_mecanicos, BD_veiculos, BD_conserto)
print("fim do programa.")

#fim do programa

'''''
Mecânicos
'''''

#Bibliotecas

from auxiliares import *

#funcôes mecânico

def existe_mecanico(dic, chave):
    if chave in dic.keys():
        return True
    else:
        return False

#inserir

def inserir_mecanico(dic):
    print("--" * 12)
    CPF = input("Digite o CPF: ")
    if existe_mecanico(dic, CPF):
        print("Esta pessoa já está cadastrada!")
        pausa()
    else:
        nome = input("Nome: ")
        sexo = input("sexo: ")
        data = input("Data de Nascimento: ")
        salario = float(input("Salário: "))
        email = input("E-mail: ")
        telefone = input("Telefone: ")

        dic[CPF] = (nome, sexo, data, salario, email, telefone)
        print("\nDados inseridos com sucesso!")
        pausa()

#exibir

def exibir_mecanicos(dic, chave):
    if existe_mecanico(dic, chave):
        dados = dic[chave]
        print()
        print(f"nome: {dados[0]}")
        print(f"sexo: {dados[1]}")
        print(f"data de nascimento: {dados[2]}")
        print(f"salário: {dados[3]}")
        print(f"e-mail: {dados[4]}")
        print(f"telefone: {dados[5]}")
    else:
        print("cadastro ja existente!")
        pausa()

#Alterar

def alterar_mecanico(dic , chave):
    if existe_mecanico(dic, chave):
        exibir_mecanicos(dic, chave)
        print("--" * 12)
        confirmar = input("deseja alterar os dados?(S/N): ").upper()
        if confirmar == "S":
            print()
            nome = input("Nome: ")
            sexo = input("Sexo: ")
            data = input("Data de Nascimento: ")
            salario = float(input("Salário: "))
            email = input("E-mail: ")
            telefone = input("Telefone: ")
            dic[chave] = (nome, sexo, data, salario, email, telefone)
            print("Alteração concluída com sucesso!")
            pausa()
        else:
            print("alteração cancelada.")
            pausa()
    else:
        print("cadastro inexistente.")
        pausa()

#Remover

def remover_mecanico(dic , chave):
    if existe_mecanico(dic, chave):
        exibir_mecanicos(dic, chave)
        confirmar = input("deseja remover os dados? (S/N): ").upper()
        if confirmar == "S":
            del dic[chave]
            print("Remoção concluída com sucesso!")
            pausa()
        else:
            print("remoção cancelada.")
    else:
        print("cadastro inexistente.")
        pausa()

#listar todos

def exibir_todos_mecanicos(dic):
    print("--" * 12)
    print("relatorio -> Mecânicos")
    print()
    print("CPF - Nome - sexo - endereço - salario - data de nascimento - telefone\n")
    for CPF in dic:
        tupla = dic[CPF]
        string = CPF + "-" + tupla[0] + "-" + tupla[1] + "-" + tupla[2] + "-" + tupla[3] + "-" + tupla[4] + "-" + tupla[5]
        print(string)
        print()
        pausa()

#gravar

def gravar_mecanico(dic):
    arq = open("mecanicos.txt", "w")
    for CPF in dic:
        tupla = dic[CPF]
        linha =  linha = CPF + ";" + tupla[0] + ";" + tupla[1] + ";" + str(tupla[2]) + ";" + tupla[3] + ";" + tupla[4] + ";" + tupla[5] + "\n"
        arq.write(linha)
    arq.close()

#recuperar

def recuperar_mecanico(dic):
    if existe_arquivo("mecanicos.txt"):
        arq = open("clientes.txt", "r")
        for linha in arq:
            linha = linha[:len(linha) - 1]
            lista = linha.split(";")
            CPF = lista[0]
            nome = lista[1]
            sexo = lista[2]
            endereco = lista[3]
            renda= float(lista[4])
            data_nascimento = lista[5]
            telefone = lista[6]
            dic[CPF] = (nome, sexo, endereco, renda, data_nascimento, telefone )

#menu mecanicos

def menu_mecanicos(dic):
    c = 0
    while c < 6:
        print("--" * 12)
        print("gerenciamento -> mecanicos")
        print("--" * 12)
        print("1 - inserir")
        print("2 - alterar")
        print("3 - remover")
        print("4 - exibir mecanico")
        print("5 - exibir todos mecanicos")
        print("6 - voltar para o menu")
        print("--" * 12)
    
    c = int(input("\nOpção: "))
    print()
    if c < 1 or c > 6:
        print("opção inválida")
    else:
        if c == 1:
            inserir_mecanico(dic)
        elif c == 2:
            CPF = input("digite o CPF para alterar: ")
            alterar_mecanico(dic , CPF)
        elif c == 3:
             CPF = input("Digite o CPF para Remover: ")
             remover_mecanico(dic, CPF)
        elif c == 4:
            CPF = input("Digite o CPF para exibir: ")
            exibir_mecanico(dic, CPF)
        elif c == 5:
            exibir_todos_mecanicos(dic)
        elif c == 6:
            gravar_mecanico(dic)

'''
Veiculos
'''
#biblioteca

from auxiliares import *

#BD = {}
#[codigo] = (Placa, tipo, marca, modelo, ano, porta, combustivel, cor )

#existe veiculo

def existe_veiculo(dic, chave):
    if chave in dic.keys():
        return True
    else:
        return False

#inserir veiculo

def inserir_veiculos(dic):
    codigo = input("digite o Código: ")
    if existe_veiculo(dic, codigo):
        print("Veiculo já cadastrado!")
        pausa()
    else:
        placa = input("placa do veiculo: ")
        tipo = input("tipo de veiculo: ")
        marca = input("marca: ")
        modelo = input("modelo: ")
        ano = input ("ano: ")
        portas = input ("Quantas portas: ")
        combustivel = input("combustivel: ")
        cor = input ("cor: ")
    
    dic[codigo] = (placa, tipo, marca, modelo, ano, portas, combustivel, cor)
    print("dados inseridos com sucesso!")
    pausa()

#Exibir veiculo

def exibir_veiculo(dic, chave):
    if existe_veiculo(dic, chave):
        dados = dic[chave]
        print()
        print(f"placa: {dados[0]}")
        print(f"tipo de veiculo: {dados[1]}")
        print(f"marca: {dados[2]}")
        print(f"modelo: {dados[3]}")
        print(f"ano: {dados[4]}")
        print(f"numero de portas: {dados[5]}")
        print(f"combustivel: {dados[6]}")
        print(f"cor: {dados[7]}")
    else:
        print("cadasto inexistente!")
        pausa()

#Alterar veiculo

def alterar_veiculo(dic, chave):
    if existe_veiculo(dic, chave):
        exibir_veiculo(dic, chave)
        confirmar = input("deseja alterar os dados? (S/N): ").upper()
        if confirmar == "S":
            print()
            placa = input("placa do veiculo: ")
            tipo = input("tipo de veiculo: ")
            marca = input("marca: ")
            modelo = input("modelo: ")
            ano = input("ano: ")
            portas = input("numero de portas: ")
            combustivel = input("combustivel: ")
            cor = input("cor: ")
            print()
            dic[codigo] = (placa, tipo, marca, modelo, ano, portas, combustivel, cor)  
            print("dados alterados com sucesso!")
            pausa()
        else:
            print("alteração cancelada.")
            pausa()
    else:
        print("cadastro inexistente!")
        pausa()

#remover veiculo

def remover_veiculos(dic, chave):
    if existe_veiculo(dic, chave):
        exibir_veiculo(dic, chave)
        confirma = input("deseja remover os dados? (S/N): ").upper()
        if confirma == "S":
            del dic[chave]
            pausa()
        else:
            print("remoção cancelada.")
    else:
        print("cadastro inexistente!")
        pausa()

#listar todos os veiculos

def exibir_todos_veiculos(dic):
    print("--"* 12)
    print("relatorios -> Veiculos")
    print()
    print("codigo - placa - tipo - marca - modelo - ano - portas - combustivel - cor")
    for codigo in dic:
        tupla = dic[codigo]
        string = codigo + " - " + tupla[0] + " - " + tupla[1] + " - " + tupla[2] + " - " + tupla[3] + " - " + tupla[4] + " - " + tupla[5] + " - " + tupla[6] + " - " + str(tupla[7])
        print(string)
    print()
    pausa()

#Gravar veiculos

def gravar_veiculos(dic):
    arq = open("veiculos.txt", "w")
    for codigo in dic:
        tupla = dic[codigo]
        linha = codigo + " ; " + tupla[0] + " ; " + tupla[1] + " ; " + tupla[2] + " ; " + tupla[3] + " ; " + tupla[4] + " ; " + tupla[5] + " ; " + tupla[6] + " ; " + str(tupla[7]) + "\n"
        arq.write(linha)
    arq.close()

#recuperar veiculos

def recuperar_veiculos(dic):
    if existe_arquivo("veiculos.txt"):
        arq = open("veiculos.txt", "r")
        for linha in arq:
            linha = linha[:len(linha)-1]
            lista = linha.split(";")
            codigo = lista[0]
            placa = lista[1]
            tipo = lista[2]
            marca = lista[3]
            modelo = lista[4]
            ano = lista[5]
            portas = lista[6]
            combustivel = lista[7]
            cor = lista[8]
            dic[codigo] = (placa, tipo, marca, modelo, ano, portas, combustivel, cor)

#menu Veiculos

def menu_veiculos(dic):
    c = 0 
    while c < 6:
        print("--" * 12)
        print("gerenciamento -> veiculos")
        print("--" * 12)
        print("1 - inserir")
        print("2 - alterar")
        print("3 - remover")
        print("4 - exibir veiculo")
        print("5 - exibir todos veiculos")
        print("6 - voltar para o menu")
        print("--" * 12)
        
        c = int(input("\nOpção: "))
        print()
        if c < 1 or c > 6:
            print("Opção Inválida")
        else:
            if c == 1:
                inserir_veiculos(dic)
            elif c == 2:
                codigo = input("Digite o Código para Alterar: ")
                alterar_veiculo(dic, codigo)
            elif c == 3:
                codigo = input("Digite o Código para Remover: ")
                remover_veiculos(dic, codigo)
            elif c == 4:
                codigo = input("Digite o Código para Exibir: ")
                exibir_veiculo(dic, codigo)
            elif c == 5:
                exibir_todos_veiculos(dic)
            elif c == 6:
                gravar_veiculos(dic)

'''
Consertos
'''

#biblioteca

from datetime import *
from auxiliares import *
from clientes import *
from imoveis import *

#existe conserto

def existe_conserto(dic, chave):
    if chave in dic.keys():
        return True
    else:
        return False

#inserir conserto

def inserir_conserto(dicC, dicE, dicK):
    CPF = input("digite seu CPF: ")
    if existe_conserto(dicC, CPF):
        placa = input("digite o placa do veiculo: ")
        if existe_conserto(dicE, placa):
            data_entrada = input("data de entrada: ")
            chave = (CPF, placa, data_entrada)
            if existe_conserto(dicK, chave):
                print("Conserto já existe")
                pausa()
            else:
               data_saida = input("data de saída: ")
               problemas = input("decrição do problema: ")
               valor = float(input("valor do conserto: "))
              
               dicK[chave] = [data_saida, problemas, valor]
               print("conserto inserido com sucesso!")
               pausa()
        else:
            print("CPF não existe")
            pausa()

#exibir

def exibir_conserto(dicC, dicE, dicK, CPF, placa, data_entrada):
    chave = (CPF, placa, data_entrada)
    if existe_conserto(dicK, chave):
        dados = dicK[chave]
        print("--" * 15)
        print("Dados - Consertos")
        print()
        # Dados Cliente
        print("--" * 15)
        print("Cliente: ")
        exibir_clientes(dicC, CPF)
        # Dados Veículo
        print("--" * 15)
        print("Veículo: ")
        exibir_veiculos(dicE, placa)
        # Dados Conserto
        print("--" * 15)
        print("Conserto: ")
        print()
        print(f"Data de Saída: {dados[0]}")
        print(f"Descrição dos Problemas: {dados[1]}")
        print(f"Valor do Conserto: R$ {dados[2]}")
        print()
    else:
        print("Este conserto não existe!")
        pausa()

# Alterar

def alterar_conserto(dicC, dicE, dicK, CPF, placa, data_entrada):
    chave = (CPF, placa, data_entrada)
    if existe_conserto(dicK, chave):
        exibir_conserto(dicC, dicE, dicK, CPF, placa, data_entrada)
        confirma = input("Deseja alterar? (S/N)").upper()
        if confirma == "S":
            data_saida = input("Data de Saída: ")
            problemas = input("Descrição dos Problemas: ")
            valor = float(input("Valor do Conserto: R$ "))
            dicK[chave] = (data_saida, problemas, valor)
            pausa()
        else:
            print("Operação cancelada!")
            pausa()
    else:
        print("Este conserto não existe!")
        pausa()

# Remover
 
def remover_conserto(dicC, dicE, dicK, CPF, placa, data_entrada):
    chave = (CPF, placa, data_entrada)
    if existe_conserto(dicK, chave):
        exibir_conserto(dicC, dicE, dicK, CPF, placa, data_entrada)
        confirma = input("Deseja remover? (S/N): ").upper()
        if confirma == "S":
            del dicK[chave]
            pausa()
        else:
            print("Operação cancelada!")
            pausa()
    else:
        print("Este conserto não existe!")
        pausa()

 # Exibir Todos
 
def exibir_todos_consertos(dicC, dicE, dicK):
    for chave in dicE:
        CPF = chave[0]
        placa = chave[1]
        data_entrada = chave[2]
        exibir_conserto(dicC, dicE, dicK, CPF, placa, data_entrada)
    print()
    pausa()

# Gravar
 
def grava_consertos(dic):
    arq = open("consertos.txt", "w")
    for chave in dic:
        CPF = chave[0]
        placa = chave[1]
        data_entrada = chave[2]
        tupla = dic[chave]
        data_saida = tupla[0]
        problemas = tupla[1]
        valor = tupla[2]
        linha = f"{CPF};{placa};{data_entrada};{data_saida};{problemas};{valor}\n"
        arq.write(linha)
    arq.close()

# Recuperar

def recupera_consertos(dic):
    if existe_arquivo("consertos.txt"):
        arq = open("consertos.txt", "r")
        for linha in arq:
            linha = linha.strip()
            lista = linha.split(";")
            CPF = lista[0]
            placa = lista[1]
            data_entrada = lista[2]
            data_saida = lista[3]
            problemas = lista[4]
            valor = float(lista[5])
            chave = (CPF, placa, data_entrada)
            dic[chave] = (data_saida, problemas, valor)
        arq.close()

 
# Menu - Consertos
 
def menu_consertos(dicC, dicE, dicK):
    c = 0
    while c < 6:
        print("--" * 15)
        print("Gerenciamento - Consertos")
        print("--" * 15)
        print("1 - Inserir")
        print("2 - Alterar")
        print("3 - Remover")
        print("4 - Exibir Conserto")
        print("5 - Exibir todos Consertos")
        print("6 - Voltar para o Menu")
        print("--" * 15)

        c = int(input("\nOpção: "))
        print()
        if c < 1 or c > 6:
            print("Opção Inválida")
            pausa()
        else:
            if c == 1:
                inserir_conserto(dicC, dicE, dicK)
            elif c == 2:
                CPF = input("Digite o CPF: ")
                placa = input("Digite a Placa: ")
                data_entrada = input("Digite a Data de Entrada: ")
                alterar_conserto(dicC, dicE, dicK, CPF, placa, data_entrada)
            elif c == 3:
                CPF = input("Digite o CPF: ")
                placa = input("Digite a Placa: ")
                data_entrada = input("Digite a Data de Entrada: ")
                remover_conserto(dicC, dicE, dicK, CPF, placa, data_entrada)
            elif c == 4:
                CPF = input("Digite o CPF: ")
                placa = input("Digite a Placa: ")
                data_entrada = input("Digite a Data de Entrada: ")
                exibir_conserto(dicC, dicE, dicK, CPF, placa, data_entrada)
            elif c == 5:
                exibir_todos_consertos(dicC, dicE, dicK)
            elif c == 6:
                grava_consertos(dicK)

# Relatório
 
def relatorio(dicC, dicE, dicK, X, Y):
    print(f"Relatório - Consertos com Data de Entrada entre {X} e {Y}.")
    print()
    for chave in dicK:
        data_entrada = chave[2]
        data_entrada_dt = datetime.strptime(data_entrada, '%d/%m/%Y')
        if len(X) > 4 and len(Y) > 4:
            xDate = datetime.strptime(X, '%d/%m/%Y')
            yDate = datetime.strptime(Y, '%d/%m/%Y')
            if data_entrada_dt >= xDate and data_entrada_dt <= yDate:
                CPF = chave[0]
                placa = chave[1]
                exibir_conserto(dicC, dicE, dicK, CPF, placa, data_entrada)
                print()
            else:
                print("Nenhum cadastro detectado nas datas informadas!")
                pausa()
        else:
            dataX = X
            dataY = Y
            anoX = datetime.strptime(dataX, '%Y')
            anoY = datetime.strptime(dataY, '%Y')
            if data_entrada_dt >= anoX and data_entrada_dt <= anoY:
                CPF = chave[0]
                placa = chave[1]
                exibir_conserto(dicC, dicE, dicK, CPF, placa, data_entrada)
                print()
            else:
                print("Nenhum cadastro detectado no intervalo informado!")
                pausa()
