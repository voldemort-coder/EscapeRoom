import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


# 🔹 Obține prețurile criptomonedelor din API-ul CoinGecko
def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Formatăm datele pentru afișare
        prices = [
            ["Bitcoin (BTC)", f"${data['bitcoin']['usd']}"],
            ["Ethereum (ETH)", f"${data['ethereum']['usd']}"]
        ]

        print("\n📈 Prețuri actuale ale criptomonedelor:")
        print(tabulate(prices, headers=["Criptomonedă", "Preț (USD)"], tablefmt="grid"))

    except requests.exceptions.RequestException as e:
        print(f"\n Eroare la conectarea cu API-ul CoinGecko: {e}")


# 🔹 Web Scraping pentru știrile de pe CoinDesk
def get_crypto_news():
    url = "https://www.coindesk.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Căutăm titlurile articolelor
        articles = soup.find_all("a", class_="headline", limit=5)

        print("\n📰 Cele mai recente 5 știri despre criptomonede:")
        for idx, article in enumerate(articles, start=1):
            title = article.text.strip()
            link = "https://www.coindesk.com" + article["href"]
            print(f"{idx}. {title}\n   🔗 {link}\n")

    except requests.exceptions.RequestException as e:
        print(f"\n Eroare la accesarea site-ului CoinDesk: {e}")


# 🔹 Executăm funcțiile
get_crypto_prices()
get_crypto_news()
