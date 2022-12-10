import asyncio
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from models import Base
from config import PG_DSN


engine = create_async_engine(PG_DSN)
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def async_create_table_people():
    """функция создания таблицы people"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    asyncio.run(async_create_table_people())
