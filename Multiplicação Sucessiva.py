a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))

resultado = 0

for _ in range(abs(b)):
    resultado += a

if b < 0:
    resultado = -resultado

print(f"O resultado de {a} x {b} é: {resultado}")