# Inicializa variáveis
somaNotas = 0
quantidadeNotas = 0

print("Digite as notas: ")

print("Digite -1 para encerrar.")
while True:
    nota = float(input("Digite uma nota: "))

    if nota == -1:
        break  

    somaNotas += nota
    quantidadeNotas += 1

if quantidadeNotas > 0:
    media = somaNotas / quantidadeNotas
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")