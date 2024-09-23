def calcularFatorial(n):
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i
    return fatorial

n = int(input("Digite um número inteiro positivo: "))

if n >= 0:
    resultado = calcularFatorial(n)
    print(f"O fatorial de {n} é: {resultado}")
else:
    print("Por favor, insira um número inteiro positivo.")