# Exercício 2: Faça uma função que recebe um número e imprime no console se ele é múltiplo de 5 e de 3 ou False caso contrário.

def multiplo_de_5_e_3(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return True
    else:
        return False
numero = int(input("Digite um numero interio:"))
if multiplo_de_5_e_3(numero):
    print(f"O numero {numero} é multiplo de 5 e de 3.")
else:
    print(multiplo_de_5_e_3(numero))