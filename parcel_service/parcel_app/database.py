from tortoise import Tortoise

DATABASE_URL = "sqlite://./db.sqlite"


async def initDb():
    # Here we create a SQLite DB using file "db.sqlite"

    config = {
        "connections": {
            "default": {
                "engine": "tortoise.backends.sqlite",
                "credentials": {"file_path": "./db.sqlite"},
            }
        },
        "apps": {
            "models": {"models": ["parcel_app.models"], "default_connection": "default"}
        },
        # "db_url": DATABASE_URL,
        # "connections_config": {"default": {"journal_mode": "DELETE"}},
    }

    await Tortoise.init(
        config=config
    )  # ,db_url=DATABASE_URL, modules={"models": ["parcel_app.models"]})

    # Generate the schema
    await Tortoise.generate_schemas()
