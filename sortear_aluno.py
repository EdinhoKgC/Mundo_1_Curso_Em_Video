import random

lista_alunos = []

for alunos in range(1,5):
    nome_aluno = input(f"Digite o nome do {alunos}º aluno: ")
    
    lista_alunos.append(nome_aluno)
    
aluno_sorteado = random.choice(lista_alunos)
print(f"O aluno sorteado foi: {aluno_sorteado}")