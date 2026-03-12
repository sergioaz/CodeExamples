"""
Test of mongodb B-tree index performances for uuid4 vs uuid7, based on
https://medium.com/@kanishks772/your-b-tree-index-was-never-designed-for-this-abuse-41dc0bd4cd9d
1. Create collection testHashIdx in mongodb mongodb mongodb://172.24.240.1:27017/ database test_uuid, collection structure: {_id: ObjectId, uuid: String, data: String}
2. create hash index on field uuid
3. Populate collection with 100K documents with random uuid and data, using async mongodb driver and batch inserts (1000 documents per batch)
4. Run 1000 queries on the collection testHashIdx to find documents by uuid and measure the time taken for each query
5. Run 1000 queries on a collection testUuidIdx to find documents by uuid and measure the time taken for each query
"""

import asyncio
from pymongo import AsyncMongoClient
import uuid6
import uuid
import time
import random

async def main():
    # Connect to MongoDB
    client = AsyncMongoClient("mongodb://172.24.240.1:27017/")
    db = client.test_uuid

    # Check if collection exists
    collections = await db.list_collection_names()
    collection4_exists = "testUuid4" in collections

    # Create collection if not exists

    collection_uuid4 = db.testUuid4
    collection_uuid7 = db.testUuid7

    #collection4_exists = False
    if not collection4_exists:
        # Create  indexes on uuid field
        await collection_uuid4.create_index([("uuid")])
        await collection_uuid7.create_index([("uuid")])

        # Populate collection with 100K documents using batch inserts
        uuids = []
        batch_size = 1000
        for batch_start in range(0, 100000, batch_size):
            batch4 = []
            batch7 = []
            for i in range(batch_start, min(batch_start + batch_size, 100000)):
                u4 = str(uuid.uuid4())
                u7 = str(uuid6.uuid7())
                data = f"data_{i}_{random.randint(0, 1000)}"
                doc4 = {"uuid": u4, "data": data}
                doc7 = {"uuid": u7, "data": data}
                batch4.append(doc4)
                batch7.append(doc7)
                uuids.append(u4)  # Use mix of u4 and u7
                uuids.append(u7)  #
            await collection_uuid4.insert_many(batch4)
            await collection_uuid7.insert_many(batch7)
    else:
        # Collection exists, get uuids from existing documents (assuming they have uuid field)
        uuids = []
        async for doc in collection_uuid4.find({}, {"uuid": 1}):
            uuids.append(doc["uuid"])
        async for doc in collection_uuid7.find({}, {"uuid": 1}):
            uuids.append(doc["uuid"])

    # Run 1000 queries on both collections
    if not uuids:
        print("No UUIDs found in collections, skipping performance test.")
        await client.close()
        return

    query_uuids = random.sample(uuids, min(1000, len(uuids)))
    time_uuid4 = []
    time_uuid7 = []

    for u in query_uuids:
        # Query uuid4 index collection
        start = time.perf_counter()
        result = await collection_uuid4.find_one({"uuid": u})
        end = time.perf_counter()
        time_uuid4.append(end - start)

        # Query uuid7 index collection
        start = time.perf_counter()
        result = await collection_uuid7.find_one({"uuid": u})
        end = time.perf_counter()
        time_uuid7.append(end - start)

    # Calculate and compare average query times
    avg_uuid4 = sum(time_uuid4) / len(time_uuid4)
    avg_uuid7 = sum(time_uuid7) / len(time_uuid7)

    print(f"Average query time with uuid4: {avg_uuid4:.6f} seconds")
    print(f"Average query time with uuid7: {avg_uuid7:.6f} seconds")
    print(f"Performance difference: {avg_uuid7 / avg_uuid4:.2f}x faster with uuid7" if avg_uuid4 > avg_uuid7 else f"Performance difference: {avg_uuid4 / avg_uuid7:.2f}x faster with uuid4")

    # Close the client
    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
