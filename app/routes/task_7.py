import logging
import time
from contextvars import ContextVar

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


# logger settings
logging.basicConfig(filename='./files/middleware.logs',
                    filemode='a',
                    format='[%(asctime)s] {%(name)s: %(lineno)s} '
                           '%(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.DEBUG)
output_log = logging.getLogger("output")

client_host: ContextVar[str | None] = ContextVar("client_host", default=None)

"""
Задание_7. Логирование в FastAPI с использованием middleware.

Написать конфигурационный файл для логгера "output"
Формат выводимых логов:
[CURRENT_DATETIME] {file: line} LOG_LEVEL - | EXECUTION_TIME_SEC | HTTP_METHOD | URL | STATUS_CODE |
[2023-12-15 00:00:00] {example:62} INFO | 12 | GET | http://localhost/example | 200 |

Дописать класс CustomMiddleware.
Добавить middleware в приложение (app).
"""
class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        """Load request ID from headers if present. Generate one otherwise."""
        client_host.set(request.client.host)
        # start time counter
        start_time = time.time()
        # execute fastapi function
        response = await call_next(request)
        # for bad request see main.py global_exception_handler function
        # stop time counter and form output data
        end_time = time.time()
        duration = end_time - start_time
        data = (f"| {int(round(duration))} | {request.method} "
                f"| {request.url} | {response.status_code} |")
        # print log to cmd and app/files/middleware.logs
        output_log.info(data)
        print(f'LOGGER-> {data}')

        return response
