from math import floor

n1 = str(input("Digite um número real: "))

if ',' in n1:
    n1 = n1.replace(',','.')
    
n1 = float(n1)

print(f"A parte inteira do número {n1} é {floor(n1)}")