from pydantic import BaseModel


class CategoriesBaseDTO(BaseModel):
    name: str


class CreateCategoryDTO(CategoriesBaseDTO):
    pass


class GetCategoryDTO(CategoriesBaseDTO):
    id: int


class GetListCategoryDTO(CategoriesBaseDTO):
    id: int
