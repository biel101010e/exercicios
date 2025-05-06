def cadastrar_aluno(nome, email, serie):
    alunos = []
    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie
    }
    
    alunos.append(aluno)
    return alunos

print(cadastrar_aluno ("capixaba", "gabriel08@gmail.com", "2° TB"))