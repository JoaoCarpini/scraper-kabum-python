import pandas as pd

def tratar_dados(lista_produtos):
    df = pd.DataFrame(lista_produtos)

    df = df.drop_duplicates(subset=["nome"])
    print(df[["nome", "preco"]])
    df = df[(df["preco"] > 500) & (df["preco"] < 15000)]
    df = df.sort_values(by=["preco"], ascending=False)
    df = df.head(10)

    return df