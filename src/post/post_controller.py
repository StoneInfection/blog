from typing import Annotated

from fastapi import APIRouter, Depends

from src.post.deps import service_provide
from src.post.post_dto import GetPostDTO, GetListPostDTO, CreatePostDTO, GetCommentDTO, UpdatePostDTO
from src.post.post_service import PostService

router = APIRouter(prefix="/post", tags=["post"])


@router.post("/", response_model=GetPostDTO)
async def create_post(dto: CreatePostDTO, service: Annotated[PostService, Depends(service_provide)]):
    return await service.create(dto)


@router.put("/{pk}", response_model=GetPostDTO)
async def update_post(pk: int, dto: UpdatePostDTO, service: Annotated[PostService, Depends(service_provide)]):
    return await service.update(pk, dto)


@router.get("/", response_model=list[GetListPostDTO])
async def get_list_post(category_id: int, service: Annotated[PostService, Depends(service_provide)]):
    return await service.get_list(category_id)


@router.get("/{post_id}", response_model=GetCommentDTO)
async def get_post(post_id: int, service: Annotated[PostService, Depends(service_provide)]):
    return await service.get(post_id)
