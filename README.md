# 🚀 Scraper de Preços com Python

Projeto de web scraping desenvolvido para coletar e analisar preços de placas de vídeo em um e-commerce.

> ⚠️ A Kabum foi utilizada apenas para fins de estudo.  
> A lógica pode ser facilmente adaptada para outros sites.

---

## 🔍 Funcionalidades

- Acessa a página automaticamente utilizando Selenium
- Coleta nome e preço dos produtos
- Remove produtos duplicados
- Filtra produtos por faixa de preço
- Ordena os resultados
- Exibe os 10 produtos mais caros dentro do filtro

---

## 🧠 O que foi aplicado

- Web Scraping com Selenium
- Tratamento de dados com Pandas
- Expressões regulares (Regex)
- Manipulação de listas e dicionários
- Pipeline de dados (extração → tratamento → saída)

---

## 🛠️ Tecnologias utilizadas

- Python
- Selenium
- Pandas
- WebDriver Manager

---

## ▶️ Como executar o projeto

### 1. Clonar o repositório

```bash
1.
git clone https://github.com/JoaoCarpini/scraper-kabum-python.git

2. Acessar a pasta
cd scraper-kabum-python

3. Instalar as dependências
pip install selenium pandas webdriver-manager

4. Executar
python main.py

📊 Exemplo de saída
Produto: Placa de Vídeo RTX 5070...
Valor: R$ 4799.99

Produto: Placa de Vídeo RTX 5060 Ti...
Valor: R$ 4099.99