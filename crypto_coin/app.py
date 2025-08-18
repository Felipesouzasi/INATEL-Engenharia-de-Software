from flask import Flask, render_template, request
import requests

import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

app = Flask(
    __name__,
    template_folder=TEMPLATES_DIR,
    static_folder=STATIC_DIR
)

BASE_URL = "https://api.coingecko.com/api/v3/simple/price"

def buscar_preco(moeda, moeda_referencia="usd"):
    params = {
        "ids": moeda.lower(),
        "vs_currencies": moeda_referencia,
        "include_market_cap": "true",
        "include_24hr_change": "true"
    }
    resposta = requests.get(BASE_URL, params=params)
    if resposta.status_code == 200:
        dados = resposta.json()
        if moeda in dados:
            preco = dados[moeda][moeda_referencia]
            market_cap = dados[moeda][f"{moeda_referencia}_market_cap"]
            variacao_24h = dados[moeda][f"{moeda_referencia}_24h_change"]
            return {
                "moeda": moeda.capitalize(),
                "preco": preco,
                "market_cap": market_cap,
                "variacao_24h": variacao_24h
            }
        else:
            return None
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    erro = None
    if request.method == 'POST':
        moeda = request.form.get('moeda')
        resultado = buscar_preco(moeda)
        if not resultado:
            erro = "Moeda não encontrada ou erro na busca."
    return render_template('index.html', resultado=resultado, erro=erro)

if __name__ == "__main__":
    app.run(debug=True)
