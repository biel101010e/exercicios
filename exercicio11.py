import json
import os

carros = 'cadastro_carros.json'

def cadastrar_dados():
    if os.path.exists(carros):
        with open(carros, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return[]
    
def obter_dados():
    modelo_carro = input("digite o modelo do carro:")
    marca_carro = input("digite o modelo do carro:")
    cor_carro = input("digite o modelo do carro:")
    ano_carro = int("digite o modelo do carro:")

    data_carro = {
        "modelo_carro": modelo_carro,
        "marca_carro": marca_carro,
        "cor_carro": cor_carro,
        "ano_carro": ano_carro,
    }

    return data_carro

def cadastrar_carros(receber_carro):
    db_carros = cadastrar_dados()
    db_carros.append(receber_carro)

    with open(carros, "w", encoding="utf-8")as arq_json:
        json.dump(db_carros, arq_json, indent=4, ensure_ascii=False)

def mostrar_carros(carros):
    if carros:
        for carro in carros:
            print(f"""
              modelo do carro{carro["modelo_carro"]}
              marca carro{carro["marca_carro"]}
              cor do carro{carro["cor_carro"]}
             ano do carro{carro["ano_carro"]}
             """ )
    else:
        print("nenhum veiculo cadastrado no momento.")


def iniciar_sistema():
    db_carro = cadastrar_dados()

    while True:
        print("")
        print("="*80)
        print("opção 1 - mostrar lista de carros ")
        print("opção 2 - cadastrar carro ")
        print("sair do sistema")
        print("="*80)

        opcao = input("escolha uma das opções do menu")

        if opcao == "1":
            mostrar_carros(db_carro)
        elif opcao == "2":
            cadastrar_carros(obter_dados())
        elif opcao == "3":
            print("sistema finalizado!!!")
            break
        else:
            print("opção invalida, escolha uma das opções do menu.")

iniciar_sistema()






         

    


            





    

    







   





