# Exercício 5: Faça um programa em que o usuário digita o raio de um círculo em m e o programa retorna no console a área do círculo em m² e o perímetro em m.


import math

raio = float(input("Digite o raio do círculo em metros: "))

area = math.pi * (raio ** 2)

perimetro = 2 * math.pi * raio

print(f"A área do círculo é {area:.2f} metros quadrados.")
print(f"O perímetro do círculo é {perimetro:.2f} metros.")