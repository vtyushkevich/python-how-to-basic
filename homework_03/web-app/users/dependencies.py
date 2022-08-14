from fastapi import Header, HTTPException, status
from . import crud
from .schemas import User


def get_user_by_token(
        token: str = Header(
            ...,
            description="User Auth Token",
            alias="x-auth-token",
        ),
):
    user = crud.get_user_by_token(token)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Auth Token",
    )
