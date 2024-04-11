from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

from app_init import app


# класс пользовательского исключения для ошибок
class CustomException(HTTPException):
    def __init__(self, detail: str, status_code: int = 400):
        super().__init__(status_code=status_code, detail=detail)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Глобальная функция реакции на неизвестную ошибку.

    Args:
        request (Request): request
        exc (Exception): unpredicted exception

    Returns:
        _type_: json response
    """
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )
