"""
task.add_done_callback registers a regular (non-async) callable to run when the Task finishes. The callback is called with the finished Task as its single argument. Common uses: consume Task.exception() to avoid warnings, log errors, or schedule follow-up coroutines with asyncio.create_task. Callbacks run in the event loop thread and should not block.
Example showing silent consumption, logging, and scheduling an async follow-up:
"""
# python
import asyncio
import logging

logging.basicConfig(level=logging.ERROR)

async def failing():
    raise RuntimeError("boom")

def silent_consumer(t: asyncio.Task):
    try:
        t.exception()
    except asyncio.CancelledError:
        pass

def log_consumer(t: asyncio.Task):
    try:
        exc = t.exception()
    except asyncio.CancelledError:
        return
    if exc is not None:
        # Log the actual exception object rather than relying on sys.exc_info()
        logging.error("background task failed", exc_info=(type(exc), exc, exc.__traceback__))

def schedule_followup(t: asyncio.Task):
    try:
        exc = t.exception()
    except asyncio.CancelledError:
        return
    # Pass the exception into the follow-up task to avoid re-raising inside it
    asyncio.create_task(handle_result(exc))

async def handle_result(exc: Exception | None):
    if exc is None:
        return
    # Log the exception received from the original task
    logging.error("handled in follow-up", exc_info=(type(exc), exc, exc.__traceback__))

async def main():
    t1 = asyncio.create_task(failing())
    t1.add_done_callback(silent_consumer)

    t2 = asyncio.create_task(failing())
    t2.add_done_callback(log_consumer)

    t3 = asyncio.create_task(failing())
    t3.add_done_callback(schedule_followup)

    await asyncio.sleep(0.1)  # let tasks run

if __name__ == "__main__":
    asyncio.run(main())
