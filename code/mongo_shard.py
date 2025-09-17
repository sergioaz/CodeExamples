import random
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["test_database"]
collection = db["test_collection2"]


# Generate and insert 10,000 records
num_records = 1000000

records = [{"key1": i, "key2": random.choice(range(200)), "is_active": random.choice([True, False])} for i in range(0, num_records)]

collection.insert_many(records)

print(f"Inserted {len(records)} records into the collection.")

"""
# Run the query and get both results and query plan
pipeline = [{"$match": {"id": 10000, "is_active": True}}]
query_with_plan = db.command("aggregate", "test_collection", pipeline=pipeline, explain=True)

# Extract results and query plan
query_results = query_with_plan["results"]
query_plan = query_with_plan["stages"]

# Print results and query plan
print("Query Results:", query_results)
print("Query Plan:", query_plan)


# run select query for random id and is_active 10000 times
for _ in range(10000):
    random_id = random.randint(1, 1000000)
    is_active = random.choice([True, False])
    result = collection.find_one({"id": random_id, "is_active": is_active})

    if result:
        print(f"Found record: {result}")
    else:
        print(f"No record found for id: {random_id} and is_active: {is_active}")


# Use $listSampledQueries to retrieve sampled queries
pipeline = [{"$listSampledQueries": {}}]

db_admin = client["admin"]

sampled_queries = db_admin.command("aggregate", "test_database", pipeline=pipeline,     cursor={})

# Print sampled queries
print("Sampled Queries:", sampled_queries)
"""