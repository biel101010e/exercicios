from exercicio04 import somar_e_calcular_media

def cadastrar_aluno(nome, email, serie, nota01, nota02, nota03):
    alunos = []
    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
        "nota": [nota01, nota02, nota03]
    }
    
    alunos.append(aluno)
    return alunos

print(cadastrar_aluno ("capixaba", "gabriel08@gmail.com", "2° TB", 8, 9, 5))