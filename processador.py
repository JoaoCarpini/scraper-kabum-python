import pandas as pd

def tratar_dados(lista_produtos):
    df = pd.DataFrame(lista_produtos)

    df = df.drop_duplicates(subset=["nome"])
    df = df[(df["preco"] > 500) & (df["preco"] < 15000)]

    return df