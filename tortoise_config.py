import os
import dotenv
from pathlib import Path

dotenv.load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DATABASE_URL = os.getenv('DATABASE_URL')


#
# database = Database(DATABASE_URL)

TORTOISE_ORM = {
    "connections": {
        "default": DATABASE_URL  #"postgres://postgres:azuhin56@localhost:5432/shop"
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
