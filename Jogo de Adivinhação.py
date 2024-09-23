import random

numeroSorteado = random.randint(1, 100)

tentativa = None

print("Bem-vindo ao jogo de adivinhação! Tente adivinhar o número entre 1 e 100.")

while tentativa != numeroSorteado:
    tentativa = int(input("Digite sua tentativa: "))

    if tentativa < numeroSorteado:
        print("Tente um número maior.")
    elif tentativa > numeroSorteado:
        print("Tente um número menor.")
    else:
        print("Parabéns! Você acertou o número.")