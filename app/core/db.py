import os
from dotenv import load_dotenv

from databases import Database

from app_init import app


# env init
load_dotenv('./files/.env')
DB_PATH = os.environ.get("DB_PATH")
DATABASE_URL = DB_PATH
# db init
database = Database(DATABASE_URL)


# тут устанавливаем условия подключения к базе данных и отключения - можно
# использовать в роутах контекстный менеджер
# async with Database(...) as db: etc
@app.on_event("startup")
async def startup_database():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_database():
    await database.disconnect()
