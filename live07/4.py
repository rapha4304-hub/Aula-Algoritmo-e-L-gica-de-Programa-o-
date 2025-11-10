opcao = ""

while opcao != "0":
    print("Menu de Opções: ")
    print("1 - Para mostrar o nome da Faculdade")
    print("2 - Para mostrar o nome da Disciplina ")
    print("3 - Para mostrar o nome do Aluno ")
    print("4 - Para mostrar a situação do Aluno ")
    print("0 - Para sair do Sistema ")

    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        print("----------")
        print("Faculdade de Tecnologia SENAI de São Paulo")
        print("----------")
    elif opcao == "2":
        print("----------")
        print("Algoritmos")
        print("----------")
    elif opcao == "3":
        print("----------")
        print("Raphael")
        print("----------")
    elif opcao == "4":
        print("----------")
        print("Aprovado")
        print("----------")
    elif opcao == "0":
        print("----------")
        print("Saindo do Sistema...")
        exit()
    else:
        print("Opção inválida, tente novamente.")
