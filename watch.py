import asyncio
import motor.motor_asyncio


async def main_async():
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017,localhost:27018,localhost:27019')

    db = client.test_database
    async for change in db.test_collection.watch():
        print(change)


asyncio.run(main_async())