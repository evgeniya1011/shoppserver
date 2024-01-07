import os
import dotenv
from pathlib import Path

dotenv.load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_URL_TEST = os.getenv('DATABASE_URL_TEST')


TORTOISE_ORM = {
    "connections": {
        "default": DATABASE_URL
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


TORTOISE_ORM_TEST = {
    "connections": {
        "default": DATABASE_URL_TEST
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
