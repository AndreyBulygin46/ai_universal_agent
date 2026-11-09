# Файл конфигуруций

from dotenv import load_dotenv
import os

load_dotenv()

# --- Конфиг Универсальный ---
class UniversalConfig:
    def __init__(self, universal_api_key=None, universal_api_url=None):
        self.universal_api_key = universal_api_key
        self.universal_api_url = universal_api_url

# --- Конфиг Mistral ---
class MistralConfig:
    MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
    MISTRAL_URL = 'https://api.mistral.io/v1/'

# --- Конфиг OpenRouter ---
class OpenRouterConfig:
    OPEN_ROUTER_API_KEY = os.getenv('OPEN_ROUTER_API_KEY')
    OPEN_ROUTER_URL = 'https://api.openrouter.ai/v1'

# --- Конфиг OpenCode ---
class OpenCodeConfig:
    OPEN_CODE_API_KEY = os.getenv('OPEN_CODE_API_KEY')
    OPEN_CODE_URL = 'https://opencode.ai/v1'

# --- Конфиг Базы данных ---
class DataBaseConfig:
    DB_URL = f'sqlite:///{os.getenv("DB_URL")}'
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')

# --- Конфиг Логирования ---
class LoggingConfig:
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO')

# --- Точка входа в конфигурацию ---
class BaseConfig:
    UNIVERSAL = UniversalConfig()
    MISTRAL = MistralConfig()
    OPEN_ROUTER = OpenRouterConfig()
    OPEN_CODE = OpenCodeConfig()
    DATA_BASE = DataBaseConfig()
    LOGGING = LoggingConfig()

if __name__ == '__main__':
    print(BaseConfig.DATA_BASE.DB_URL)