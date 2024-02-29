from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.comment.comment_model import CommentModel
from src.post.post_dto import CreatePostDTO, UpdatePostDTO
from src.post.post_model import PostModel


class PostRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, dto: CreatePostDTO):
        instance = PostModel(**dto.model_dump())
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get_list(self, category_id: int):
        stmt = select(PostModel).filter_by(category_id=category_id)
        raw = await self.session.execute(stmt)
        return raw.scalars()

    async def get(self, post_id: int):
        stmt = select(PostModel).filter_by(id=post_id).join(CommentModel, CommentModel.post_id == PostModel.id).options(joinedload(PostModel.comments))
        raw = await self.session.execute(stmt)
        return raw.scalar()

    async def update(self, dto: UpdatePostDTO, pk: int):
        stmt = update(PostModel).values(**dto.model_dump()).filter_by(id=pk).returning(PostModel)
        raw = await self.session.execute(stmt)
        await self.session.commit()
        return raw.scalar_one()
