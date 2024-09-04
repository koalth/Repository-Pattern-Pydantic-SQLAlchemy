from .repository import GenericRepository, GenericService
from .model import ItemOrm
from .entity import Item, ItemCreate, ItemUpdate
from uuid import UUID
from typing import List, Generic, TypeVar, Type


class ItemRepository(GenericRepository[ItemOrm, ItemCreate, ItemUpdate, Item]):
    def __init__(self):
        super().__init__(ItemOrm, Item)


class ItemService(GenericService[ItemOrm, ItemCreate, ItemUpdate, Item]):
    repository = ItemRepository()
