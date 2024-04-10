from fastapi import APIRouter, UploadFile

from core import average_age_by_position
from .exception import CustomException


router = APIRouter(tags=["Стажировка"])

"""
Задание_4. Работа с pandas и csv. 

В модуле app.core реализуйте функцию average_age_by_position(), 
которая принимает на вход CSV файл с данными о сотрудниках компании. 

В файле должны быть следующие колонки: "Имя", "Возраст", "Должность". 
Функция должна вернуть словарь, в котором ключами являются уникальные
должности, а значениями — средний возраст сотрудников на каждой должности. 
Для чтения и работы с csv файлами, нужно использовать библиотеку pandas.

Пример CSV файла (employees.csv): 
Имя,Возраст,Должность
Алексей,25,Разработчик
Мария,30,Менеджер
Иван,28,Разработчик
Анна,35,Менеджер


Роут так же должен принимать на входе csv файл.
Пример ответа:
{
    "Разработчик": 26.5,
    "Менеджер": 32.5
}

Рекомендуется добавить аннотации типов. Также добавьте исключения, если файл
приходит не валидный, например, 
неправильный формат файла, названия столбцов отличаются и т.д. 
В таких случаях ожидается строка с ошибкой и status code 400.
"""
@router.post("/get_average_age_by_position",
             description="Задание_4. Работа с pandas и csv")
async def get_average_age_by_position(file: UploadFile) -> dict[str, float | int]:
    """Функция-обработчик файла-таблицы сотрудников.
    Обрабатывает получаемый файл в csv формате и выдаёт словарь,
    в котором указан средний возраст среди сотрудников по их должностями.
    """
    fct = file.content_type
    
    csv_types = ('text/x-csv', 'application/vnd.ms-excel',
                 'application/csv', 'application/x-csv',
                 'text/csv', 'text/comma-separated-values',
                 'text/x-comma-separated-values', 'text/tab-separated-values')
    
    if fct not in csv_types:
        raise CustomException(detail='Bad file type. Except csv type.',
                              status_code=400)
    
    result = average_age_by_position(file.file)
    
    return result
