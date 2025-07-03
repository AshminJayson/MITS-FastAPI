from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    age: int
    address: str
    is_active: bool


class UpdateUser(BaseModel):
    email: str | None = None
    phone: str | None = None
    address: str | None = None
