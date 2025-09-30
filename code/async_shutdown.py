import signal
import asyncio
import sys

async def main():
    print("Starting service...")
    loop = asyncio.get_running_loop()

    stop_event = asyncio.Event()

    def shutdown():
        if not stop_event.is_set():
            print("Received shutdown signal.")
            stop_event.set()

    if sys.platform != "win32":
        loop.add_signal_handler(signal.SIGINT, shutdown)
        loop.add_signal_handler(signal.SIGTERM, shutdown)

    try:
        await stop_event.wait()
    except (asyncio.CancelledError, KeyboardInterrupt):
        shutdown()
    finally:
        print("Shutdown complete.")

try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
