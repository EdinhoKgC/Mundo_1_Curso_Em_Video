import random

lista_alunos = []

for aluno in range(1,5):
    nome_aluno = input(f"Digite o nome do {aluno}º aluno para ordem de apresentação: ")
    lista_alunos.append(nome_aluno)
    
random.shuffle(lista_alunos)

print("=" * 40)
print("A ordem de apresentação dos alunos será:")
print("")
for i, aluno in enumerate(lista_alunos, start=1):
    print(f"{i}º - {aluno}")
    
print("=" * 40)