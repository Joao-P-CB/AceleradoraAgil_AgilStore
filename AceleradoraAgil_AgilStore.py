def ler_numero(flag_type):  # Funcao que le entrada do teclado e testa caso o usuario inseriu um numero ou nao
    repetir = 1
    # Em geral a funcao garante que o programa nao acabe travando e mantem o corpo principal mais limpo
    if flag_type == 1:  # flag_type define qual a mensagem que deve aparecer na tela para pedir para o usuario
        while repetir == 1:  # Repete ate que o usuario insira um numero valido
            num = input("Qual a quantidade do produto adicionado? ")
            try:
                return int(num)
            except ValueError:  # Solucao adapatada do link: https://pt.stackoverflow.com/questions/288558/como-eu-fa%C3%A7o-prevenir-que-o-input-do-usu%C3%A1rio-n%C3%A3o-resulte-em-um-valueerror-e-ped
                print("\nFormato incorreto, tente novamente.")

    elif flag_type == 2:
        while repetir == 1:
            num = input("Qual o preco do produto adicionado? ")
            try:
                return float(num)
            except ValueError:
                print("\nFormato incorreto, tente novamente.")

    elif flag_type == 3:
        while repetir == 1:
            num = input("Digite o ID do produto: ")
            try:
                return int(num)
            except ValueError:
                print("\nFormato incorreto, tente novamente.")

    elif flag_type == 4:
        while repetir == 1:
            num = input("Digite a opcao desejada: ")
            try:
                return int(num)
            except ValueError:
                print("\nFormato incorreto, tente novamente.")


def lista_ids():
    print("\nID   | Nome")  # Funcao que imprime lista de ids para o usuario poder ver o id que ira escolher
    for i in range(len(produtos)):
        print((produtos[i][4]), "   | ", produtos[i][0])


def lista_total(j):  # Funcao que organiza e imprime a lista de acordo com o input do usuario
    if j != -1:
        listaordenada = sorted(produtos, key=lambda x: x[j])  # fonte da solução com lambda: https://pt.stackoverflow.com/questions/101159/ordernar-lista-de-listas
    else:
        listaordenada = produtos
    print("\nNome   | Categoria   | Quantidade   | Preco   | ID   ")
    for i in range(len(listaordenada)):
        print(*listaordenada[i], sep="  | ")


def busca(j,
          b_id):  # Funcao que busca um parametro dentro da lista, variavel j alinha produtos com o tipo de informacao encontrada em b_id
    encontrou = 0
    i = 0
    while encontrou == 0 and i < len(produtos):  # Percorre produtos buscando o valor de b_id na coluna j da matriz
        if produtos[i][j] == b_id:
            encontrou = 1
            encontrado = i
        i = i + 1

    if encontrou == 0:
        return -1  # Flag que nao encontrou o parametro enviado
    else:
        return encontrado  # Caso encontrou retorna a linha da matriz onde o produto se encontra, para poder trabalhar diretamente na linha


def imprime_produto(
        resultado):  # Imprime os dados de um produto especifico, recebendo uma flag que diz se o produto não existe ou a posição dele
    if resultado == -1:
        print("Produto nao encontrado.")
    else:
        print(produtos[resultado], sep=" | ")


# ________________________________________________________________________________________

# Código main abaixo:

# ________________________________________________________________________________________


produtos = []
op = 0
total_id = 1

print("\nSeja bem-vindo(a) ao controle de estoque da AgilStore!")

