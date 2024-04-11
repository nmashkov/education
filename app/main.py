from app_init import app
from routes.task_1 import router as r_1
from routes.task_2 import router as r_2
from routes.task_3 import router as r_3
from routes.task_4 import router as r_4
from routes.task_5 import router as r_5
from routes.task_6 import router as r_6
from routes.task_7 import CustomMiddleware
from routes.task_8 import router as r_8
from routes.task_11 import router as r_11


app.add_middleware(CustomMiddleware)

app.include_router(r_1)
app.include_router(r_2)
app.include_router(r_3)
app.include_router(r_4)
app.include_router(r_5)
app.include_router(r_6)
app.include_router(r_8)
app.include_router(r_11)
