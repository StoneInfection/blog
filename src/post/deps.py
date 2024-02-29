from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db_helper import db_helper
from src.post.post_repository import PostRepository
from src.post.post_service import PostService


def service_provide(session: Annotated[AsyncSession, Depends(db_helper.get_session)]):
    return PostService(PostRepository(session))
