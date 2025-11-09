resposta = input("Você quer converter Dolar para Real? (s/n) ")
if resposta == 's':
    Dolar = int(input("digite o valor em dolares: "))
    cotacao = int(input("digite a cotação do dolar: "))

    real = Dolar * cotacao

    print(f"O valor em reais é: {real}")
else:
    real = int(input("digite o valor em reais: "))
    cotacao = int(input("digite a cotação do dolar: "))
    dolar = real / cotacao
    print(f"O valor em dolares é: {dolar}")
