# Exercício 9: Usando o método random(), crie um programa que solicita ao usuário que adivinhe um número inteiro entre 1 e 10. Se o usuário digitar um número menor que 1 ou maior que 10, solicite que ele insira um número válido. Se o usuário digitar um número válido, verifique se o número que o usuário digitou é igual ao número gerado aleatoriamente pelo programa. Se o número for igual, imprima "Você acertou!". Caso contrário, imprima "Você errou!".

import random

numero_aleatorio = random.randint(1, 10)

while True:
    
    try:
        numero = int(input("Adivinhe um número entre 1 e 10: "))
        
        if 1 <= numero <= 10:
            break
        else:
            print("Por favor, insira um número válido entre 1 e 10.")
    except ValueError:
        print("Por favor, insira um número válido entre 1 e 10.")

if numero == numero_aleatorio:
    print("Você acertou!")
else:
    print(f"Você errou!")

