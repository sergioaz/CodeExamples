"""
https://medium.com/@ThinkingLoop/12-pydantic-v2-model-patterns-youll-reuse-forever-543426b3c003

Master 12 essential Pydantic v2 patterns — validators, computed fields, discriminated unions, TypeAdapter, settings, and more — with copy-ready snippets.
"""


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
1. Baseline DTO ( DATA TRANSFER OBJECT) that plays nicely with everything
Use a single “base” with sane defaults so every model serializes predictably.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from pydantic import BaseModel, ConfigDict

class DTO(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,        # ORM objects → models
        populate_by_name=True,       # allow snake_case + aliases
        extra='forbid',              # fail fast on unknown fields
        str_strip_whitespace=True
    )

class UserDTO(DTO):
    id: int
    email: str
    full_name: str | None = None

# Usage examples:

# 1) Direct construction
user1 = UserDTO(id=1, email="alice@example.com", full_name="Alice")
print("user1:", user1.model_dump())

# 2) From a dict (validation applied)
data = {"id": 2, "email": "bob@example.com"}
user2 = UserDTO.model_validate(data)
print("user2 JSON:", user2.model_dump_json())


# 3) From an ORM-like object (SimpleNamespace) — works because DTO sets from_attributes=True
from types import SimpleNamespace
orm_obj = SimpleNamespace(id=3, email="carol@example.com", full_name="Carol")
user3 = UserDTO.model_validate(orm_obj)
print("user3:", user3.model_dump())

# 4) Extra-field example — will raise a validation error because extra='forbid'
bad = {"id": 4, "email": "dave@example.com", "unexpected": "value"}
try:
    UserDTO.model_validate(bad)
except Exception as exc:
    print("validation error (expected):", exc)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
2) Snake↔camel without pain (alias generator)
APIs love camelCase; Python loves snake_case. Bridge them.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import re
from pydantic import BaseModel, ConfigDict, Field

# def to_camel(s: str) -> str:
#    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), s)

pattern = r'_([a-z])'          # first capturing group = the letter after '_'

def repl(match):
    # match.group(0) -> the entire match (underscore + letter)
    # match.group(1) -> just the captured letter
    return match.group(1).upper()

def to_camel(s: str) -> str:
    return re.sub(pattern, repl, s)


class ApiModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel,
                              populate_by_name=True,
                              extra='forbid')

class Product(ApiModel):
    product_id: int = Field(alias="productId")  # explicit if needed
    unit_price: float

# Usage examples

from pydantic import ValidationError

# 1) Direct construction using snake_case (populate_by_name=True)
p1 = Product(product_id=1, unit_price=9.99)
print("p1:", p1)
print("p1 (snake keys):", p1.model_dump())                # {'product_id': 1, 'unit_price': 9.99}
print("p1 (camel keys):", p1.model_dump(by_alias=True))   # {'productId': 1, 'unitPrice': 9.99}
print("p1 JSON (camel):", p1.model_dump_json(by_alias=True))

# 2) Validate / construct from camelCase payload (e.g. incoming JSON from API)
payload = {"productId": 2, "unitPrice": 19.99}
p2 = Product.model_validate(payload)
print("p2.product_id:", p2.product_id)

# 3) Accept alias-based dicts and still access snake_case attributes
payload2 = {"productId": 3, "unitPrice": 29.95}
p3 = Product.model_validate(payload2)
print("p3:", p3.model_dump())            # default returns snake_case keys

# 4) Handle validation errors (extra fields are forbidden by the DTO base config)
bad = {"productId": 4, "unitPrice": 9.99, "unexpectedField": "x"}
try:
    Product.model_validate(bad)
except ValidationError as exc:
    print("validation error (expected):", exc)

"""    
3) Field validators that do the boring things perfectly
    v2 introduces @field_validator with mode='before'|'after'.
"""

from pydantic import BaseModel, field_validator

class Email(BaseModel):
    address: str

    @field_validator('address', mode='before')
    @classmethod
    def normalize(cls, v: str) -> str:
        v = v.strip().lower()
        if '@' not in v:
            raise ValueError('Invalid email')
        return v

try:
    email = Email(address="srmitin!yahoo.com")
except ValidationError as e:
    # print the error message from the exception and exception type
    print(f"validation error (expected): {e} ({type(e).__name__})")

"""
4) Cross-field sanity with model validators
When one field depends on another, use @model_validator.
"""

from pydantic import BaseModel, model_validator

class Window(BaseModel):
    start: int
    end: int

    @model_validator(mode='after')
    def check_order(self):
        if self.end <= self.start:
            raise ValueError('end must be > start')
        return self

