# Exercício 6: Faça um programa que solicita o ano de nascimento do usuário e retorna o seu signo no horóscopo chinês.

def calcular_signos_chines(ano_mascimento):
    signo_chineses = ["Rato", "Búfalo", "Tigre","Coelho","Dragão","Cavalo","Serpente","Cabra","Galo","Javali"]
    ano_base = 1900
    indice_signo = (ano_mascimento - ano_base) % 12
    return signo_chineses[indice_signo]
ano_nascimento = int(input("Digite o ano de seu nascimento:"))
signo = calcular_signos_chines(ano_nascimento)
print(f"Seu signo em chinês é {signo}")