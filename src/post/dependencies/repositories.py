from typing import Annotated
from fastapi import Depends

from src.post.post_repository import PostRepository

IPostRepository = Annotated[PostRepository, Depends()]
