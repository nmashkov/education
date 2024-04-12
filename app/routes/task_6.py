import uuid

from fastapi import APIRouter

from core import DataGenerator
from models import Task6

router = APIRouter(tags=["API для хранения файлов"])

"""
Задание_6. 

Изучите следущие классы в модуле app.core: BaseWriter, DataGenerator

API должно принимать json, по типу:
{
    "file_type": "json",  # или "csv", "yaml"
    "matrix_size": int    # число от 4 до 15
}
В ответ на удачную генерацию файла должен приходить id для скачивания.

Добавьте реализацию методов класса DataGenerator.
Добавьте аннотации типов и (если требуется) модели в модуль app.models.

(Подумать, как переисползовать код из задания 5)
"""
@router.post("/generate_file", description="Задание_6. Конвертер")
async def generate_file(data: Task6) -> int:
    """Описание."""
    file_type = data.file_type
    matrix_size = data.matrix_size
    new_name = str(uuid.uuid4())[:8]

    new_data = DataGenerator()
    new_data.generate(matrix_size)
    new_data.to_file(path=new_name, writer=file_type)
    file_id: int = new_data.file_id

    return file_id
