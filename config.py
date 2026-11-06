# Файл конфигуруций

from dotenv import load_dotenv
import os

load_dotenv()

# --- Конфиг Mistral ---
class MistralConfig:
    MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
    MISTRAL_URL = 'https://api.mistral.io/v1/'

# --- Конфиг OpenRouter ---
class OpenRouterConfig:
    OPEN_ROUTER_API_KEY = os.getenv('OPEN_ROUTER_API_KEY')
    OPEN_ROUTER_URL = 'https://api.openrouter.ai/v1

# --- Конфиг OpenCode ---
class OpenCodeConfig:
    pass

# --- Конфиг универсальный ---
class UniversalConfig:
    pass

# --- Конфиг Базы данных ---
class DataBaseConfig:
    pass

# --- Конфиг Логирования ---
class LoggingConfig:
    pass

# --- Главный конфиг ---
class BaseConfig:
    MISTRAL = MistralConfig()
    OPEN_ROUTER = OpenRouterConfig()
    OPEN_CODE = OpenCodeConfig()
    UNIVERSAL = UniversalConfig()
    DATA_BASE = DataBaseConfig()
    LOGGING = LoggingConfig()
