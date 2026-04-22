def tratar_dados(lista_produtos):
    produtos_unicos = []
    nomes_vistos = set()

    for produto in lista_produtos:
        nome = produto["nome"].strip()

        if nome not in nomes_vistos:
            produtos_unicos.append(produto)
            nomes_vistos.add(nome)

    return produtos_unicos