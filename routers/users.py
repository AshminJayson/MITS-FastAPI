import random
from fastapi import APIRouter, HTTPException, status, Form

from schemas.user import User, UpdateUser
from data.user import users

router = APIRouter(prefix="/users")


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user['id'] == user_id:
            return user

    raise HTTPException(status.HTTP_404_NOT_FOUND, "User Not Found")


@router.post("/", response_model=User)
def create_user(name: str = Form(...), email: str = Form(...), phone: str = Form(...), address: str = Form(...), age: int = Form(...)):
    new_user = {
        "id": random.randint(50, 1000),
        "name": name,
        "age": age,
        "phone": phone,
        "address": address,
        "email": email,
        "is_active": True
    }

    users.append(new_user)
    return new_user


@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, up_info: UpdateUser):
    for idx, user in enumerate(users):
        if user['id'] == user_id:
            if up_info.phone is not None:
                user['phone'] = up_info.phone
            if up_info.address is not None:
                user['address'] = up_info.address
            if up_info.email is not None:
                user['email'] = up_info.email

            users[idx] = user
            return user

    raise HTTPException(status.HTTP_404_NOT_FOUND, "user not found")


@router.delete("/{user_id}")
def delete_user(user_id: int):
    validIndex = -1
    for idx, user in enumerate(users):
        if user['id'] == user_id:
            validIndex = idx
            break

    if validIndex == -1:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not Found")
    else:
        users.pop(validIndex)
        return {"message": "User successfully deleted"}
