from tortoise import Tortoise

DATABASE_URL = "sqlite://./db.sqlite3"

async def initDb():
    # Here we create a SQLite DB using file "db.sqlite3"

    await Tortoise.init(db_url=DATABASE_URL,modules={"models":["parcel_app.models"]})

    # Generate the schema
    await Tortoise.generate_schemas()

