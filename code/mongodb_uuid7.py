"""
Code to test uuid index performance in mongodb
Based on https://medium.com/@kanishks772/your-b-tree-index-was-never-designed-for-this-abuse-41dc0bd4cd9d
1. create collection testUuid7Idx in mongodb mongodb://172.24.240.1:27017/ database test_uuid, collection structure: {_id: ObjectId, uuid: String, data: String}
2. create index on field uuid
3. Populate collection with 100K documents with random uuid and data
4. create collection testUuid7NoIdx in mongodb mongodb://172.24.240.1:27017/ database test_uuid, collection structure: {_id: ObjectId, uuid: String, data: String}
5. Populate collection with 100K documents with random uuid and data
6. Run 1000 queries on both collections to find documents by uuid and measure the time taken for each query
7. Compare the average query time for both collections to demonstrate the performance difference between indexed and non-indexed queries on the uuid field.
"""

import asyncio
from pymongo import AsyncMongoClient
import uuid6 as uuid
import time
import random

async def main():
    # Connect to MongoDB
    client = AsyncMongoClient("mongodb://172.24.240.1:27017/")
    db = client.test_uuid

    # Drop collections if they exist
    await db.testUuid7Idx.drop()
    await db.testUuid7NoIdx.drop()

    # Create collections
    collection_idx = db.testUuid7Idx
    collection_no_idx = db.testUuid7NoIdx

    # Create index on uuid field for indexed collection
    await collection_idx.create_index("uuid")

    # Populate collections with 100K documents using batch inserts
    uuids = []
    batch_size = 1000
    for batch_start in range(0, 100000, batch_size):
        batch = []
        for i in range(batch_start, min(batch_start + batch_size, 100000)):
            u = str(uuid.uuid7())
            data = f"data_{i}_{random.randint(0, 1000)}"
            doc = {"uuid": u, "data": data}
            batch.append(doc)
            uuids.append(u)
        await collection_idx.insert_many(batch)
        await collection_no_idx.insert_many(batch)

    # Run 1000 queries on both collections
    query_uuids = random.sample(uuids, 1000)
    times_idx = []
    times_no_idx = []

    for u in query_uuids:
        # Query indexed collection
        start = time.perf_counter()
        result = await collection_idx.find_one({"uuid": u})
        end = time.perf_counter()
        times_idx.append(end - start)

        # Query non-indexed collection
        start = time.perf_counter()
        result = await collection_no_idx.find_one({"uuid": u})
        end = time.perf_counter()
        times_no_idx.append(end - start)

    # Calculate and compare average query times
    avg_idx = sum(times_idx) / len(times_idx)
    avg_no_idx = sum(times_no_idx) / len(times_no_idx)

    print(f"Average query time with index: {avg_idx:.6f} seconds")
    print(f"Average query time without index: {avg_no_idx:.6f} seconds")
    print(f"Performance difference: {avg_no_idx / avg_idx:.2f}x faster with index")

    # Close the client
    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
