from typing import Annotated
from fastapi import Depends

from src.category.category_repository import CategoryRepository

ICategoryRepository = Annotated[CategoryRepository, Depends()]
