def somaDivindoPor3 (a, b):
    soma = 0
    for i in range(a, b + 1):
        if i % 3 == 0:
            soma += i
    return soma

a = int(input("Digite o primeiro número inteiro positivo: "))
b = int(input("Digite o segundo número inteiro positivo: "))

if a > 0 and b > 0 and a <= b:
    resultado = somaDivindoPor3(a, b)
    print(f"A soma dos números divisíveis por 3 entre {a} e {b} é: {resultado}")
else:
    print("Por favor, insira números inteiros positivos, e A deve ser menor ou igual a B.")