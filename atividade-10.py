# Exercício 10: Faça um programa que solicita ao usuário escrever um texto e conta quantas vezes a letra "a" aparece no texto.

def contador_de_a():
    texto = input("Digite seu nome completo: ")
    return f'As letras "a" aparecem {texto.count("a")} vezes na frase'
print(contador_de_a())