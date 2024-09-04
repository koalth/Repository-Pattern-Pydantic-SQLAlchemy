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

    async def get_items_in_price_range(
        self, min_price: float, max_price: float
    ) -> List[Item]:
        return await self.repository.get_all(
            ItemOrm.price >= min_price, ItemOrm.price <= max_price
        )
