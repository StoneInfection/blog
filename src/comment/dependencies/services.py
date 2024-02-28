from typing import Annotated
from fastapi import Depends

from src.comment.comment_service import CommentService

ICommentService = Annotated[CommentService, Depends()]
