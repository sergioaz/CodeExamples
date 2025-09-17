"""
uv pip install patterns
"""

"""
Strategy — choosing behavior at runtime
The Strategy pattern allows you to define a family of algorithms and switch between them dynamically.
"""
from pytterns import strategy, load

@strategy("payment")
class CreditCardPayment:
    def check(self, method):
        return method == "credit_card"
        #return method == "paypal"

    def execute(self):
        return "Processing payment via Credit Card"


@strategy("payment")
class PayPalPayment:
    def check(self, method):
        return method == "paypal"

    def execute(self):
        return "Processing payment via PayPal"


payment_strategy = load.strategy("payment").check("paypal").execute()
print(payment_strategy)  # Processing payment via PayPal

"""
Chain of Responsibility — processing requests in sequence
This pattern allows a request to pass through a chain of handlers, each responsible for a specific step in the process.
"""

from pytterns import chain, load

@chain("auth_chain", order=1)
class Authenticator:
    def handle(self, request):
        if not request.get("authenticated", False):
            print("Authentication failed!")
            return
        print("User authenticated")

@chain("auth_chain", order=2)
class Authorizer:
    def handle(self, request):
        if request.get("role") != "admin":
            print("Authorization failed!")
            return
        print("User authorized")

@chain("auth_chain", order=3)
class Logger:
    def handle(self, request):
        print(f"Logging request: {request}")

auth_chain = load.chain("auth_chain")
auth_chain.handle({"authenticated": True, "role": "admin"})

"""
Observer — reacting to events
The Observer pattern lets you register listeners for an event and notify them later.
"""

from pytterns import observer, load

@observer('user.created')
def send_welcome_email(user_id):
    print(f"send welcome to {user_id}")
    return 'email_sent'

@observer('user.created')
class AuditListener:
    def update(self, user_id):
        print(f"audit: created {user_id}")
        return 'audited'

results = load.observer('user.created').notify(42)
print(results)  # [(True, 'email_sent'), (True, 'audited')]

results = load.observer('user.created')
print(results)
results.notify(43)

"""
Factory — creating objects dynamically
The Factory pattern centralizes the creation of objects without exposing instantiation details.
"""

from pytterns import factory, load

@factory('db')
class MyDB:
    def __init__(self, dsn):
        self.dsn = dsn

inst = load.factory('db').create('sqlite:///:memory:')
print(inst.dsn)


"""
Command — encapsulating actions as objects
The Command pattern maps commands to handlers (functions or classes) that can be executed on demand.

Benefit: decouples the caller from the executor and enables features like undo/redo, queuing, or scheduling commands.
"""

from pytterns import command, load

@command('say')
def say(msg):
    print(msg)
    return msg

@command('say')
class Loud:
    def execute(self, msg):
        print(msg.upper())
        return "Loud!"

res = load.command('say').execute('hello')
print (f"{res=}")