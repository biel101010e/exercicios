clientes = []

def obter_dados_dos_clientes():
    nome_cliente = input("informe seu nome completo")
    CPF_cliente = int(input("digite seu CPF"))
    RG_cliente = int(input("digite seu RG"))
    nascimento_cliente = float(input("informe sua data de nascimento"))
    endereco_cliente = input("digite seu endereço")
    cidade_cliente = input("informe sua cidade")
    estado_cliente = input("informe seu estado")
    telefone_cliente = int(input("digite seu telefone"))
    celular_cliente = int("digite seu celular")
    email_cliente = input("digite seu email")

    cliente = {
        "nome_cliente": nome_cliente,
        "CPF_cliente": CPF_cliente,
        "RG_cliente": RG_cliente,
        "nascimento_cliente": nascimento_cliente,
        "endereco_cliente": endereco_cliente,
        "cidade_cliente": cidade_cliente,
        "estado_cliente": estado_cliente,
        "telefone_cliente": telefone_cliente,
        "celular_cliente": celular_cliente,
        "email_cliente": email_cliente,
    }

    return cliente

def cadastrar_cliente(dados_cliente):
    clientes.append(dados_cliente)

    return clientes

def mostrar_dados_clientes(dados_clientes):
    for cliente in dados_clientes:
        print(f"""
              nome do cliente: {cliente["nome_cliente"]}")
              CPF do cliente: {cliente["CPF_cliente"]}")
              RG do cliente: {cliente["RG_cliente"]}")
               data de nascimento do cliente: {cliente["nascimento_cliente"]}")
              endereço do cliente: {cliente["endereço_cliente"]}")
              cidade do cliente: {cliente["cidade_cliente"]}")
              estado do cliente: {cliente["estado_cliente"]}")
             telefone do cliente: {cliente["telefone_cliente"]}")
              celular do cliente: {cliente["celular_cliente"]}")
              email do cliente: {cliente["email_cliente"]}")
""" )
        
def iniciar_sistema():
    while True:
        print("")
        print("="*80)
        print("opção 1 - mostrar lista de clientes")
        print("opção 2 - cadastrar clientes")
        print("opção 3 - sair do sistema")

        opcao = input("escolha uma das opções do menu: ")

        if opcao == "1":
            mostrar_dados_clientes(clientes)
        elif opcao ==  "2":
            cadastrar_cliente(obter_dados_dos_clientes())
        elif opcao == "3":
            print("sistema finalizado!")
            break
        else:
            print("opção invalida, escolha uma das opções do menu.")

iniciar_sistema()












































