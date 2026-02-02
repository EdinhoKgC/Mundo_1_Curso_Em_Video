nome_completo = str(input("Digite seu nome completo: ")).strip()

primeiro_nome = nome_completo.split()[0]

print("Seu nome completo em maiúsculas é: ", nome_completo.upper())

print("Seu nome completo em minúsculas é: ", nome_completo.lower())

print("Seu nome completo tem {} Letras.".format(len(nome_completo) - nome_completo.count(" ")))

print("Seu primeiro nome é {} e ele tem {} letras.".format(primeiro_nome, len(primeiro_nome)))