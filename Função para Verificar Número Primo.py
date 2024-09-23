def numeroPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um número: "))

if numeroPrimo(numero):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
