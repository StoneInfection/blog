from src.post.post_dto import CreatePostDTO, UpdatePostDTO
from src.post.post_repository import PostRepository


class PostService:

    def __init__(self, repository: PostRepository):
        self.repository = repository

    async def create(self, dto: CreatePostDTO):
        return await self.repository.create(dto)

    async def get_list(self, category_id: int):
        return await self.repository.get_list(category_id)

    async def get(self, post_id: int):
        return await self.repository.get(post_id)

    async def update(self, pk: int, dto: UpdatePostDTO):
        return await self.repository.update(dto, pk)
