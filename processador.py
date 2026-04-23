import pandas as pd

def tratar_dados(lista_produtos):
    df = pd.DataFrame(lista_produtos)

    df = df.drop_duplicates(subset=["nome"])
    df = df[(df["preco"] > 2000) & (df["preco"] < 4000)]
    df = df.sort_values(by=["preco"], ascending=False)
    df = df.head(10)

    return df