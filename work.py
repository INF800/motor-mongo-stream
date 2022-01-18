import asyncio
import motor.motor_asyncio


async def main_async():
    # client = motor.motor_asyncio.AsyncIOMotorClient('172.16.238.10', replicaset='rs0') # connect via internal IP
    # client = motor.motor_asyncio.AsyncIOMotorClient('0.0.0.0', port=27018, replicaset='rs0') # connect via external IP (note the port)
    client = motor.motor_asyncio.AsyncIOMotorClient('143.198.72.16', port=27018, replicaset='rs0') # connect via external IP (note the port)

    db = client.test_database
    count = 0
    while count < 100:
        document = {'name': 'rob', 'count': count}
        result = await db.test_collection.insert_one(document)
        print('result %s' % repr(result.inserted_id))
        count += 1
        await asyncio.sleep(5)


asyncio.run(main_async())
