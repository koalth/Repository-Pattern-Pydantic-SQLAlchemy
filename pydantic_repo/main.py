import asyncio
from .service import ItemService
from .entity import ItemUpdate, Item, ItemCreate

async def main():

    item_1 = ItemCreate(name="item_one", description="This is a cool item", price=23.00)
    item_2 = ItemCreate(name="item_two", description="this is another cool item", price=4.00)
    item_3 = ItemCreate(name="item_three", price=50.00)

    itemService = ItemService()

    # await itemService.create(item_1)
    # await itemService.create(item_2)
    # await itemService.create(item_3)

    items = await itemService.get_items_in_price_range(3.00, 49.00)

    print(items)


def run():
    asyncio.run(main())
