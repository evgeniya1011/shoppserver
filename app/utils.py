import os
from dotenv import load_dotenv
from jose import JWTError, jwt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta

from passlib.context import CryptContext
from starlette import status
from tortoise import Tortoise
from tortoise.contrib.fastapi import HTTPNotFoundError
from pathlib import Path

from app.models import User
import dotenv

from tortoise_config import SECRET_KEY

# dotenv.load_dotenv()
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# SECRET_KEY = os.getenv('SECRET_KEY')


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     """Получение текущего пользователя"""
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])  #декодирование кода
#         email: str = payload.get("sub")
#         if email is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception
#
#     user = await User.get_or_none(email=email)
#     if user is None:
#         raise credentials_exception
#     return user


# async def authenticate_user(current_user: User = Depends(get_current_user)):
#     return current_user


async def create_jwt_token(data: dict, expires_delta=timedelta(minutes=30)):
    """Создание JWT-tokena"""
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256") #кодирование словаря в строку JWt
    return encoded_jwt

#
# async def create_token(user: User):
#     expires = timedelta(minutes=30)
#     access_token_expires = datetime.utcnow() + expires
#     access_token = await create_jwt_token(
#         data={"sub": user.email, "scopes": []},
#         expires_delta=expires,
#     )
#     token = await Token.create(user=user, access_token=access_token, expires_at=access_token_expires)
#     return token


# def verify_token(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])  #декодирование кода
#         user_id: int = payload.get("sub")
#         if user_id is None:
#             raise credentials_exception
#         return user_id
#     except JWTError:
#         raise credentials_exception


# async def get_current_user(token: str = Depends(verify_token)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     user_id = int(token.split("_")[1])
#     user = await User.get(id=user_id)
#     if user is None:
#         raise credentials_exception
#     return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
# async def get_current_user(token: str = Depends(create_jwt_token)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await User.get_or_none(id=user_id)
    if user is None:
        raise credentials_exception
    return user


async def authenticate_user(current_user: User = Depends(get_current_user)):
    return current_user


