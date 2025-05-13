from exercicio04 import somar_notas

alunos = []

def obter_dados_aluno():
    nome_aluno = input("Informe o nome do completo do aluno: ")
    email_aluno = input("Informe o email completo do aluno: ")
    serie_aluno = input("Informe a serie do aluno: ")
    nota01 = int(input("digite a nota01 do aluno: "))
    nota02 = int(input("digite a nota02 do aluno: "))
    nota03 = int(input("digite a nota03 do aluno: "))

    return cadastrar_aluno(nome_aluno, email_aluno, serie_aluno, nota01, nota02, nota03)

    


def cadastrar_aluno(nome, email, serie, nota01=0, nota02=0, nota03=0):

    notas = [nota01, nota02, nota03]

    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
        "nota": notas,
        "media": somar_notas(notas)
    }

    alunos.append(aluno)
    media = somar_notas(aluno["nota"])
    return alunos
    

obter_dados_aluno()

def mostrar_dados_alunos(dados_alunos):
    for aluno in dados_alunos:
        print(f"nome do aluno: {aluno["nome"]}")
    return print(dados_alunos)

mostrar_dados_alunos(alunos)
