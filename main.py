import requests
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from psycopg2.extras import execute_values
from utils import carregar_api_key, carregar_db_config

#Simbolo da ação que deseja buscar
STOCK_SYMBOL = 'MSFT'

#função para criar conexao com banco
def connect_db():
    conexao = psycopg2.connect(**carregar_db_config())
    return conexao

#função para criar tabela caso não exista
def create_table(conexao):
    query = """
    CREATE TABLE IF NOT EXISTS stock_prices(
        date DATE PRIMARY KEY,
        open FLOAT,
        high FLOAT,
        low FLOAT,
        close FLOAT,
        volume BIGINT
    );
    """
    with conexao.cursor() as cursor:
        cursor.execute(query)
        conexao.commit()

#função para buscar os dados da API (Alpha Vantage)
def fetch_stock_data(simbolo):
    url = f'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': simbolo,
        'apikey': carregar_api_key(),
        'outputsize': 'compact' # últimos 100 dias
    }
    response = requests.get(url, params=params)
    data = response.json()
    if 'Time Series (Daily)' not in data:
        raise Exception(f"Erro na API: {data.get('Error Message', 'Dados não encontrados.')}")
    
    time_series = data['Time Series (Daily)']

    #Extrair e formatar os dados para inserir no banco
    
    dados = []
    for date, daily_data in time_series.items():
        dados.append((
            date,
            float(daily_data['1. open']),
            float(daily_data['2. high']),
            float(daily_data['3. low']),
            float(daily_data['4. close']),
            int(daily_data['5. volume'])
        ))

    return dados
    
    
#função para inserir dados no banco
def insert_stock_data(conexao, dados):
    query = """
    INSERT INTO stock_prices (date, open, high, low, close, volume)
    VALUES %s
    ON CONFLICT (date) DO UPDATE SET
        open = EXCLUDED.open,
        high = EXCLUDED.high,
        low = EXCLUDED.low,
        close = EXCLUDED.close,
        volume = EXCLUDED.volume;
    """
    with conexao.cursor() as cursor:
        execute_values(cursor, query, dados)
        conexao.commit()
    
#função para carregar os dados do banco
def load_data(conexao):
    query = f"SELECT * FROM stock_prices ORDER BY date;"
    return pd.read_sql(query, conexao, index_col="date",parse_dates=["date"])

#função para montar o gráfico
def plot_data(df):
    plt.figure(figsize=(12,5))
    plt.plot(df.index, df['close'], label='Fechamento')
    plt.plot(df.index,df['open'], label="Abertura")
    plt.title('Preço de Fechamento')
    plt.xlabel('Data')
    plt.ylabel('Preço (USD)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12,3))
    plt.bar(df.index, df['volume'], color='orange')
    plt.title('Volume Negociado')
    plt.xlabel('Data')
    plt.ylabel('Volume')
    plt.tight_layout()
    plt.show()
#função principal
def main():
    print("Conectando ao banco...")
    conexao = connect_db()

    try:

        print("Criando tabela caso não exista...")
        create_table(conexao)

        print(f"Buscando dados da ação {STOCK_SYMBOL}...")
        stock__dados = fetch_stock_data(STOCK_SYMBOL)

        print(f"Inserindo {len(stock__dados)} registros no banco...")
        insert_stock_data(conexao,stock__dados)

        print("Carregando dados para análise...")
        df = load_data(conexao)

        print("Montando dados...")
        plot_data(df)
        
    finally:
        conexao.close()

if __name__ == '__main__':
    main()