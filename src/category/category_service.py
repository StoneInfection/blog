from src.category.dependencies.repositories import ICategoryRepository
from src.category.categories_dto import CreateCategoryDTO


class CategoryService:

    def __init__(self, repository: ICategoryRepository):
        self.repository = repository

    async def create(self, dto: CreateCategoryDTO):
        return await self.repository.create(dto)

    async def get_list(self):
        return await self.repository.get_list()
