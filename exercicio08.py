import json
import os

data = "data.json"

def carregar_dados():
    if os.path.exists(data):
        with open(data, "r", encoding="utf-8", ) as arc_json:
            return json.load(arc_json)
    else:
        return []
    


clientes = carregar_dados()

for cliente in clientes:
    print(cliente["nome_completo"])













