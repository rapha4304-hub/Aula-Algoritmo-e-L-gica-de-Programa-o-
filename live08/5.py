alunos = [
    {"Nome": "Raphael", "Nota": 8},
    {"Nome": "Luana", "Nota": 9}]

for aluno in alunos:
    if aluno["Nota"] >= 5:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    print(f"{aluno["Nome"]} está {situacao}")
