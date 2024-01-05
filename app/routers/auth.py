from fastapi import APIRouter, HTTPException, status
from app.utils import create_jwt_token, pwd_context
from app.models import User, UserPydantic
from app.schemas import UserRegistration, UserLogin


auth_router = APIRouter()


@auth_router.post("/register", response_model=UserPydantic)
async def register(user: UserRegistration):
    hashed_password = pwd_context.hash(user.password)
    user_data = user.model_dump()
    user_data['password'] = hashed_password
    user_data['password_confirmation'] = hashed_password
    new_user = await User.create(**user_data)
    return await UserPydantic.from_tortoise_orm(new_user)


@auth_router.post('/login', response_model=dict)
async def login_user(user: UserLogin):
    """Авторизация пользователя"""
    authenticated_user = await User.get(email=user.email_phone_number)
    if authenticated_user is None or not pwd_context.verify(user.password, authenticated_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
            )
    token_data = {"sub": str(authenticated_user.id)}
    token = await create_jwt_token(token_data)
    return {"access_token": token, "token_type": "bearer"}