while op != 6:
    print("\nComandos a seguir: \n\n 1) Adicionar produto \n 2) Listar produto \n 3) Atualizar produto \n 4) Excluir produto \n 5) Buscar produto \n 6) Encerrar programa \n")
    op = ler_numero(4)  # Chama a função para garantir que sera devolvido um numero

    match op:
        case 1:  # Caso 1 = adicionar um produto novo
            new = []
            teste_preco = 0
            teste_quant = 0
            teste_prod_existente = 1

            while teste_prod_existente == 1:  # flag para testar se o produto já existe. Caso o usuário decida inserir um novo ele retornará a esse ponto
                texto_nome = input("\nDigite o nome do produto a ser adicionado: ")
                texto_nome = texto_nome.capitalize()  # Mantém os nomes com a primeira letra maiúsicula, ajuda com padronização e em testes para garantir que não há nomes repetidos

                if len(produtos) == 0:  # Caso a lista de produtos esteja vazia, não realiza testes, apenas segue o processo de inserção
                    teste_prod_existente = 0
                    new.append(texto_nome)
                    continuar = 1
                else:  # Caso hajam produtos na lista, testa se o produto de mesmo nome já existe
                    existe = busca(0, texto_nome)

                    if existe == -1:  # Se retornar -1 significa que o produto não se encontra na lista, então segue o código
                        teste_prod_existente = 0
                        new.append(texto_nome)
                        continuar = 1
                    else:  # Caso encontre ele segue com o teste se o usuário quer abortar a inserção ou tentar novamente
                        teste_continuar = 0

                        # Eu ia remover essa parte e apenas mover o usuario de volta para o menu principal, com a ideia de deixar o codigo mais simplificado.
                        # Porem apos pensar um pouco sobre eu decidi nao remover, ao meu ver, nao faria sentido remover opcoees do usuario que fazem sua experiencia mais fluida.
                        # Por isso mantive o trecho para que ele escolha se quer voltar ao menu ou apenas tentar novamente mesmo que seja facil de ele voltar a esse ponto.
                        while teste_continuar != 1 and teste_continuar != 2:

                            print("\nProduto ja se encontra na base de dados.\n")
                            print("Gostaria de tentar novamente?\n 1) Sim \n 2) Nao ")
                            teste_continuar = ler_numero(4)

                            if teste_continuar == 2:  # Se o usuário decidiu não tentar novamente pula o resto do case
                                teste_prod_existente = 0
                                continuar = 0
                                input("\nVoltando ao menu principal. \nPressione enter para continuar.")
                            elif teste_continuar != 1:  # Se o usuário não digitou uma opcão válida então repete a pergunta
                                print("Resposta invalida, tente novamente.")

            if continuar == 1:  # Se tudo deu certo e o usuário não abortou a inserção, ele continuará pedindo as informações do produto
                new.append(input("Digite a categoria do produto a ser adicionado: "))  # A categoria não tem muitas condições, então apenas lê o que o usuário digitou
                new[1] = new[1].capitalize()

                while teste_quant == 0:
                    quant = ler_numero(1)  # Chama a função que lê número identificando que se trata de quantidade

                    if quant < 0:  # Quantidade pode ser 0 mas não pode ser negativa
                        print("Quantidade invalida, tente novamente.")
                    else:
                        teste_quant = 1
                        new.append(quant)

                while teste_preco == 0:  # Identifica que é preço
                    preco = ler_numero(2)

                    if preco <= 0:  # Preço não pode ser 0 ou negativo, deve ser um valor positivo.
                        print("Preco invalido, tente novamente.")
                    else:
                        teste_preco = 1
                        new.append(preco)

                new.append(total_id)  # Insere o ID no produto e adiciona + 1

                total_id = total_id + 1  # O ID começa em 1 e vai adicionando 1 para cada produto novo inserido, não volta após exclusões de itens pois não é conectado com o index do produto no vetor produtos

                produtos.append(new)  # Insere o produto new no vetor produtos, deixa de ser um placeholder e faz parte da lista.

        case 2:  # Caso de Imprimir a lista
            i = 0
            if len(produtos) > 0:
                print("\nComo voce gostaria de imprimir a lista? \n 1) Ordem de ID \n 2) Ordem Alfabetica \n 3) Ordem de Quantidade \n 4) Ordem de Preco \n 5) Filtrar por uma categoria\n")
                op_lista = ler_numero(4)  # Identifica qual a opção que o usuário escolheu e chama a função Lista total de acordo, exceto no caso de filtrar categoria
                match op_lista:

                    case 1:
                        lista_total(4)
                        input("\nPressione Enter para continuar.")

                    case 2:
                        lista_total(0)
                        input("\nPressione Enter para continuar.")

                    case 3:
                        lista_total(2)
                        input("\nPressione Enter para continuar.")

                    case 4:
                        lista_total(3)
                        input("\nPressione Enter para continuar.")

                    case 5:  # Como o codigo de filtrar categoria é um tanto diferente do resto e apenas acontece nesse caso, a função foi escrita local mesmo
                        categoria_lista = input("\nQual a categoria que deseja listar? ")
                        categoria_lista = categoria_lista.capitalize()  # Pede a categoria a ser filtrada
                        achou = 0  # Flag se houve algum item encontrado
                        print("\n\nNome     | Categoria     | Quantidade     | Preco     | ID     \n")
                        for i in range(len(produtos)):
                            if produtos[i][1] == categoria_lista:
                                print(*produtos[i],sep="  | ")  # Caso hajam items da categoria enviada, eles serão impressos e a flag Achou deixará de ser 0
                                achou = achou + 1

                        if achou == 0:  # Caso não tenha encontrado algum item, informa o usuário
                            input("\nNenhum item da categoria foi encontrado. \nPressione enter para continuar.")
                        else:  # Inseri esses trechos de input pedindo para o usuário apertar enter pois o menu principal pode empurrar toda o texto pra fora sem dar a chance do usuário entender o que aconteceu
                            input("\nPressione Enter para continuar.")  # Para garantir que o usuário leia as mensagens de erro ou veja as listas impressas é pedido um enter antes de empurrar tudo com o menu principal novamente.

                    case _:
                        print("\nOpcao invalida, tente novamente.")
            else:
                input("A lista de produtos esta vazia. \nPressione enter para continuar.")  # Caso não haja nenhum produto na lista, o programa não avança, apenas informa o usuário

        case 3:  # Caso de edição de itens
            i = 0
            if len(produtos) > 0:  # Apenas entra na função caso hajam itens na lista
                teste_troca = 0
                while teste_troca == 0:
                    print("\nDigite o ID do produto que gostaria de editar ou 0 para voltar ao menu principal: ")  # Imprime a lista de IDs e nomes para o usuário ver o ID do produto a ser editado
                    lista_ids()
                    troca_id = ler_numero(3)

                    produto_alt = [-1, -1, -1,-1]  # O produto placeholder começa com flags de -1 para o programa entender que esses elementos não devem ser inseridos no produto pois não sofreram alterações
                    alterar = 1  # Variável que carrega a opção do usuário no menu
                    alterado = 0  # Variável que identifica se o usuário inseriu alguma informação no placeholder ou não
                    index_troca = -1  # Flag que indica se o ID digitado foi encontrado ou não, caso não ele permanecerá com o valor -1
                    i = 0

                    if troca_id == 0:  # Caso o usuário tenha inserido 0 (nenhum ID será 0) então simplesmente volta ao menu principal
                        index_troca = -2  # Essa parte existe para que o usuário tenha fácil acesso ao menu principal sem precisar inserir um ID válido e depois abortar

                    while index_troca == -1 and i < len(produtos):
                        if produtos[i][4] == troca_id:
                            index_troca = i  # Busca a posição na lista onde o produto em questão se encontra
                        i = i + 1

                    if index_troca >= 0:  # Se não for -1 ou -2 significa que o item foi encontrado, procede com as alterações
                        teste_troca = 1  # O usuário inseriu um ID válido então não precisa manter o loop correndo
                        while alterar != 0:  # Mantém o usuário nas alterações até que ele deseja sair
                            print("\nO que deseja alterar? \n 1) Nome \n 2) Categoria \n 3) Quantidade \n 4) Preco \n Digite 0 para encerrar alteracoes\n")
                            alterar = ler_numero(4)

                            match alterar:
                                case 1:
                                    nome_repetido = 0
                                    produto_alt[0] = input("Digite o novo nome do produto: ")
                                    produto_alt[0] = produto_alt[0].capitalize()

                                    for i in range(
                                            len(produtos)):  # Testa se o novo nome já existe dentro da lista, caso sim volta para as opções de alterações
                                        if i != index_troca:
                                            if produto_alt[0] == produtos[i][0]:
                                                nome_repetido = 1
                                                produto_alt[0] = -1  # Reverte a alteração e invalida o campo pois o nome inserido já está na lista
                                                print("\nProduto de mesmo nome ja existe na lista, alteracao nao foi salva. \n")

                                    if nome_repetido != 1:
                                        alterado = 1  # Caso o nome inserido não seja repetido, altera a flag para o programa saber que houve uma alteração salva no placeholder

                                case 2:
                                    produto_alt[1] = input("Digite a nova categoria do produto: ")  # lê a nova categoria, não há critério algum para categoria
                                    alterado = 1  # Programa entende que houve uma alteração para confirmar ao final

                                case 3:
                                    teste_quant = 0
                                    while teste_quant == 0:
                                        produto_alt[2] = ler_numero(1)

                                        if produto_alt[2] < 0:  # Novamente, quantidade não pode ser negativa
                                            print("Quantidade invalida, tente novamente.")
                                        else:
                                            teste_quant = 1
                                    alterado = 1

                                case 4:
                                    teste_preco = 0
                                    while teste_preco == 0:
                                        produto_alt[3] = ler_numero(2)

                                        if produto_alt[3] <= 0:  # Preço deve ser positivo
                                            print("Quantidade invalida, tente novamente.")
                                        else:
                                            teste_preco = 1
                                    alterado = 1

                                case 0:
                                    confirmar = -1  # Ao encerrar as alterações, caso haja alguma alteração válida o programa pede para o usuário confirmar se quer salvar ou não
                                    if alterado == 1:  # Teste se houve alguma alteração válida
                                        while confirmar == -1:
                                            print("Gostaria de confirmar as alteracoes? \n1) Sim \n2) Nao")
                                            conf_alt = ler_numero(4)

                                            match conf_alt:
                                                case 1:
                                                    for i in range(
                                                            len(produto_alt)):  # Caso o usuário confirme as alterações, insere todos os valores que não sejam -1
                                                        if produto_alt[i] != -1:
                                                            produtos[index_troca][i] = produto_alt[i]
                                                    confirmar = 1

                                                case 2:  # Programa volta para o menu principal caso o usuário escolha não salvar
                                                    print("Edicao abortada.")
                                                    confirmar = 1

                                                case _:
                                                    print("\nOpcao invalida, tente novamente.\n")

                                        # Novamente pede um enter antes de continuar para garantir que o usuário possa entender o que houve antes de seguir
                                        input("Alteracoes finalizadas. \nPressione enter para continuar.")
                                    else:
                                        input("\nNenhuma alteracao inserida. \nPressione enter para continuar.")

                                case _:
                                    print("\nOpcao invalida, tente novamente.")

                    elif index_troca == -1:  # Caso o usuário tenha inserido um ID que pesquisou e não encontrou pede para inserir novamente
                        print("\nID invalido, tentar novamente?")
                    else:  # Caso a flag não seja positiva e não seja -1 então o usuário decidiu voltar (flag -2) então o programa apenas volta para o menu principal
                        teste_troca = 1
                        input("Voltando ao menu principal. \nPressione enter para continuar.")
            else:  # Lista vazia a função simplesmente encerra.
                input("\nA lista de produtos esta vazia. \nPressione enter para continuar.")

        case 4:  # Caso de remoção de produtos
            if len(produtos) > 0:
                print("\nQual o produto que deseja remover? Digite 0 case deseja voltar ao menu anterior")
                lista_ids()
                valido = 0
                index_remover = -1

                while valido == 0:
                    remove_id = ler_numero(3)  # Pede o ID a ser removido
                    confirmado = 0
                    i = 0
                    if remove_id != 0:  # Caso o usuário digite um ID que não seja 0 a função continua
                        index_remover = busca(4, remove_id)  # Chama a função de busca com o ID

                        if index_remover == -1:  # Se não encontrou o ID o usuário deverá tentar novamente
                            print("\nID invalido, tente novamente.")
                        else:
                            valido = 1  # Encontrou um ID válido, então o loop não precisará repetir
                            confirmar = 0

                            while confirmar != 1 and confirmar != 2:
                                print("\nConfirmar a exclusao do item? \n 1) Sim \n 2) Nao \n")  # Confirma com o usuário sobre a exclusão
                                confirmar = ler_numero(4)
                                match confirmar:
                                    case 1:  # Caso sim, remove o item da lista
                                        produtos.pop(index_remover)
                                        input("\nExclusao realizada com sucesso! \nPressione enter para continuar.")

                                    case 2:  # Caso não, volta ao menu principal
                                        input("\nExclusao abortada. \nPressione enter para continuar.")

                                    case _:
                                        print("\nOpcao invalida, tente novamente.")
                    else:  # Se o usuário digitar 0 o programa apenas volta ao menu principal
                        valido = 1
                        input("\nVoltando ao menu principal. \nPressione enter para continuar.")
            else:  # Lista vazia = não roda código algum
                input("\nA lista de produtos esta vazia. \nPressione enter para continuar.")

        case 5:  # Caso de busca
            op_busca = 1
            if len(produtos) > 0:
                while op_busca != 0:

                    print("\nComo preferes fazer a busca? \n 1) Nome do produto \n 2) ID do produto \n 0) Encerrar a busca\n")  # Função um tanto simples, pede para o usuário a opção desejada
                    op_busca = ler_numero(4)

                    match op_busca:  # Identifica o caso que ele quer, pede o produto específico baseado no parâmetro de busca e retorna os dados do produto se existir e uma mensagem de produto não encontrado caso contrário.
                        case 1:
                            busca_nome = input("\nDigite o nome do produto: ")
                            busca_nome = busca_nome.capitalize()
                            resultado_busca = busca(0, busca_nome)  # Busca
                            imprime_produto(resultado_busca)  # Imprime

                        case 2:
                            busca_id = ler_numero(3)
                            resultado_busca = busca(4, busca_id)
                            imprime_produto(resultado_busca)

                        case 0:
                            input("\nBuscas encerradas. \nPressione enter para continuar")

                        case _:
                            print("\nOpcao invalida, tente novamente.")
            else:
                input("\nA lista de produtos esta vazia. \nPressione enter para continuar.")

        case 6:  # Encerra o programa
            print("\nPrograma Encerrando!")

        case _:  # Opção inválida
            print("\nOpcao invalida, tente novamente.")
