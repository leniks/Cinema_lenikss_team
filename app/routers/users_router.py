from fastapi import APIRouter, HTTPException, status
from app.services.auth_service import get_password_hash
from app.services.users_service import UserService
from app.schemas.User_schema import RegisterUser


router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post("/register/")
async def register_user(user_data: RegisterUser) -> dict:
    user = await UserService.get_user_or_none_by_email(user_email=user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )
    user_dict = user_data.dict()
    user_dict['password'] = get_password_hash(user_data.password)
    await UserService.add_user(**user_dict)
    return {'message': 'Вы успешно зарегистрированы!'}