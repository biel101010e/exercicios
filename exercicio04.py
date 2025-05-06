def  somar_e_calcular_media(numeros):
    if not numeros:
        print("a lista está vazia.")
        return
    
soma = sum(numeros)
media = soma / len(numeros)

print(f"soma:{soma}")
print(f"média {media}")

