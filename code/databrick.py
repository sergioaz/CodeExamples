from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Create a DataFrame
data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
columns = ["Name", "Value"]
df = spark.createDataFrame(data, columns)

# Show the DataFrame
df.show()

# Perform a basic operation
df.filter(df["Value"] > 1).show()

# Stop the Spark session
spark.stop()