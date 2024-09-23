def celsiusParaFahrenheit(celsius):
    return (celsius * 9/5) + 32

print("Tabela de conversão de Celsius para Fahrenheit:")
print("Celsius\tFahrenheit")

for celsius in range(0, 101, 10):
    fahrenheit = celsiusParaFahrenheit(celsius)
    print(f"{celsius}°C\t{fahrenheit:.1f}°F")