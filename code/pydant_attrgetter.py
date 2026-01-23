from datetime import datetime, timedelta
from pydantic import BaseModel, Field
"""
squared = list(map(lambda x: x ** 2, range(5)))
squared = list(lambda x: x ** 2, range(5))
print (squared)
"""

class User (BaseModel):
    username: str = Field (..., description = "User name")
    last_login: datetime = Field(..., description="Last login timestamp")

users = []
users.append(User(username="user1", last_login=datetime.now()))
users.append(User(username="user2", last_login=datetime.now() - timedelta(hours=1)))

from operator import attrgetter

print (f"Users before sort: {users=}")

users.sort(key=attrgetter("last_login"))

print (f"Users after sort : {users=}")

