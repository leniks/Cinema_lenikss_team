from fastapi import APIRouter, HTTPException, status, Response, Depends

from app.services.auth_service import get_password_hash
from app.services.users_service import UserService
from app.services.dependencies_service import create_access_token, get_current_user

from app.schemas.User_schema import RegisterUser, AuthUser

from app.models.User import User

router = APIRouter(prefix='/auth', tags=['Авторизация / Аутентификация'])


@router.post("/register/")
async def register_user(user_data: RegisterUser) -> dict:
    user = await UserService.get_user_or_none_by_email(user_email=user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )
    user_dict = user_data.dict()
    user_dict['hashed_password'] = get_password_hash(user_data.password)
    del user_dict['password']
    await UserService.add_user(**user_dict)
    return {'message': 'Вы успешно зарегистрированы!'}


@router.post("/login/")
async def auth_user(response: Response, user_data: AuthUser):
    check = await UserService.authenticate_user(email=user_data.email, password=user_data.password)
    if check is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Неверная почта или пароль')
    access_token = create_access_token({"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}


@router.get("/me/")
async def get_me(user_data: User = Depends(get_current_user)):
    return user_data

