from typing import Annotated
from fastapi import Depends

from src.post.post_service import PostService

IPostService = Annotated[PostService, Depends()]
