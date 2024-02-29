from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.category.categories_dto import CreateCategoryDTO
from src.category.categories_model import CategoryModel


class CategoryRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, dto: CreateCategoryDTO):
        instance = CategoryModel(**dto.model_dump())
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get_list(self):
        stmt = select(CategoryModel)
        raw = await self.session.execute(stmt)
        return raw.scalars()
