from fastapi import HTTPException, status, Request
from .token import verify_token


def get_current_user(request: Request):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    return verify_token(request, credentials_exception)