from dotenv import load_dotenv
import os

def carregar_db_config():
    load_dotenv()
    return {
        'host': os.getenv("DB_HOST"),
        'port': int(os.getenv("DB_PORT",5432)),
        'database': os.getenv("DB_NAME"),
        'user': os.getenv("DB_USER"),
        'password': os.getenv("DB_PASS")  
    }
def carregar_api_key():
    load_dotenv()
    return os.getenv("API_KEY")