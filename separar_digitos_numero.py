numero = int(input("Digite um número inteiro entre 0 e 9999: "))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print(f"O numero digitado é: {numero}")
print(f"A unidade é: {unidade}")
print(f"A dezena é: {dezena}")
print(f"A centena é: {centena}")
print(f"O milhar é: {milhar}")