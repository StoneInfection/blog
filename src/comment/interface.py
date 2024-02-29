# from typing import Protocol
# from abc import abstractmethod
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from src.comment.comment_dto import CreateCommentDTO, UpdateCommentDTO
# from src.comment.comment_model import CommentModel
#
#
# class ICommentRepository(Protocol):
#
#     @abstractmethod
#     async def create(self, dto: CreateCommentDTO):
#         raise NotImplementedError
#
#     @abstractmethod
#     async def update(self, dto: UpdateCommentDTO, pk: int):
#         raise NotImplementedError
#
#     @abstractmethod
#     async def delete(self, pk: int) -> None:
#         raise NotImplementedError
#
#
# class IPostRepository(Protocol):
#
#     @abstractmethod
#     async def get_list(self, category_id: int) -> None:
#         raise NotImplementedError

