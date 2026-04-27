from scraper_kabum import pegar_produtos
from scraper_mercadolivre import pegar_produtos_mercadolivre
from processador import tratar_dados
from dotenv import load_dotenv
import os

load_dotenv()

URL_KABUM = os.getenv(
    "URL_KABUM",
    "https://www.kabum.com.br/hardware/placa-de-video-vga/placa-de-video-nvidia"
)

URL_MERCADO = os.getenv(
    "URL_MERCADO",
    "https://lista.mercadolivre.com.br/placa-de-video-nvidia-geforce-rtx#D[A:placa%20de%20video%20nvidia%20geforce%20rtx]"
)


def executar_kabum():
    print("Buscando dados...")
    lista_de_produtos = pegar_produtos(URL_KABUM)

    print(f"Quantidade recebida do scraper: {len(lista_de_produtos)}")

    if lista_de_produtos:
        dados_finais = tratar_dados(lista_de_produtos)

        print(f"Sucesso! {len(dados_finais)} produtos processados.\n")

        for _, produto in dados_finais.iterrows():
            print(f"Produto: {produto['nome']} | Valor: R$ {produto['preco']:.2f}")
    else:
        print("Não foi possível obter os produtos.")

def executar_mercadolivre():
    print("Buscando dados...")
    lista_de_produtos = pegar_produtos_mercadolivre(URL_MERCADO)

    print(f"Quantidade recebida do scraper: {len(lista_de_produtos)}")

    if lista_de_produtos:
        dados_finais = tratar_dados(lista_de_produtos)

        print(f"Sucesso! {len(dados_finais)} produtos processados.\n")

        for _, produto in dados_finais.iterrows():
            print(f"Produto: {produto['nome']} | Valor: R$ {produto['preco']:.2f}")
    else:
        print("Não foi possível obter os produtos.")


if __name__ == "__main__":
    executar_kabum()
    executar_mercadolivre()