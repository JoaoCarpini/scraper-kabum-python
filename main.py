from scraper_kabum import pegar_produtos
from scraper_mercadolivre import pegar_produtos_mercadolivre
from scraper_amazon import pegar_produtos_amazon
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
    "https://lista.mercadolivre.com.br/placa-de-video-nvidia-geforce-rtx"
)

URL_AMAZON = os.getenv(
    "URL_AMAZON",
    "https://www.amazon.com.br/b?node=16364811011&ref=cct_cg_BRPCG_3a1"
)


def executar_comparador():
    print("Buscando dados da Kabum...")
    lista_kabum = pegar_produtos(URL_KABUM)

    print("Buscando dados do Mercado Livre...")
    lista_mercado = pegar_produtos_mercadolivre(URL_MERCADO)

    print("Buscando dados da Amazon...")
    lista_amazon = pegar_produtos_amazon(URL_AMAZON)

    lista_total = lista_kabum + lista_mercado + lista_amazon

    print(f"\nTotal de produtos recebidos: {len(lista_total)}")

    if lista_total:
        dados_finais = tratar_dados(lista_total)

        print(f"\nSucesso! {len(dados_finais)} produtos processados.\n")

        # TODOS OS PRODUTOS
        print("========== TODOS OS PRODUTOS ==========\n")
        for _, produto in dados_finais.iterrows():
            print(
                f"Produto: {produto['nome']} | "
                f"Loja: {produto['loja']} | "
                f"Valor: R$ {produto['preco']:.2f}"
            )

        mais_baratos = dados_finais.sort_values(
            by=["preco"],
            ascending=True
        ).head(10)

        print("\n========== TOP 10 MAIS BARATOS ==========\n")
        for _, produto in mais_baratos.iterrows():
            print(
                f"Produto: {produto['nome']} | "
                f"Loja: {produto['loja']} | "
                f"Valor: R$ {produto['preco']:.2f}"
            )

        mais_caros = dados_finais.sort_values(
            by=["preco"],
            ascending=False
        ).head(10)

        print("\n========== TOP 10 MAIS CAROS ==========\n")
        for _, produto in mais_caros.iterrows():
            print(
                f"Produto: {produto['nome']} | "
                f"Loja: {produto['loja']} | "
                f"Valor: R$ {produto['preco']:.2f}"
            )

    else:
        print("Não foi possível obter os produtos.")


if __name__ == "__main__":
    executar_comparador()