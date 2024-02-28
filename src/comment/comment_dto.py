from pydantic import BaseModel


class CommentBaseDTO(BaseModel):
    post_id: int
    text: str
    name_user: str


class CreateCommentDTO(CommentBaseDTO):
    pass


class UpdateCommentDTO(CommentBaseDTO):
    pass
