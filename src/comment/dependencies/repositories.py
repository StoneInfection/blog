from typing import Annotated
from fastapi import Depends

from src.comment.comment_repository import CommentRepository

ICommentRepository = Annotated[CommentRepository, Depends()]
