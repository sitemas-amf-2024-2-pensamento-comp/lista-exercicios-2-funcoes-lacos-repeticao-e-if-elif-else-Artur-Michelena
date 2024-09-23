def divisores(n):
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs

n = int(input("Digite um número inteiro positivo: "))

if n > 0:
    resultado = divisores(n)
    print(f"Os divisores de {n} são: {resultado}")
else:
    print("Por favor, insira um número inteiro positivo.")