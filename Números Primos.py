def numeoPrimo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0:
            return False
    return True
n = int(input("Digite um número inteiro positivo: "))

if n > 0:
    if numeoPrimo(n):
        print(f"{n} é um número primo.")
    else:
        print(f"{n} não é um número primo.")
else:
    print("Por favor, insira um número inteiro positivo.")
