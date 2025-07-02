from fastapi import APIRouter, HTTPException, status

from schemas.user import User
from data.user import users

router = APIRouter(prefix='/users')


@router.get("/{user_id}", response_model=User)
def get_user_data(user_id: int):
    print("Fetching user data with user ID", user_id)
    for user in users:
        if user["id"] == user_id:
            print("User found:", user)
            return user

    raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
