import json 
import os

barbeiro = "agenda_barbearia.json"

def carregar_dados():
    if os.path.exists(barbeiro):
        with open(barbeiro, "r", encoding="utf-8" )as arq_json:
            return json.load(arq_json)
    else:
        return[]
    

def obter_dados():
    nome_cliente = input("digite o seu nome por favor")
    serviço_cliente = input("digite o serviço que você deseja fazer")
    data_cliente = (input("digite o data que você deseja"))
    horario_cliente = (input("digite o horario que você deseja"))
    observação_cliente = input("digite alguma observação que você deseja fazer")

    data_cliente = {
        "nome_cliente": nome_cliente,
        "serviço_cliente": serviço_cliente,
        "data_cliente": data_cliente,
        "horario_cliente": horario_cliente,
    }

    return data_cliente

def agenda_barbeiro(cadastrar_clientes):
    db_barbeiro = carregar_dados()
    db_barbeiro.append(cadastrar_clientes)

    with open(barbeiro, "w", encoding="utf-8") as arq_json:
        json.dump(db_barbeiro, arq_json, indent=4, ensure_ascii=False)

def mostrar_agenda(clientes):
    if clientes:
        for cliente in clientes:
            print(f"""
                nome do cliente{barbeiro["nome_cliente"]}
                serviço do cliente{barbeiro["nome_cliente"]}
                data do cliente{barbeiro["nome_cliente"]}
                horario do cliente{barbeiro["nome_cliente"]}
                observação do cliente{barbeiro["nome_cliente"]}
 """ )
    else:
        print("nenhum agendamento")

def iniciar_sistema():
    db_barbeiro = carregar_dados()

    while True:
        print("")
        print("="*80)
        print("opção 1 - serviços agendados ")
        print("opção 2 - agendamentos ")
        print("opçãp 3 - sair do sistema")
        print("="*80)

        opcao = input("escolha uma das opções do menu:")

        if opcao == "1":
            mostrar_agenda(db_barbeiro)
        elif opcao == "2":
            agenda_barbeiro(obter_dados())
        elif opcao == "3":
            print("sistema finalizado!!!")
            break
        else:
            print("opção invalida, escolha uma das opções do menu.")

iniciar_sistema()

        







