from fastapi import APIRouter

from src.comment.comment_dto import CreateCommentDTO, UpdateCommentDTO
from src.comment.dependencies.services import ICommentService

router = APIRouter(prefix="/comment", tags=["comment"])


@router.post("/", response_model=CreateCommentDTO)
async def create_comment(dto: CreateCommentDTO, service: ICommentService):
    return await service.create(dto)


@router.put("/{pk}", response_model=CreateCommentDTO)
async def update_comment(pk: int, dto: UpdateCommentDTO, service: ICommentService):
    return await service.update(pk, dto)


@router.delete("/{pk}")
async def delete_comment(pk: int, service: ICommentService):
    return await service.delete(pk)
