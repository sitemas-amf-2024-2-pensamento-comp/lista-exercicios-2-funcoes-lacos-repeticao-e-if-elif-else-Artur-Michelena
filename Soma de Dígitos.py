def somaDigitos(n):
    soma = 0
    while n > 0:
        soma += n % 10  
        n = n // 10     
    return soma

n = int(input("Digite um número inteiro positivo: "))

if n >= 0:
    resultado = somaDigitos(n)
    print(f"A soma dos dígitos de {n} é: {resultado}")
else:
    print("Por favor, insira um número inteiro positivo.")