from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import BigInteger, String, ForeignKey

engine = create_async_engine(url = 'sqlite+aiosqlite:///db.sqlite3')
async_session = async_sessionmaker(engine)

class BaseModel(DeclarativeBase, AsyncAttrs):
    pass

#todo: if user uses it for the first time/ not the first rodeo 
class User(BaseModel):
    __tablename__ = 'users' 
    id: Mapped[int] = mapped_column(primary_key = True)
    tg_id = mapped_column(BigInteger)


class Category(BaseModel):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(25))

class Item(BaseModel):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(25))
    description: Mapped[str] = mapped_column(String(100))
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))

async def async_main():
    async with engine.begin() as connection:
        await connection.run_sync(BaseModel.metadata.create_all)