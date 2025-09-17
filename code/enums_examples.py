"""
Enums in Python
"""
from enum import Enum, auto

# ============== This automatically assigns 1, 2, 3 to the roles
class UserRole1(Enum):
    ADMIN = auto()
    EDITOR = auto()
    VIEWER = auto()

# ================= Enums with Extra Data
class UserRole2(Enum):
    ADMIN = ("Admin", "Has full access")
    EDITOR = ("Editor", "Can edit content")
    VIEWER = ("Viewer", "Can only view content")

    def __init__(self, display_name, description):
        self.display_name = display_name
        self.description = description

role = UserRole.ADMIN
print(role.display_name)  # Admin
print(role.description)  # Has full access

# ============== Enum with behavior 
class UserRole3(Enum):
    ADMIN = 1
    EDITOR = 2
    VIEWER = 3

    def can_edit(self):
        return self in {UserRole3.ADMIN, UserRole3.EDITOR}

    def can_delete(self):
        return self == UserRole3.ADMIN

# bad :
if role in [UserRole3.ADMIN, UserRole3.EDITOR]:
    print("User can edit content")

# good:
if role.can_edit():
    print("User can edit content")