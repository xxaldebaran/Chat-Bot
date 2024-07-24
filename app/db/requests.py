from app.db.models import async_session
from app.db.models import User, Item, Category 
from sqlalchemy import select, delete, update 

async def set_user(tg_id: int):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))  

        if not user:
            session.add(User(tg_id = tg_id))
            await session.commit()

async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))