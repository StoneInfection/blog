from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.lib.models.base_model import Base


class CommentModel(Base):
    __tablename__ = 'comment'

    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=True)
    text: Mapped[str]
    name_user: Mapped[str]
