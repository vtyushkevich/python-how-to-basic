from pydantic import BaseModel, constr, Field
from typing import List
from uuid import uuid4


class UserBase(BaseModel):
    username: constr(min_length=3) = Field(..., example="Vadim")


class UserIn(UserBase):
    pass


class UserOut(UserBase):
    id: int = Field(..., example=1)


def generate_token():
    return str(uuid4())


class User(UserOut):
    token: str = Field(default_factory=generate_token)
