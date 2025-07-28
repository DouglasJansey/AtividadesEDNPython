def checkAge(age):
    age = int(input("Digite sua idade!"))
    if age <= 0:
        print("Insira uma idade válida!")
    elif age <= 18:
        print("Menor de idade!")
    else:
        print("Maior de idade!")
        


def calcImc(peso, altura):
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
        
