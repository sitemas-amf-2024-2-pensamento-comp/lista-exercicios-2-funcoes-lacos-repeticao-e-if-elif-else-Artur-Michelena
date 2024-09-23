salario = float(input("Digite o seu salário mensal: "))
valor_emprestimo = float(input("Digite o valor do empréstimo: "))
taxaJuros = float(input("Digite a taxa de juros mensal (em %): "))
num_meses = int(input("Digite o número de meses para pagar: "))

taxaJuros /= 100

prestacao = valor_emprestimo * (taxaJuros * (1 + taxaJuros) ** num_meses) / ((1 + taxaJuros) ** num_meses - 1)

limite_salario = 0.3 * salario

print(f"O valor da prestação mensal será: R${prestacao:.2f}")

if prestacao > limite_salario:
    print("Empréstimo não aprovado. O valor da prestação excede 30% do seu salário.")
else:
    print("Empréstimo aprovado!")