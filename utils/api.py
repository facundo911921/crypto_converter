import requests

def get_crypto_price(symbol: str, convert_to: str = "USDT") -> dict:
    """Obtém o preço atual de uma criptomoeda em outra moeda (par de negociação)"""
    try:
        # Definindo endpoint da API
        pair = f"{symbol.upper()}{convert_to.upper()}"
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={pair}"

        # Fazendo requisição GET
        response = requests.get(url)
        response.raise_for_status()

        # Formatando resposta
        data = response.json()

        return {"symbol": symbol.upper(), "price": float(data["price"])}

    except requests.exceptions.RequestException as error:
        return {"error": error}