import json
import os 
funcio = "funcionarios.json"

def carregar_dados():
    if os.path.exists(funcio):
        with open(funcio, "r", encoding= "utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return[]
    
funcionarios = carregar_dados()

for funcionario in funcionarios:
    print(f"nome: {funcionario["nome"]} salario: {funcionario["salario"]}")
    



    







