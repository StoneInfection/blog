from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.comment.comment_repository import CommentRepository

from src.comment.comment_service import CommentService
from src.database.db_helper import db_helper


def service_provide(session: Annotated[AsyncSession, Depends(db_helper.get_session)]):
    return CommentService(CommentRepository(session))
