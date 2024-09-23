def calcularAreaRetangulo(largura, altura):
    return largura * altura

largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area = calcularAreaRetangulo(largura, altura)

print(f"A área do retângulo é: {area:.2f}")