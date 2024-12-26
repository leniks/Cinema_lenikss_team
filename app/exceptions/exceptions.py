from fastapi import HTTPException


class TokenExpiredException(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail='Токен истек')


class NoJwtException(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail='Token not found')


class NoUserIdException(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail='Не найден ID пользователя')


class ForbiddenException(HTTPException):
    def __init__(self):
        super().__init__(status_code=403, detail='Access forbidden')
