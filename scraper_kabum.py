from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import re


def extrair_preco(texto):
    matches = re.findall(r"\d{1,3}(?:\.\d{3})*,\d{2}", texto)

    valores = []

    for match in matches:
        valor = float(match.replace(".", "").replace(",", "."))

        if valor > 1000:
            valores.append(valor)

    if not valores:
        return None

    return min(valores)


def pegar_produtos(URL_KABUM):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    produtos = []

    try:
        driver.get(URL_KABUM)
        time.sleep(6)

        links = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/produto/"]')
        print(f"Quantidade de links de produto encontrados: {len(links)}")

        vistos = set()

        for link in links:
            try:
                href = link.get_attribute("href")

                if not href or href in vistos:
                    continue

                texto = link.text.strip()
                if not texto:
                    continue

                linhas = [linha.strip() for linha in texto.split("\n") if linha.strip()]

                nome = None
                for linha in linhas:
                    if "Placa de Vídeo" in linha or "Placa de Video" in linha:
                        nome = linha
                        break

                if not nome:
                    continue

                preco = extrair_preco(texto)

                if preco is None:
                    continue

                produtos.append({
                    "nome": nome,
                    "preco": preco
                })

                vistos.add(href)

            except Exception:
                continue

        return produtos

    except Exception as e:
        print(f"Erro no scraping: {e}")
        return []

    finally:
        driver.quit()