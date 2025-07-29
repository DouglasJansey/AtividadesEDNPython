
def saudacao():
    print("Olá, mundo!")


def calculadoraSoma():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    soma = numero1 + numero2
    print(f"Soma de {numero1} + {numero2} = {soma}")


def calculadoraVolume():
    comprimento = float(input("Digite o comprimento da caixa (cm): ").replace(",", "."))
    largura = float(input("Digite a largura da caixa (cm): ").replace(",", "."))
    altura = float(input("Digite a altura da caixa (cm): ").replace(",", "."))
    volume = comprimento * largura * altura
    print(f"Volume da caixa: {volume} cm³")

def calculadoraPrecoTotal():
    produto = input("Digite o nome do produto: ")
    precoUnitario = float(input("Digite o preço unitário (R$): ").replace(",", "."))
    quantidade = int(input("Digite a quantidade: "))
    precoTotal = precoUnitario * quantidade

    print(f"Produto: {produto}")
    print(f"Preço unitário: R$ {precoUnitario:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço total: R$ {precoTotal:.2f}")

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
    
def calculadora():
    def soma(value1, value2):
        result = value1 + value2
        return print(f"Resultado da soma: {result}")
    def subtracao(value1, value2):
        result = value1 - value2
        return print(f"Resultado da subtração: {result}")
    def multiplicacao(value1, value2):
        result = value1 * value2
        return print(f"Resultado da multiplicação: {result}")
    def divisao(value1, value2):
        try:
            result = value1 / value2
            print("Resultado da divisão: ", result)
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida.")
            return
        

    while True:
        print("Bem-vindo à Calculadora!")
        print("Escolha uma das opções abaixo para realizar um cálculo:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
         
        if opcao in ["1", "2", "3", "4"]:
            try:
                valor1 = float(input("Digite o primeiro valor: "))
                valor2 = float(input("Digite o segundo valor: "))
            except ValueError:
                print("Erro: Digite apenas números válidos.")
                continue
            
        if opcao == "0":
            print("Saindo da calculadora...")
            break         
        elif opcao == "1":
                soma(valor1, valor2)      
        elif opcao == "2":
                subtracao(valor1, valor2)
        elif opcao == "3":
                multiplicacao(valor1, valor2)
        elif opcao == "4":
                divisao(valor1, valor2)
        else:
                print("Opção inválida! Tente novamente.")
  
def verificarSenha():
    senha = input("Digite uma senha: ")

    if len(senha) < 8:
        print("Senha fraca: deve ter pelo menos 8 caracteres.")
        return

    temNumero = False
    for caractere in senha:
        if caractere.isdigit():
            temNumero = True
            break

    if not temNumero:
        print("Senha fraca: deve conter pelo menos um número.")
    else:
        print("Senha forte!")   
        
def classificarNumeros():
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número (ou 'sair' para encerrar): ")

        if entrada.lower() == "sair":
            break

        if not entrada.isdigit():
            print("Por favor, digite apenas números inteiros.")
            continue

        numero = int(entrada)

        if numero % 2 == 0:
            print(f"{numero} é par.")
            pares += 1
        else:
            print(f"{numero} é ímpar.")
            impares += 1

    print("\nResumo:")
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")
    
def calcularMediaTurma():
    notas = []

    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
        
        if nome.lower() == "sair":
            break

        notaTexto = input(f"Digite a nota do aluno {nome}: ")

        if notaTexto.replace('.', '').isdigit():
            nota = float(notaTexto)
            notas.append(nota) 
        else:
            print("Nota inválida! Digite um número.")
    
    if len(notas) > 0:
        soma = sum(notas)  
        media = soma / len(notas)  
        print(f"\nA média da turma é: {media:.2f}")
    else:
        print("Nenhuma nota foi registrada.")      
              
def menu():
    while True:
        print("\nMenu:")
        print("1. Checar Idade")
        print("2. Calculadora de Soma")
        print("3. Calculadora de Volume")
        print("4. Calculadora de Preço Total")
        print("5. Calcular IMC")
        print("6. Converter Temperatura")
        print("7. Verificar Ano Bissexto")
        print("8. Cconversor de Moeda")
        print("9. Calculadora de Desconto")
        print("10. Calculadora de Média")
        print("11. Calculadora de Consumo de Distância")
        print("12. Calculadora")
        print("13. Verificador de senha")
        print("14. Verificar números pares e ímpares")
        print("15. Calcular média da turma")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            checarIdade()
        elif opcao == "2":
            calculadoraSoma()
        elif opcao == "3":
            calculadoraVolume()
        elif opcao == "4":
            calculadoraPrecoTotal()
        elif opcao == "5":
            calcularImc()
        elif opcao == "6":
            converterTemperatura()
        elif opcao == "7":
            verificarBissexto()
        elif opcao == "8":
            conversorMoeda()
        elif opcao == "9":
            calculadoraDesconto()
        elif opcao == "10":
            calculadoraMedia()
        elif opcao == "11":
            calculadoraConsumoDistancia()
        elif opcao == "12":
            calculadora()
        elif opcao == "13":
            verificarSenha()
        elif opcao == "14":
            classificarNumeros()
        elif opcao == "15":
            calcularMediaTurma()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")
menu()