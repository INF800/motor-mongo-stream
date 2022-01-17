import asyncio
import motor.motor_asyncio


async def main_async():
    # client = motor.motor_asyncio.AsyncIOMotorClient('172.16.238.10', replicaset='rs0')
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://172.16.238.10:27017/?replicaSet=rs0')
    db = client.test_database
    async for change in db.test_collection.watch():
        print(change)


asyncio.run(main_async())