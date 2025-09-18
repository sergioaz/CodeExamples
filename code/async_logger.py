import logging.handlers
import queue
import time

# import threading

log_queue = queue.Queue(-1)

queue_handler = logging.handlers.QueueHandler(log_queue)
queue_listener = logging.handlers.QueueListener(log_queue, logging.StreamHandler())

logger = logging.getLogger("async_logger")
logger.addHandler(queue_handler)
logger.setLevel(logging.DEBUG)

queue_listener.start()
logger.info("Non-blocking logging in action")
time.sleep(1)
queue_listener.stop()  # Ensure all logs are processed before exit