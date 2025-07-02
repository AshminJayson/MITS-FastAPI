from fastapi import APIRouter, HTTPException, status

from schemas.user import User
from data.user import users

router = APIRouter(prefix="/users")


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user['id'] == user_id:
            return user

    raise HTTPException(status.HTTP_404_NOT_FOUND, "User Not Found")
