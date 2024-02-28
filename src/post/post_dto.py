from pydantic import BaseModel


class PostBaseDTO(BaseModel):
    title: str
    text: str
    name_user: str
    category_id: int


class CreatePostDTO(PostBaseDTO):
    pass


class UpdatePostDTO(PostBaseDTO):
    pass


class GetListPostDTO(PostBaseDTO):
    id: int


class GetPostDTO(PostBaseDTO):
    id: int


class CommentDTO(BaseModel):
    post_id: int
    text: str
    name_user: str
    id: int


class GetCommentDTO(PostBaseDTO):
    comments: list[CommentDTO] | None = None

    class Config:
        from_attributes = True
