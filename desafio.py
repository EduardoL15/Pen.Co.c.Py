def calculadora():
    while True:
        print("Calculadora Simples")
        print()
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("s. sair")
        operacao = input("Selecione uma opção ou 's' para Sair: ")

        if operacao == 's' or operacao =='S':
            print("Obrigado por utilizar a Calculadora Simples")
            break

        if operacao not in ["1", "2", "3", "4"]:
            print("Opção invalido! Teste novamente.")
            continue

        num1 = float(input("1° Numero: "))
        num2 = float(input("2° Numero: "))

        if operacao == "1":
            resutado = num1 + num2
            print(f"O Resultado da Soma é {resutado}")
        elif operacao == "2":
            resutado = num1 - num2
            print(f"O Resultado da Subtração é {resutado}")
        elif operacao == "3":
            resutado = num1 * num2
            print(f"O Resultado da Multiplicação é {resutado}")
        else:
            if num2 == 0:
                print("Divisões por zero não são possiveis. Tente Novamente")
                continue
            else:
                resutado = num1 / num2
            print(f"O Resultado da Divisão é {resutado}")

calculadora()

