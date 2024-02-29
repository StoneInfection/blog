from src.category.categories_dto import CreateCategoryDTO
from src.category.category_repository import CategoryRepository


class CategoryService:

    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    async def create(self, dto: CreateCategoryDTO):
        return await self.repository.create(dto)

    async def get_list(self):
        return await self.repository.get_list()
