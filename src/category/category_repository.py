from sqlalchemy import select

from src.category.dependencies.session import ISession
from src.category.categories_dto import CreateCategoryDTO
from src.category.categories_model import CategoryModel


class CategoryRepository:

    def __init__(self, session: ISession):
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
