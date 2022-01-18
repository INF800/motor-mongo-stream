import asyncio
import motor.motor_asyncio


async def main_async():
    # client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017,localhost:27018,localhost:27019')

    # the slash `/` after ip address is important.
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://143.198.72.16/:27017,143.198.72.16/:27018,143.198.72.16/:27019')

    db = client.test_database
    async for change in db.test_collection.watch():
        print(change)


asyncio.run(main_async())