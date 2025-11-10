print("Bem-vindo a calculadora fácil")

opcao = ""
while opcao != "0":
    print("Menu de Operações:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair da calculadora")
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        num1 = (input("Digite o primeiro número: "))
        num2 = (input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"O resultado da soma é: {resultado}")
    elif opcao == "2":
        num1 = (input("Digite o primeiro número: "))
        num2 = (input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}")
    elif opcao == "3":
        num1 = (input("Digite o primeiro número: "))
        num2 = (input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"O resultado da multiplicação é: {resultado}")
    elif opcao == "4":
        num1 = (input("Digite o primeiro número: "))
        num2 = (input("Digite o segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    elif opcao == "0":
        print("Saindo da calculadora. Até mais!")
        exit()
    else:
        print("Opção inválida, tente novamente.")
