from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.lib.models.base_model import Base


class PostModel(Base):
    __tablename__ = 'post'

    title: Mapped[str]
    text: Mapped[str]
    name_user: Mapped[str]
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'), nullable=True)
    comments = relationship("CommentModel", lazy='raise_on_sql')
