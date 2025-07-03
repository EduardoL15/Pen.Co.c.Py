def lista_de_compras():
    lista = {}
    id = 0
    id_maior = 0
    unidade_medida = {
        "A": "Quilograma",
        "B": "Grama",
        "C": "Litro",
        "D": "Mililitro",
        "E": "Unidade",
        "F": "Metro",
        "G": "Centímetro"
        }
    while True:
        print(lista)
        print()
        print("A. Adicionar produto")
        print("B. Remover produto")
        print("C. Pesquisar produtos")
        print("D. Sair do programa")
        operacao = input("Selecione uma opção ou 'D' para Sair: ").upper()

        if operacao == "D":
            break

        if operacao not in ["A", "B", "C", "D"]:
            print("Opção invalido! Teste novamente.\n")
            continue

        match operacao:
            case "A":
                nome_P = input("Digite o nome do Produto(ou V para Voltar): ").upper()
                if nome_P == "V":
                    print("Voltando para tela inicial...\n")
                    continue
                else:
                    if nome_P not in lista:
                        

                medida_escolhida = None
                while not medida_escolhida:
                    print(f"\nEscolha a Unidade de medida: ")
                    for k, v in unidade_medida.items():
                        print(f"{k}.{v}")
                    medida = input("Selecione uma opção: ").upper()
                    medida_escolhida = unidade_medida.get(medida)
                    if not medida_escolhida:
                        print("Tipo inválido!\n")

                match medida:
                    case "A":
                        while True:
                            try:
                                valor = float(input("Digite quantos Kg são: "))
                                unidade_m = {
                                    valor : "Quilograma"
                                }
                                break
                            except ValueError:
                                print("valor incoreto! confira se foram inseridos apenas números.\n")
                                continue
                    case "B":
                        while True:
                            try:
                                valor = float(input("Digite quantos g são: "))
                                unidade_m = {
                                        valor : "Grama"
                                }
                                break
                            except ValueError:
                                print("valor incoreto! confira se foram inseridos apenas números.\n")
                                continue
                    case "C":
                        while True:
                            try:
                                valor = float(input("Digite quantos L são: "))
                                unidade_m = {
                                        valor : "Litro"
                                }
                                break
                            except ValueError:
                                print("valor incoreto! confira se foram inseridos apenas números.\n")
                                continue
                    case "D":
                        while True:
                            try:
                                valor = float(input("Digite quantos Ml são: "))
                                unidade_m = {
                                        valor : "Mililitro"
                                }
                                break
                            except ValueError:
                                print("valor incoreto! confira se foram inseridos apenas números.\n")
                                continue
                    case "E":
                        while True:
                            try:
                                valor = float(input("Digite quantas unidades são: "))
                                unidade_m = {
                                        valor : "Unidade"
                                }
                                break
                            except ValueError:
                                print("valor incoreto! confira se foram inseridos apenas números.\n")
                                continue
                    case "F":
                        while True:
                            try:
                                valor = float(input("Digite quantos M são: "))
                                unidade_m = {
                                        valor : "Metro"
                                }
                                break
                            except ValueError:
                                print("valor incoreto! confira se foram inseridos apenas números.\n")
                                continue
                    case "G":
                        while True:
                            try:
                                valor = float(input("Digite quantos Cm são: "))
                                unidade_m = {
                                        valor : "Centímetro"
                                }
                                break
                            except ValueError:
                                print("valor incoreto! confira se foram inseridos apenas números.\n")
                                continue
                while True:
                    try:
                        quatidade = int(input("informe a Quantidade: "))
                        break
                    except ValueError:
                        print("valor incoreto! confira se foram inseridos apenas números.\n")
                        continue
                descricao = input("Informe a descrição do Produto: ")

                id_maior = id

                if id == id_maior:
                    id += 1

                item = {
                    "ID": id,
                    "Nome": nome_P,
                    "medida": unidade_m,
                    "Quantidade": quatidade,
                    "descrição do Produto": descricao
                }
                lista.append(item)
                print(f"O item {nome_P} foi adicionado na lista!")

                return lista, id
            case B:
                nome_P = input("Informe o nome do Produto que deseja excluir: ")   


lista_de_compras()