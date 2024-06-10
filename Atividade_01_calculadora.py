import os
def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida"
    else:
        return x / y
    
while True:
    print("\nMenu de Opções:")
    print("1. SOMA")
    print("2. SUBTRAÇÃO")
    print("3. MULTIPLICAÇÃO")
    print("4. DIVISÃO")
    print("5. Sair")
    
    escolha = input("\nEscolha uma operação de 1 a 5. ")
    
    if escolha == '5':
        print("Obrigado por participar até logo...")
        break

    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = somar(num1, num2)
        print("O resultado é: ", resultado)
        
    elif escolha == '2':
        resultado = subtrair(num1, num2)
        print("O resultado é: ", resultado)
    elif escolha == '3':
        resultado = multiplicar(num1, num2)
        print("O resultado é: ", resultado)
    elif escolha == '4':
        resultado = dividir(num1, num2)
        print("O resultado é: ", resultado)
    else:
        print("Entrada inválida. Por favor, escolha um número de 1 a 5.")
        
