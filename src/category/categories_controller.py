from typing import Annotated

from fastapi import APIRouter, Depends

from src.category.categories_dto import GetListCategoryDTO, CreateCategoryDTO, GetCategoryDTO
from .category_service import CategoryService
from .deps import service_provide

router = APIRouter(prefix="/category", tags=["category"])


@router.post("/", response_model=GetCategoryDTO)
async def create_category(dto: CreateCategoryDTO, service: Annotated[CategoryService, Depends(service_provide)]):
    return await service.create(dto)


@router.get("/", response_model=list[GetListCategoryDTO])
async def get_list_category(service: Annotated[CategoryService, Depends(service_provide)]):
    return await service.get_list()
