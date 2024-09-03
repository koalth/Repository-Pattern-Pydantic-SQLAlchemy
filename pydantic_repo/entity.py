from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import Optional, List, Generic, TypeVar, Type
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeMeta


class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    
class Item(ItemBase):
    id: UUID
    
    model_config = ConfigDict(from_attributes=True)