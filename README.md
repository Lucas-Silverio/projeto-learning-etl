##Projeto de Engenharia de Dados — API Financeira + PostgreSQL

#Descrição:
Projeto para aprendizado em Engenharia de Dados. Coleta dados financeiros via API, armazena em banco PostgreSQL e gera gráficos para análise.
Tecnologias usadas

    Python

    PostgreSQL

    psycopg2

    requests (para API financeira)

    pandas, matplotlib (manipulação e visualização de dados)

    python-dotenv (para variáveis de ambiente)

#Como usar

    Crie um ambiente virtual e ative-o:

python -m venv venv
venv\Scripts\activate   # no Windows CMD

Instale as dependências:

pip install -r requirements.txt

Configure o arquivo .env com suas variáveis:

DB_HOST=...
DB_NAME=...
DB_USER=...
DB_PASS=...
API_KEY=...

Execute o script principal:

    python main.py

#Objetivo

    Praticar coleta e armazenamento de dados financeiros

    Manipulação e análise de dados em Python

    Uso de banco relacional para engenharia de dados

    Visualização gráfica simples para insights