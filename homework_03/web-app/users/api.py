from fastapi import APIRouter, HTTPException, status, Depends
from typing import List

from .schemas import UserIn, UserOut, User
from .dependencies import get_user_by_token

from . import crud

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=List[UserOut])
def list_users():
    return crud.list_users()


@router.post("", response_model=UserOut)
def create_user(user_in: UserIn):
    return crud.create_users(user_in=user_in)


@router.get("/me", response_model=UserOut)
def get_me(user: User = Depends(get_user_by_token)):
    return user


@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int):
    user = crud.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"from user #{user_id} not found",
    )
    # return crud.get_user_by_id(user_id)
