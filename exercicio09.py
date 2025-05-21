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
    if funcionario["salario"]>5500:
        print(f"nome: {funcionario["nome"]} salario: {funcionario["salario"]}")
    



    







