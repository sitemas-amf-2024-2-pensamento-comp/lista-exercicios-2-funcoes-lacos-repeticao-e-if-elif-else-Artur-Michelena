def contarVogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for caractere in texto:
        if caractere in vogais:
            contador += 1
    return contador

frase = input("Digite uma frase: ")

numeroVogais = contarVogais(frase)
print(f"O número de vogais na frase é: {numeroVogais}")