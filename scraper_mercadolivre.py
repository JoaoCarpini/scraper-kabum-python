from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def pegar_produtos_mercadolivre(url):
    print("Entrou no scraper do Mercado Livre")

    produtos = []

    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(url)
    print("Abriu a página")

    WebDriverWait(driver, 10).until(
        lambda x: x.find_element(By.CSS_SELECTOR, "div.poly-card__content")
    )

    cards = driver.find_elements(By.CSS_SELECTOR, "div.poly-card__content")
    print(f"Cards encontrados: {len(cards)}")

    for card in cards:
        try:
            titulo = card.find_element(
                By.CSS_SELECTOR,
                "a.poly-component__title"
            )

            nome = titulo.text.strip()

            try:
                parte_inteira = card.find_element(
                    By.CSS_SELECTOR,
                    "span.andes-money-amount__fraction"
                ).text.replace(".", "")
            except:
                continue

            try:
                centavos = card.find_element(
                    By.CSS_SELECTOR,
                    "span.andes-money-amount__cents"
                ).text
            except:
                centavos = "00"

            valor = f"{parte_inteira}.{centavos}"
            preco_final = float(valor)

            # Filtro para garantir que é uma placa de vídeo e não acessórios
            nome_upper = nome.upper()
            termos_validos = ["RTX", "GTX", "RX ", "RX-", "RX0", "RX5", "RX6", "RX7", "GT ", "RADEON", "GEFORCE", "QUADRO", "GPU", "AMD", "NVIDIA"]
            
            # Exceções para termos comuns que não indicam necessariamente uma placa
            e_placa = any(termo in nome_upper for termo in termos_validos)
            
            # Bloquear acessórios e componentes que não são a placa em si
            termos_bloqueados = ["SUPORTE", "ESPELHO", "CABO", "COOLER", "PASTA TERMICA", "FAN", "VENTOINHA", "EXTENSOR"]
            e_acessorio = any(termo in nome_upper for termo in termos_bloqueados)

            if not e_placa or e_acessorio:
                continue

            produtos.append({
                "nome": nome,
                "preco": preco_final,
                "loja": "Mercado Livre"
            })

        except Exception:
            continue

    driver.quit()
    return produtos