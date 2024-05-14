import asyncio
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

from beanie import Document, Indexed, init_beanie


class Category(BaseModel):
    name: str
    description: str


class Product(Document):
    name: str
    description: Optional[str] = None
    price: Indexed(float)
    category: Category

async def example():
    client = AsyncIOMotorClient("mongodb://localhost:27017")

    await init_beanie(database=client.db_name, document_models=[Product])

    chocolate = Category(
        name="Chocolate", description="A preparation of roasted and ground cacao seeds."
    )

    tonybar = Product(name="Tony's", price=5.95, category=chocolate)

    await tonybar.insert()

    product = await Product.find_one(Product.price < 10)

    print(product)

    await product.set({Product.name: "Gold bar"})

    try:
        all_products: list[Product] = await Product.find_all().to_list()
    except BufferError:
        raise BufferError("Failed with reading from DB.")


if __name__ == "__main__":
    asyncio.run(example())
