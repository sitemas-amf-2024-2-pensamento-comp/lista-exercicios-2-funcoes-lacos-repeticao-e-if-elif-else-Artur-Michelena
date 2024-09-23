def contarParesimpares(n):
    pares = []
    impares = []
    
    for i in range(1, n+1):
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    
    return pares, impares

n = int(input("Digite um número inteiro positivo: "))

if n > 0:
    pares, impares = contarParesimpares(n)
    print("Números pares:", pares)
    print("Números ímpares:", impares)
else:
    print("Por favor, insira um número inteiro positivo.")
