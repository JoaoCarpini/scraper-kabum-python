from scraper import pegar_produtos
from processador import tratar_dados

URL = "https://www.kabum.com.br/hardware/placa-de-video-vga/placa-de-video-nvidia"


def executar():
    print("Buscando dados...")
    lista_de_produtos = pegar_produtos(URL)

    print(f"Quantidade recebida do scraper: {len(lista_de_produtos)}")

    if lista_de_produtos:
        dados_finais = tratar_dados(lista_de_produtos)

        print(f"Sucesso! {len(dados_finais)} produtos processados.\n")

        for _, produto in dados_finais.iterrows():
            print(f"Produto: {produto['nome']} | Valor: R$ {produto['preco']:.2f}")
    else:
        print("Não foi possível obter os produtos.")


if __name__ == "__main__":
    executar()