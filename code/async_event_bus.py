import asyncio

class EventBus:
    def __init__(self):
        self.handlers = {}

    def on(self, event_name):
        def decorator(func):
            self.handlers.setdefault(event_name, []).append(func)
            return func
        return decorator

    async def emit(self, event_name, *args, **kwargs):
        for handler in self.handlers.get(event_name, []):
            await handler(*args, **kwargs)

bus = EventBus()

@bus.on("user_signed_up")
async def send_email(user):
    print(f"Sending email to {user}")

@bus.on("user_signed_up")
async def log_signup(user):
    print(f"Logging signup for {user}")

asyncio.run(bus.emit("user_signed_up", "alice@example.com"))