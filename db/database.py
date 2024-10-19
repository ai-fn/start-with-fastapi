from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import Settings
from db.models import Model


conn_string = f"postgresql+asyncpg://{Settings.db_user}:{Settings.db_password}@{Settings.db_host}:5432/{Settings.db_name}"

engine = create_async_engine(conn_string)
session = async_sessionmaker(engine, expire_on_commit=False)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
