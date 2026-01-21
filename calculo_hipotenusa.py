import math

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))

cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5

print("=" * 60)
print(" " * 15 + "CÁLCULO DA HIPOTENUSA SEM MATH :")
print("")
print(" " * 10 + f"A hipotenusa do triângulo retângulo é: {hipotenusa:.2f}")
print("=" * 60)

print("")
print("")

print("=" * 60)
print(" " * 15 + "CÁLCULO DA HIPOTENUSA COM MATH :")
print("")

hipotenusa_math = math.hypot(cateto_oposto, cateto_adjacente)
print(" " * 10 + f"A hipotenusa do triângulo retângulo é: {hipotenusa_math:.2f}")
print("=" * 60)