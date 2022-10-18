import os
import secrets
from dotenv import load_dotenv
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, status, HTTPException

security = HTTPBasic()
load_dotenv('.env')

AUTH_USER = os.getenv('AUTH_USER')
AUTH_PASS = os.getenv('AUTH_PASS')

def current_user(credentials: HTTPBasicCredentials = Depends(security)):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = str.encode(AUTH_USER)
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = str.encode(AUTH_PASS)

    correct_username = secrets.compare_digest(current_username_bytes, correct_username_bytes)
    correct_password = secrets.compare_digest(current_password_bytes, correct_password_bytes)

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid credentials",
            headers = {"WWW-Authenticate": "Basic"}
        )
    return { "username": credentials.username, "password": credentials.password}