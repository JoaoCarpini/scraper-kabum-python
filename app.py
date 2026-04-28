import streamlit as st

from scraper_kabum import pegar_produtos
from scraper_mercadolivre import pegar_produtos_mercadolivre
from scraper_amazon import pegar_produtos_amazon
from processador import tratar_dados
from dotenv import load_dotenv
import os

load_dotenv()

URL_KABUM = os.getenv("URL_KABUM")
URL_MERCADO = os.getenv("URL_MERCADO")
URL_AMAZON = os.getenv("URL_AMAZON")

st.title("Comparador Inteligente de GPUs")

st.markdown(
    "<h4 style='text-align: center;'>Kabum + Mercado Livre + Amazon</h4>",
    unsafe_allow_html=True
)

with st.spinner("Buscando produtos..."):
    lista_kabum = pegar_produtos(URL_KABUM)
    lista_mercado = pegar_produtos_mercadolivre(URL_MERCADO)
    lista_amazon = pegar_produtos_amazon(URL_AMAZON)

    lista_total = lista_kabum + lista_mercado + lista_amazon
    df = tratar_dados(lista_total)

st.subheader("🔥 Top 10 Mais Baratos")

mais_baratos = df.sort_values(
    by=["preco"],
    ascending=True
).head(10)

st.dataframe(mais_baratos)

st.subheader("💎 Top 10 Mais Caros")

mais_caros = df.sort_values(
    by=["preco"],
    ascending=False
).head(10)

st.dataframe(mais_caros)

st.subheader("📊 Todos os Produtos")

st.dataframe(df)