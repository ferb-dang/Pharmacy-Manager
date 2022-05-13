from datetime import datetime, timedelta
import time
from click import pass_context
import jwt
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Dict
from passlib.context import CryptContext

from .config import SECRETKEY, ALGORITHM


access_jwt_subject = "access"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Create a function to hash password
def password_hash(password):
    return pwd_context.hash(password, salt=SECRETKEY)


# Create a function to verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# Create a function store JWT token
def token_response(token: str):
    return {"access_token": token}


# Create JWT token using payload, SECRET, ALGORITHM
def sign_jwt(obj):
    payload = {
        "sub": obj,
        "expiry": time.time() + 600
        }
    token = jwt.encode(payload, SECRETKEY, algorithm=ALGORITHM)  # Real JWT token
    return token_response(token)


# Translate JWT token from client
def decode_jwt(token: str):
    try:
        decode_token = jwt.decode(token, SECRETKEY, algorithms=ALGORITHM)
        return decode_token if decode_token["expiry"] >= time.time() else None
    except:
        return {}




# MiddleWare authenticate
class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if (
                not credentials.scheme == "Bearer"
            ):  # If credentials not bearer, it's will raise exception
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token."
                )
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str):
        isTokenValid: bool = False

        try:
            payload = decode_jwt(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid
