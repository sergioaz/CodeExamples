"""
https://medium.com/@ThinkingLoop/12-pydantic-v2-model-patterns-youll-reuse-forever-543426b3c003

Master 12 essential Pydantic v2 patterns — validators, computed fields, discriminated unions, TypeAdapter, settings, and more — with copy-ready snippets.
"""


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
1. Baseline DTO that plays nicely with everything
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
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

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