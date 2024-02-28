from fastapi import APIRouter

from src.category.categories_dto import GetListCategoryDTO, CreateCategoryDTO, GetCategoryDTO
from src.category.dependencies.services import ICategoryService

router = APIRouter(prefix="/category", tags=["category"])


@router.post("/", response_model=GetCategoryDTO)
async def create_category(dto: CreateCategoryDTO, service: ICategoryService):
    return await service.create(dto)


@router.get("/", response_model=list[GetListCategoryDTO])
async def get_list_category(service: ICategoryService):
    return await service.get_list()
