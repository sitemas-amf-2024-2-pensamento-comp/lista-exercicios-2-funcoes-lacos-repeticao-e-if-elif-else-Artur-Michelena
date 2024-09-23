def converterFahrenheit(celsius):
    return (celsius * 9/5) + 32

while True:
    celsius = float(input("Digite uma temperatura em Celsius (ou -999 para sair): "))
    
    if celsius == -999:
        break

    fahrenheit = converterFahrenheit(celsius)
    print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F")
