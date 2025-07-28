age = int(input("Digite sua idade!"))
def checkAge(age):
    if age <= 0:
        print("Insira uma idade válida!")
    elif age <= 18:
        print("Menor de idade!")
    else:
        print("Maior de idade!")
        
checkAge(age)

