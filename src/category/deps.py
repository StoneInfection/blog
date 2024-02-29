from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.category.category_repository import CategoryRepository
from src.category.category_service import CategoryService
from src.database.db_helper import db_helper


def service_provide(session: Annotated[AsyncSession, Depends(db_helper.get_session)]):
    return CategoryService(CategoryRepository(session))
