def checarIdade(age):
    age = int(input("Digite sua idade!"))
    if age <= 0:
        print("Insira uma idade válida!")
    elif age <= 18:
        print("Menor de idade!")
    else:
        print("Maior de idade!")
        


def calcularImc(peso, altura):
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = peso / (altura ** 2)

    print(f"Seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif imc < 25:
        print("Classificação: Peso normal")
    elif imc < 30:
        print("Classificação: Sobrepeso")
    else:
        print("Classificação: Obeso")
        
def converterTemperatura():
    temperatura = float(input("Digite a temperatura: "))
    origem = input("De qual unidade? (C, F ou K): ").upper()
    destino = input("Para qual unidade? (C, F ou K): ").upper()

    if origem == "C":
        celsius = temperatura
    elif origem == "F":
        celsius = (temperatura - 32) * 5 / 9
    elif origem == "K":
        celsius = temperatura - 273.15
    else:
        print("Unidade de origem inválida!")


    if destino == "C":
        resultado = celsius
    elif destino == "F":
        resultado = celsius * 9 / 5 + 32
    elif destino == "K":
        resultado = celsius + 273.15
    else:
        print("Unidade de destino inválida!")
        return

    print(f"Resultado: {resultado:.2f} {destino}")
    
    