"""
Forgetting That asyncio Exceptions Bubble in Weird Ways
Asynchronous Python introduces sneaky failure modes. If you don’t explicitly handle exceptions in asyncio.create_task, you can lose critical error signals. Attackers love hiding in “unobserved task exceptions.”

async def do_stuff():
    raise RuntimeError("Security check failed")

asyncio.create_task(do_stuff())  # Exception swallowed silently!

Fix: Always set exception handlers.
"""

import asyncio


async def do_stuff():
    raise RuntimeError("Security check failed")


async def main():
    # schedule the coroutine while the event loop is running
    task = asyncio.create_task(do_stuff())

    # Option A: await and handle exceptions explicitly
    try:
        await task
    except Exception as e:
        print(f"task failed with exception: {e}")


#task = asyncio.create_task(do_stuff())
#task.add_done_callback(lambda t: t.exception())

if __name__ == "__main__":
    asyncio.run(main())


