from sqlalchemy import update, delete

from src.category.dependencies.session import ISession
from src.comment.comment_dto import CreateCommentDTO, UpdateCommentDTO
from src.comment.comment_model import CommentModel


class CommentRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def create(self, dto: CreateCommentDTO):
        instance = CommentModel(**dto.model_dump())
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def update(self, dto: UpdateCommentDTO, pk: int):
        stmt = update(CommentModel).values(**dto.model_dump()).filter_by(id=pk).returning(CommentModel)
        raw = await self.session.execute(stmt)
        await self.session.commit()
        return raw.scalar_one()

    async def delete(self, pk: int) -> None:
        stmt = delete(CommentModel).where(CommentModel.id == pk)
        await self.session.execute(stmt)
        await self.session.commit()
