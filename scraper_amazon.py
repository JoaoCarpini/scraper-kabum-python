from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

def pegar_produtos_amazon(URL_AMAZON):
    print("Entrou no scraper do Amazon")

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

    driver.get(URL_AMAZON)
    print("Abriu a página")

    WebDriverWait(driver, 10).until(
        lambda x: x.find_element(
            By.CSS_SELECTOR,
            "div[data-component-type='s-search-result']"
        )
    )

    cards = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
    print(f"Cards encontrados: {len(cards)}")

    for card in cards:
        try:
            nome = card.find_element(
                By.CSS_SELECTOR,
                "h2 span"
            ).text.strip()

            try:
                parte_inteira = card.find_element(
                    By.CSS_SELECTOR,
                    "span.a-price-whole"
                ).text.replace(".", "").replace(",", "")
            except:
                continue

            try:
                centavos = card.find_element(
                    By.CSS_SELECTOR,
                    "span.a-price-fraction"
                ).text
            except:
                centavos = "00"

            valor = f"{parte_inteira}.{centavos}"
            preco_final = float(valor)

            produtos.append({
                "nome": nome,
                "preco": preco_final,
                "loja": "Amazon"
            })

        except Exception as e:
            print(f"Erro: {e}")
            continue

    driver.quit()
    return produtos