# Exercicio 4: Faça um programa que solicita ao usuário escrever o nome das frutas que ele deseja comprar. O usuário deve digitar as frutas até digitar a palavra "sair". O programa deve imprimir na tela a lista de frutas que o usuário deseja comprar.


lista=[]
while True:
    frutas = input("""Escreva a fruta que voce deseja ou digite "sair":""")
    if frutas == "sair":
        print(lista)
        break
    lista.append(frutas)
    print(lista)