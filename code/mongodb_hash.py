"""
Test of mongodb hash index performance for high-cardinality field based on
https://medium.com/@kanishks772/your-b-tree-index-was-never-designed-for-this-abuse-41dc0bd4cd9d
1. Create collection testHashIdx in mongodb mongodb mongodb://172.24.240.1:27017/ database test_uuid, collection structure: {_id: ObjectId, uuid: String, data: String}
2. create hash index on field uuid
3. Populate collection with 100K documents with random uuid and data, using async mongodb driver and batch inserts (1000 documents per batch)
4. Run 1000 queries on the collection testHashIdx to find documents by uuid and measure the time taken for each query
5. Run 1000 queries on a collection testUuidIdx to find documents by uuid and measure the time taken for each query
"""

import asyncio
from pymongo import AsyncMongoClient
import uuid
import time
import random

async def main():
    # Connect to MongoDB
    client = AsyncMongoClient("mongodb://172.24.240.1:27017/")
    db = client.test_uuid

    # Check if collection exists
    collections = await db.list_collection_names()
    collection_exists = "testHashIdx" in collections

    # Create collection if not exists
    collection_hash = db.testHashIdx

    if not collection_exists:
        # Create hashed index on uuid field
        await collection_hash.create_index([("uuid", "hashed")])

        # Populate collection with 100K documents using batch inserts
        uuids = []
        batch_size = 1000
        for batch_start in range(0, 100000, batch_size):
            batch = []
            for i in range(batch_start, min(batch_start + batch_size, 100000)):
                u = str(uuid.uuid4())
                data = f"data_{i}_{random.randint(0, 1000)}"
                doc = {"uuid": u, "data": data}
                batch.append(doc)
                uuids.append(u)
            await collection_hash.insert_many(batch)
    else:
        # Collection exists, get uuids from existing documents (assuming they have uuid field)
        uuids = []
        async for doc in collection_hash.find({}, {"uuid": 1}):
            uuids.append(doc["uuid"])

    # Get the B-tree indexed collection
    collection_btree = db.testUuidIdx

    # Run 1000 queries on both collections
    query_uuids = random.sample(uuids, min(1000, len(uuids)))
    times_hash = []
    times_btree = []

    for u in query_uuids:
        # Query hashed index collection
        start = time.perf_counter()
        result = await collection_hash.find_one({"uuid": u})
        end = time.perf_counter()
        times_hash.append(end - start)

        # Query B-tree index collection
        start = time.perf_counter()
        result = await collection_btree.find_one({"uuid": u})
        end = time.perf_counter()
        times_btree.append(end - start)

    # Calculate and compare average query times
    avg_hash = sum(times_hash) / len(times_hash)
    avg_btree = sum(times_btree) / len(times_btree)

    print(f"Average query time with hashed index: {avg_hash:.6f} seconds")
    print(f"Average query time with B-tree index: {avg_btree:.6f} seconds")
    print(f"Performance difference: {avg_btree / avg_hash:.2f}x faster with hashed index" if avg_hash < avg_btree else f"Performance difference: {avg_hash / avg_btree:.2f}x faster with B-tree index")

    # Close the client
    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
