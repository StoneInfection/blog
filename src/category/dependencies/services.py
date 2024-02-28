from typing import Annotated
from fastapi import Depends

from src.category.category_service import CategoryService


ICategoryService = Annotated[CategoryService, Depends()]
