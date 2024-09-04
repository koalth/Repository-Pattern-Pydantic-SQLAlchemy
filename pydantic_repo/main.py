import asyncio
from .service import ItemService
from .entity import ItemUpdate, Item, ItemCreate

async def main():

    item_1 = ItemCreate(name="item_one", description="This is a cool item", price=23.00)
    item_2 = ItemCreate(name="item_two", description="this is another cool item", price=4.00)
    item_3 = ItemCreate(name="item_three", price=50.00)

    itemService = ItemService()

    item_1_ent = await itemService.create(item_1)
    print(item_1_ent)

    test_item = await itemService.get(item_1_ent.id)
    print(test_item)

    assert item_1_ent == test_item

def run():
    asyncio.run(main())