try:
    window = Window(start=10, end=5)
except ValidationError as e:
    print(f"validation error (expected): {e} ")

"""
5) Computed fields for “obvious” derivatives
No need to store what you can derive.
"""

from pydantic import BaseModel, computed_field

class Name(BaseModel):
    first: str
    last: str

    @computed_field
    @property
    def display(self) -> str:
        return f"{self.first.title()} {self.last.title()}"

full_name = Name(first="john",last="doe")
print("full_name.display:", full_name.display)  # "John Doe"

print("Model:", full_name.model_dump())  # Model: {'first': 'john', 'last': 'doe', 'display': 'John Doe'}

"""
6) Serialization that respects clients (and you)
Fine-tune output with field_serializer and model_dump.
"""

from datetime import datetime, timezone
from pydantic import BaseModel, field_serializer

class Event(BaseModel):
    id: str
    at: datetime

    @field_serializer('at')
    def iso8601(self, dt: datetime, _info):
        return dt.astimezone(timezone.utc).isoformat()

e = Event(id='a1', at=datetime.now())
print (e.model_dump(by_alias=True, exclude_none=True))       # tuned output
print (e.model_dump_json())                                   # fast JSON

"""
7) Discriminated unions that make APIs self-describing
Model “one of many” payloads without brittle if/else jungles.
"""
from typing import Annotated, Union, Literal
from pydantic import BaseModel, Field, TypeAdapter

class Click(BaseModel):
    kind: Literal['click']
    x: int; y: int

class Input(BaseModel):
    kind: Literal['input']
    value: str

Event = Annotated[Union[Click, Input], Field(discriminator='kind')]

# Define the adapter for the Event union
event_adapter = TypeAdapter(Event)

# Valid input for Click
click_event = event_adapter.validate_python({"kind": "click", "x": 100, "y": 200})
print(click_event)  # Click(kind='click', x=100, y=200)

# Valid input for Input
input_event = event_adapter.validate_python({"kind": "input", "value": "hello"})
print(input_event)  # Input(kind='input', value='hello')

"""
8) TypeAdapter for validation without a model
Validate arbitrary types (lists, primitives, nested dicts) on the fly.
"""

from typing import List
from pydantic import TypeAdapter

ta = TypeAdapter(List[int])
nums = ta.validate_python(['1', 2, 3])    # → [1, 2, 3]
json_ready = ta.dump_python(nums)         # fast serializer
print ("json_ready:", json_ready)

"""
9) Settings from environment (clean, dry, testable)
Pydantic v2’s BaseSettings makes it easy to load config from env vars or .env files.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='APP_', env_file='.env')
    db_url: str
    debug: bool = False
    cache_ttl: int = 300

# APP_DB_URL=postgres://... python app.py
try:
    settings = AppSettings()  # env + .env merged, types parsed

    print("Database URL:", settings.db_url)
    print("Debug mode:", settings.debug)
    print("Cache TTL:", settings.cache_ttl)
except ValidationError as e:
    print(f"Settings validation error: {e}")

"""
10) ORM interop without ceremony
v2 replaces from_orm=True with from_attributes=True and model_validate.
Pro tip: Use this to produce clean DTOs from ORM rows for your API layer — no leaky models.
"""

from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: str

# SQLAlchemy row ( sa_row) with attributes `.id` and `.email`
# u = User.model_validate(sa_row)

"""
11) Immutable value objects you can trust
Some things should never change after creation — IDs, money, coordinates.
"""

from pydantic import BaseModel, ConfigDict

class Money(BaseModel):
    model_config = ConfigDict(frozen=True)
    amount: int          # cents
    currency: str = 'USD'

m = Money(amount=500)
try:
    m.amount = 600  # ❌ raises error (frozen)
except ValidationError as e:
    print(f"Validation error (expected): {e}")

m2 = m.model_copy(update={'amount': 600})  # ✅ new instance

print (m2)  # Money(amount=600, currency='USD')

"""
12) Validate function calls at the boundary
@validate_call guards service functions like a bouncer at 2 AM.
When to use: API layer, CLI entrypoints, cron tasks — anywhere untrusted data enters your system.
"""

from pydantic import validate_call
from typing import Annotated
from pydantic import Field

@validate_call
def charge(user_id: int, amount: Annotated[float, Field(gt=0)]):
    # if we're here, inputs are clean
    return {'ok': True}

charge(42, '9.99')  # ✅ becomes 9.99 (coerced & validated)
try:
    charge(42, '-5')  # ❌ raises ValidationError (amount must be > 0)
except ValidationError as e:
    print(f"Validation error (expected): {e}")
# charge('u1', -5)  # ❌ raises ValidationError


