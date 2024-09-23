def fibonacci(n):
    sequencia = [0, 1] 
    for i in range(2, n):
        proximo = sequencia[i-1] + sequencia[i-2]
        sequencia.append(proximo)
    return sequencia[:n]  

n = int(input("Digite um número inteiro positivo: "))

if n > 0:
    resultado = fibonacci(n)
    print(f"Os primeiros {n} números da sequência de Fibonacci são: {resultado}")
else:
    print("Por favor, insira um número inteiro positivo.")