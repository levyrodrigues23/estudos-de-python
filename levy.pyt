# Simulação de banco de dados com listas de dicionários
veiculos = []
clientes = []
vendedores = []
vendas = []

# Funções CRUD para veículos
def cadastrar_veiculo():
    id_veiculo = len(veiculos) + 1
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    ano = input("Digite o ano do veículo: ")
    cor = input("Digite a cor do veículo: ")
    preco = float(input("Digite o preço do veículo: "))
    status = "disponível"
    
    veiculo = {
        "ID": id_veiculo,
        "Marca": marca,
        "Modelo": modelo,
        "Ano": ano,
        "Cor": cor,
        "Preço": preco,
        "Status": status
    }
    
    veiculos.append(veiculo)
    print(f"Veículo {modelo} cadastrado com sucesso!")

def listar_veiculos():
    if len(veiculos) == 0:
        print("Nenhum veículo cadastrado.")
    else:
        for veiculo in veiculos:
            print(veiculo)

def atualizar_veiculo(id_veiculo):
    for veiculo in veiculos:
        if veiculo['ID'] == id_veiculo:
            veiculo['Marca'] = input("Digite a nova marca do veículo: ")
            veiculo['Modelo'] = input("Digite o novo modelo do veículo: ")
            veiculo['Ano'] = input("Digite o novo ano do veículo: ")
            veiculo['Cor'] = input("Digite a nova cor do veículo: ")
            veiculo['Preço'] = float(input("Digite o novo preço do veículo: "))
            veiculo['Status'] = input("Digite o novo status (disponível/vendido): ")
            print(f"Veículo ID {id_veiculo} atualizado com sucesso!")
            return
    print(f"Veículo com ID {id_veiculo} não encontrado.")

def excluir_veiculo(id_veiculo):
    global veiculos
    veiculos = [veiculo for veiculo in veiculos if veiculo['ID'] != id_veiculo]
    print(f"Veículo com ID {id_veiculo} excluído com sucesso!")

# Funções CRUD para clientes
def cadastrar_cliente():
    id_cliente = len(clientes) + 1
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    email = input("Digite o email do cliente: ")
    
    cliente = {
        "ID": id_cliente,
        "Nome": nome,
        "CPF": cpf,
        "Telefone": telefone,
        "Endereço": endereco,
        "Email": email
    }
    
    clientes.append(cliente)
    print(f"Cliente {nome} cadastrado com sucesso!")

def listar_clientes():
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes:
            print(cliente)

def atualizar_cliente(id_cliente):
    for cliente in clientes:
        if cliente['ID'] == id_cliente:
            cliente['Nome'] = input("Digite o novo nome do cliente: ")
            cliente['CPF'] = input("Digite o novo CPF do cliente: ")
            cliente['Telefone'] = input("Digite o novo telefone do cliente: ")
            cliente['Endereço'] = input("Digite o novo endereço do cliente: ")
            cliente['Email'] = input("Digite o novo email do cliente: ")
            print(f"Cliente ID {id_cliente} atualizado com sucesso!")
            return
    print(f"Cliente com ID {id_cliente} não encontrado.")

def excluir_cliente(id_cliente):
    global clientes
    clientes = [cliente for cliente in clientes if cliente['ID'] != id_cliente]
    print(f"Cliente com ID {id_cliente} excluído com sucesso!")

# Menu para interação com o sistema
def menu():
    while True:
        print("\nSistema de Concessionária - CRUD")
        print("1. Cadastrar Veículo")
        print("2. Listar Veículos")
        print("3. Atualizar Veículo")
        print("4. Excluir Veículo")
        print("5. Cadastrar Cliente")
        print("6. Listar Clientes")
        print("7. Atualizar Cliente")
        print("8. Excluir Cliente")
        print("9. Sair")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            cadastrar_veiculo()
        elif opcao == 2:
            listar_veiculos()
        elif opcao == 3:
            id_veiculo = int(input("Digite o ID do veículo a ser atualizado: "))
            atualizar_veiculo(id_veiculo)
        elif opcao == 4:
            id_veiculo = int(input("Digite o ID do veículo a ser excluído: "))
            excluir_veiculo(id_veiculo)
        elif opcao == 5:
            cadastrar_cliente()
        elif opcao == 6:
            listar_clientes()
        elif opcao == 7:
            id_cliente = int(input("Digite o ID do cliente a ser atualizado: "))
            atualizar_cliente(id_cliente)
        elif opcao == 8:
            id_cliente = int(input("Digite o ID do cliente a ser excluído: "))
            excluir_cliente(id_cliente)
        elif opcao == 9:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

# Executando o menu
menu()
