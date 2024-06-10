def calcular_imc():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = peso / (altura ** 2)
    print("Seu IMC é: {:.2f}".format(imc))

calcular_imc()
