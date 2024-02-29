from typing import Annotated

from fastapi import APIRouter, Depends

from src.comment.comment_dto import CreateCommentDTO, UpdateCommentDTO
from src.comment.comment_service import CommentService
from src.comment.deps import service_provide

router = APIRouter(prefix="/comment", tags=["comment"])


@router.post("/", response_model=CreateCommentDTO)
async def create_comment(dto: CreateCommentDTO, service: Annotated[CommentService, Depends(service_provide)]):
    return await service.create(dto)


@router.put("/{pk}", response_model=CreateCommentDTO)
async def update_comment(pk: int, dto: UpdateCommentDTO, service: Annotated[CommentService, Depends(service_provide)]):
    return await service.update(pk, dto)


@router.delete("/{pk}")
async def delete_comment(pk: int, service: Annotated[CommentService, Depends(service_provide)]):
    return await service.delete(pk)
