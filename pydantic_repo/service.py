from .repository import GenericRepository
from .model import ItemOrm
from .entity import Item, ItemCreate, ItemUpdate
from uuid import UUID
from typing import List

class ItemRepository(GenericRepository[ItemOrm, ItemCreate, ItemUpdate, Item]):
    def __init__(self):
        super().__init__(ItemOrm, Item)
        
class ItemService:
    
    itemRepository: ItemRepository = ItemRepository()
    
    async def create_item(self, item: ItemCreate) -> Item:
        return await self.itemRepository.create(item)
    
    async def get_item(self, id: UUID) -> Item:
        return await self.itemRepository.get(id)
    
    async def get_items_by_price_range(self, min_price: float, max_price: float) -> List[Item]:
        return await self.itemRepository.get_all(
            ItemOrm.price >= min_price,
            ItemOrm.price <= max_price
        )
    
    async def update_item(self, id: UUID, item_update: ItemUpdate) -> Item:
        return await self.itemRepository.update(id, item_update)
    
    async def delete_item(self, id: UUID) -> None:
        await self.itemRepository.delete(id)