from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse

from core import get_actual_file_table, save_file
from core.exception import CustomException


router = APIRouter(tags=["API для хранения файлов"])

"""
Задание_5. API для хранения файлов

a.	Написать API для добавления(POST) "/upload_file" и
    скачивания (GET) "/download_file/{id}" файлов. 
В ответ на удачную загрузку файла должен приходить id для скачивания. 
b.	Добавить архивирование к post запросу, то есть файл должен сжиматься и
    сохраняться в ZIP формате.
с*.Добавить аннотации типов.
"""
@router.post("/upload_file",
             description="Задание_5. API для хранения файлов")
async def upload_file(file: UploadFile = File(...)) -> int:
    """Функция загрузки файлов."""
    # get files table
    table = get_actual_file_table()
    # check file existing
    fname = file.filename
    id = None
    if fname not in table.values():
        if len(table) > 0:
            last_id = list(table.keys())[-1]
            id = int(last_id) + 1
        else:
            id = 0
        table[id] = fname
        save_file(table, file)
    else:
        raise CustomException(detail='Файл с таким именем уже есть на сервере',
                              status_code=400)
    # return id of uploaded file
    return id


@router.get("/download_file/{file_id}",
            description="Задание_5. API для хранения файлов")
async def download_file(file_id: int) -> FileResponse:
    """Функция скачивания файлов по их id."""
    # get files table
    table = get_actual_file_table()
    # check file existing
    id = None
    if str(file_id) not in table.keys():
        raise CustomException(detail='Файл отсутствует на сервере.',
                              status_code=400)
    else:
        id = str(file_id)
    # get file path
    f_name = table[id]
    f_path = f'./files/temp/{f_name}'
    # return file
    return FileResponse(path=f_path,
                        filename=f_name)
