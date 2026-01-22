import math

angulo = int(input("digite o ângulo em graus: "))

seno = math.sin(math.radians(angulo))
cosceno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print ("=" * 60)
print(" " * 10 + "CÁLCULO DE SENO, COSSENO E TANGENTE :")
print("")

print(" " * 15 + f"O seno de {angulo}° é: {seno:.2f}")
print(" " * 15 + f"O cosseno de {angulo}° é: {cosceno:.2f}")
print(" " * 15 + f"A tangente de {angulo}° é: {tangente:.2f}")
print("=" * 60)