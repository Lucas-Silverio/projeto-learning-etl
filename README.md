# 📊 Projeto de Engenharia de Dados — API Financeira + PostgreSQL

## 🧾 Descrição

Projeto de aprendizado em Engenharia de Dados que realiza:

- Coleta de dados financeiros via API
- Armazenamento dos dados em um banco de dados PostgreSQL
- Análise e visualização dos dados por meio de gráficos

## 🛠️ Tecnologias Utilizadas

- **Python**
- **PostgreSQL**
- **psycopg2** — conexão com o banco
- **requests** — consumo da API financeira
- **pandas**, **matplotlib** — manipulação e visualização dos dados
- **python-dotenv** — gerenciamento de variáveis de ambiente

## 🚀 Como Executar

### 1. Clone o repositório

``` 
git clone https://github.com/Lucas-Silverio/projeto-learning-etl.git
cd projeto-learning-etl
```
### 2. Crie e ative o ambiente virtual
```
python -m venv venv
```
**Ative o ambiente:**

Windows (Powershell): .\venv\Scripts\Activate.ps1
<br><br>
Linux: source /venv/bin/activate

### 3. Instale as dependências
```
pip install -r requirements.txt
```

### 4. Configure o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```

DB_HOST=seu_host
DB_NAME=seu_banco
DB_USER=seu_usuario
DB_PASS=sua_senha
API_KEY=sua_chave_api
```
### 5. Execute o pipeline
```
python main.py
```

## 🎯 Objetivos do Projeto

- Praticar a extração de dados a partir de APIs públicas
- Armazenar e organizar dados em um banco relacional
- Realizar transformações e análises com pandas
- Gerar visualizações simples para extração de insights

## 📎 Fonte de Dados

Os dados utilizados neste projeto são obtidos por meio da **[Alpha Vantage API](https://www.alphavantage.co/)** — uma API pública para dados financeiros em tempo real e históricos.

> É necessário gerar uma chave gratuita no site da Alpha Vantage para acessar os endpoints.
