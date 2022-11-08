from typing import List
from fastapi import HTTPException, Depends
from .oauth2 import get_current_user
from models.tbl_users import User

class RoleChecker:
    def __init__(self, allowed_roles: List):
        self.allowed_roles = allowed_roles

    def __call__(self, user: User = Depends(get_current_user)):

        if not user:
            raise HTTPException(
                status_code=403,
                detail="Operation not permitted"
            )

        if user.get("role") not in self.allowed_roles:
            raise HTTPException(
                status_code=403,
                detail="Operation not permitted"
            )

superadmin = RoleChecker(["superadmin"])
manager = RoleChecker(["superadmin", "manager"])
user = RoleChecker(["superadmin", "manager", "user"])