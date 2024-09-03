from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List, Generic, TypeVar, Type
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)

class ItemOrm(Base):
    __tablename__ = "items"
    name: Mapped[str]
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    price: Mapped[float]
    
    
    