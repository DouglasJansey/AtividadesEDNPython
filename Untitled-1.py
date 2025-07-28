def checarIdade():
    age = int(input("Digite sua idade!"))
    if age <= 0:
        print("Insira uma idade válida!")
    elif age <= 18:
        print("Menor de idade!")
    else:
        print("Maior de idade!")
        


def calcularImc():
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
    
def verificarBissexto():
    ano = int(input("Digite um ano: "))

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano} é um ano BISSEXTO.")
    else:
        print(f"{ano} NÃO é um ano bissexto.")
        
        
def conversorMoeda():
    reais = float(input("Digite o valor em reais (R$): ").replace(",", "."))
    taxa_dolar = 5.20
    taxa_euro = 6.15

    dolares = reais / taxa_dolar
    euros = reais / taxa_euro

    print(f"Valor em reais: R$ {reais:.2f}")
    print(f"Valor em dólares: US$ {dolares:.2f}")
    print(f"Valor em euros: € {euros:.2f}")
    print()

def calculadoraDesconto():
    produto = input("Digite o nome do produto: ")
    preco_original = float(input("Digite o preço original (R$): ").replace(",", "."))
    desconto_pct = float(input("Digite a porcentagem de desconto (%): ").replace(",", "."))

    valor_desconto = preco_original * (desconto_pct / 100)
    preco_final = preco_original - valor_desconto

    print(f"Produto: {produto}")
    print(f"Preço original: R$ {preco_original:.2f}")
    print(f"Desconto: {desconto_pct:.2f}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Preço final com desconto: R$ {preco_final:.2f}")
    print()
        
def calculadoraMedia():
    nota1 = float(input("Digite a nota 1: ").replace(",", "."))
    nota2 = float(input("Digite a nota 2: ").replace(",", "."))
    nota3 = float(input("Digite a nota 3: ").replace(",", "."))

    media = (nota1 + nota2 + nota3) / 3


    print(f"Nota 1: {nota1:.2f}")
    print(f"Nota 2: {nota2:.2f}")
    print(f"Nota 3: {nota3:.2f}")
    print(f"Média final: {media:.2f}")
    print()

def calculadoraConsumoDistancia():
    distancia = float(input("Digite a distância percorrida (km): ").replace(",", "."))
    combustivel = float(input("Digite o combustível gasto (litros): ").replace(",", "."))

    consumo_medio = distancia / combustivel


    print(f"Distância percorrida: {distancia:.2f} km")
    print(f"Combustível gasto: {combustivel:.2f} litros")
    print(f"Consumo médio: {consumo_medio:.2f} km/l")
    print()
    
def menu():
    while True:
        print("\nMenu:")
        print("1. Checar Idade")
        print("2. Calcular IMC")
        print("3. Converter Temperatura")
        print("4. Verificar Ano Bissexto")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            checarIdade()
        elif opcao == "2":
            calcularImc()
        elif opcao == "3":
            converterTemperatura()
        elif opcao == "4":
            verificarBissexto()
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")
menu()
