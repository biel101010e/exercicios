def cadastrar_filmes(nome_filme, descricao, classificacao, categoria01, categoria02, categoria03):
    filmes = []
    filme = {
        "nome_filme": nome_filme,
        "descricao": descricao,
        "classificacao": classificacao,
        "categoria": [categoria01, categoria02, categoria03]
    }

    filmes.append(filme)
    return filmes

print(cadastrar_filmes ("velozes e furiosos", "filme de carros", 16, "crime", "aventura", "comedia"))













