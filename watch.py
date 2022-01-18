import asyncio
import motor.motor_asyncio


async def main_async():
    # client = motor.motor_asyncio.AsyncIOMotorClient('172.16.238.10', replicaset='rs0')  # connect via internal IP
    # client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://172.16.238.10:27017/?replicaSet=rs0')  # connect via internal IP
    # client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://0.0.0.0:27018/?replicaSet=rs0')  # connect via external IP (note the port)
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://143.198.72.16:27018/?replicaSet=rs0')  # connect via external IP (note the port)

    db = client.test_database
    async for change in db.test_collection.watch():
        print(change)


asyncio.run(main_async())
