import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s - %(request_id)s',
)

# Get a logger instance
logger = logging.getLogger(__name__)

def process_data(data, request_id):
    """Processes data and logs information with a request ID."""
    logger.info(f"Processing data: {data}", extra={'request_id': request_id})
    # Perform data processing logic here
    logger.info("Data processing complete", extra = {})

if __name__ == "__main__":
    process_data("example data", "12345")
