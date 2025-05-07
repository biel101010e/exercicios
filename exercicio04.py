def  somar_e_calcular_media(lista):
    total = 0 
    for i in lista:
        total += i
    media = total/len(lista)
    return total


print(somar_e_calcular_media())


