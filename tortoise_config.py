


# DATABASE_URL = "postgres://postgres:azuhin56@localhost:5432/shopping"
#
# database = Database(DATABASE_URL)

TORTOISE_ORM = {
    "connections": {
        "default": "postgres://postgres:azuhin56@localhost:5432/shop"
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
