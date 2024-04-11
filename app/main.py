from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from routes.task_1 import router as r_1
from routes.task_2 import router as r_2
from routes.task_3 import router as r_3
from routes.task_4 import router as r_4
from routes.task_5 import router as r_5
from routes.task_6 import router as r_6
from routes.task_7 import CustomMiddleware
from routes.task_8 import router as r_8


app = FastAPI()


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
        content={"error": "ЛУЛУЛУЛ Internal server error"}
    )


app.add_middleware(CustomMiddleware)

app.include_router(r_1)
app.include_router(r_2)
app.include_router(r_3)
app.include_router(r_4)
app.include_router(r_5)
app.include_router(r_6)
app.include_router(r_8)
