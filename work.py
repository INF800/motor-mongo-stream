import asyncio
import motor.motor_asyncio

# URI: 
# 'mongodb://<HOSTNAME>:27017,<HOSTNAME>:27018,<HOSTNAME>:27019/<DBNAME>'
# 
# If on Linux / MacOS add the following to your /etc/hosts file.
# 127.0.0.1  mongo1
# 127.0.0.1  mongo2
# 127.0.0.1  mongo3
# And use localhost as the HOSTNAME
# -----------------------------------------------------------------------------
# not working:
# If on a linux server, use the hostname provided by the docker compose file
# e.g. HOSTNAME = mongo1, mongo2, mongo3
# -----------------------------------------------------------------------------

async def main_async():
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017,localhost:27018,localhost:27019')

    db = client.test_database
    count = 0
    while count < 100:
        document = {'name': f'rob-{count}', 'count': count}
        result = await db.test_collection.insert_one(document)
        print(f'{count}: result %s' % repr(result.inserted_id))
        count += 1
        await asyncio.sleep(5)


asyncio.run(main_async())