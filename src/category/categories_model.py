from sqlalchemy.orm import Mapped

from src.lib.models.base_model import Base


class CategoryModel(Base):
    __tablename__ = 'category'

    name: Mapped[str]
