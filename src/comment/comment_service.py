from src.comment.comment_dto import CreateCommentDTO, UpdateCommentDTO
from src.comment.comment_repository import CommentRepository


class CommentService:

    def __init__(self, repository: CommentRepository):#, repo_post: IPostRepository):
        self.repository = repository

    async def create(self, dto: CreateCommentDTO):
        return await self.repository.create(dto)

    async def update(self, pk: int, dto: UpdateCommentDTO):
        return await self.repository.update(dto, pk)

    async def delete(self, pk: int):
        return await self.repository.delete(pk)
