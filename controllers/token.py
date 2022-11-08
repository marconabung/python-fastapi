from fastapi import Request, status
from fastapi.responses import RedirectResponse
from datetime import datetime, timedelta
from jose import JWTError, jwt
from configs.env import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    to_encode = data.copy()    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_token(request: Request, credentials_exception):
    try:
        token = request.cookies.get("access_token")
        if not token:
            return None

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        role: str = payload.get("role")
        name: str = payload.get("name")

        if not name:
            return None
        
        token_data = {
            "role": role,
            "name": name
        }

        return token_data

    except JWTError as e:
        raise credentials_exception