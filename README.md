# CriptoCoin

## Descrição do Projeto
O CriptoCoin é uma aplicação web desenvolvida em Flask que permite ao usuário consultar informações em tempo real sobre criptomoedas, como preço atual, valor de mercado e variação nas últimas 24 horas. Os dados são obtidos diretamente da API pública do CoinGecko. O objetivo é fornecer uma interface simples, rápida e visualmente agradável para acompanhar o mercado de criptomoedas.

## Configuração do Ambiente
1. **Clone o repositório:**
	```bash
	git clone <url-do-repositorio>
	cd criptoCoin
	```
2. **(Opcional) Crie um ambiente virtual:**
	```bash
	python -m venv venv
	source venv/bin/activate  # Linux/Mac
	venv\Scripts\activate   # Windows
	```

## Instalação de Dependências
Execute o comando abaixo para instalar todas as dependências necessárias:
```bash
pip install flask requests
```

## Execução do Projeto
1. Certifique-se de estar na raiz do projeto (onde está o arquivo `pyproject.toml` ou `app.py`).
2. Execute o servidor Flask:
	```bash
	python -m crypto_coin.app
	```
3. Acesse no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Explicação dos dois últimos tópicos

### Instalação de Dependências
Esse passo garante que todas as bibliotecas externas usadas no projeto (como Flask e Requests) estejam instaladas no seu ambiente Python. O comando `pip install flask requests` baixa e instala essas bibliotecas automaticamente.

### Execução do Projeto
Após instalar as dependências, você executa o servidor Flask com o comando `python -m crypto_coin.app`. Isso inicia a aplicação web localmente, permitindo que você acesse a interface pelo navegador e utilize todas as funcionalidades do CriptoCoin.
# Projeto CryptoCoin
Sistema simples em Python para consultar preços de criptomoedas usando a API da CoinGecko.

## 🚀 Funcionalidades
- Consulta o preço atual da criptomoeda
- Mostra variação nas últimas 24h
- Exibe valor de mercado

## 🛠️ Tecnologias usadas
- Python 3.10+
- Poetry (gerenciador de dependências e build)
- requests (para chamadas HTTP)

## 📦 Como rodar
1. Instale o Poetry:
```bash
pip install poetry
