import requests
import openai
import os

COINGECKO_BASE = "https://api.coingecko.com/api/v3"

def coletar_dados_coingecko(moeda):
    moeda = moeda.lower()
    # Preço, market cap, variação 24h, volume, supply
    price_url = f"{COINGECKO_BASE}/coins/markets"
    price_params = {
        "vs_currency": "usd",
        "ids": moeda
    }
    price_resp = requests.get(price_url, params=price_params)
    if price_resp.status_code == 200 and price_resp.json():
        info = price_resp.json()[0]
        preco = info.get("current_price", "N/A")
        market_cap = info.get("market_cap", "N/A")
        variacao_24h = info.get("price_change_percentage_24h", "N/A")
        volume = info.get("total_volume", "N/A")
        circulating_supply = info.get("circulating_supply", "N/A")
        total_supply = info.get("total_supply", "N/A")
        high_24h = info.get("high_24h", "N/A")
        low_24h = info.get("low_24h", "N/A")
    else:
        preco = market_cap = variacao_24h = volume = circulating_supply = total_supply = high_24h = low_24h = "N/A"

    # Indicadores técnicos básicos (usando dados de preço)
    rsi = "N/A (precisa de histórico de preços)"
    macd = "N/A (precisa de histórico de preços)"

    # Dados on-chain (CoinGecko fornece alguns, mas limitados)
    onchain_url = f"{COINGECKO_BASE}/coins/{moeda}"
    onchain_resp = requests.get(onchain_url)
    if onchain_resp.status_code == 200:
        onchain = onchain_resp.json()
        genesis_date = onchain.get("genesis_date", "N/A")
        block_time = onchain.get("block_time_in_minutes", "N/A")
        hashing_algorithm = onchain.get("hashing_algorithm", "N/A")
        sentiment = onchain.get("sentiment_votes_up_percentage", "N/A")
    else:
        genesis_date = block_time = hashing_algorithm = sentiment = "N/A"

    # Monta string de dados
    dados = f'''
Moeda: {moeda}
Preço atual: {preco}
Market Cap: {market_cap}
Variação 24h: {variacao_24h}
Volume 24h: {volume}
Supply circulante: {circulating_supply}
Supply total: {total_supply}
Máxima 24h: {high_24h}
Mínima 24h: {low_24h}
Genesis date: {genesis_date}
Block time: {block_time}
Hashing: {hashing_algorithm}
Sentimento CoinGecko: {sentiment}
RSI: {rsi}
MACD: {macd}
'''
    return dados

# Prompt base (resumido para caber aqui, use o seu completo)
prompt_base = """
Você é uma inteligência artificial especialista em análise de criptomoedas, mercados financeiros, DeFi e economia global. 
Seu objetivo é prever, de forma fundamentada e probabilística, o preço mais provável da criptomoeda informada para daqui a 7 dias.

Agora analise os seguintes dados:
[INSIRA AQUI OS DADOS COLETADOS]
"""

def analise_cripto(moeda):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    dados = coletar_dados_coingecko(moeda)
    prompt = prompt_base.replace("[INSIRA AQUI OS DADOS COLETADOS]", dados)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    moeda = input("Digite o nome da criptomoeda (ex: bitcoin, ethereum): ")
    print("\nColetando dados...")
    resultado = analise_cripto(moeda)
    print("\nAnálise e previsão para 7 dias:")
    print(resultado)