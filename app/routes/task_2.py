from typing import Annotated

from fastapi import APIRouter, Body

from core import convert_arabic_to_roman, convert_roman_to_arabic
from models import ConverterResponse


router = APIRouter(tags=["Стажировка"])

"""
Задание_2. Конвертер
    1. Реализовать функции convert_arabic_to_roman() и convert_roman_to_arabic() из пакета app.core
    2. Написать логику и проверки для вводимых данных. Учитывать, что если арабское число выходит за пределы 
    от 1 до 3999, то возвращать "не поддерживается"
    3. Запустить приложение и проверить результат через swagger
"""
@router.post("/converter", description="Задание_2. Конвертер")
async def convert_number(number: Annotated[int | str, Body()]) -> ConverterResponse:
    """
    Принимает арабское или римское число.
    Конвертирует его в римское или арабское соответственно.
    Возвращает первоначальное и полученное числа в виде json:
    {
        "arabic": 10,
        "roman": "X"
    }
    """
    arabic = 0  # переменная для арабского числа
    roman = ''  # переменная для римского числа  

    # проверка типа параметра number и дальнейшее определение чисел
    if isinstance(number, int):
        arabic = number
        roman = convert_arabic_to_roman(number)
    elif isinstance(number, str):
        arabic = convert_roman_to_arabic(number)
        roman = number
    else:
        raise ValueError('Неверный формат')

    converter_response = ConverterResponse(arabic=arabic, roman=roman)

    return converter_response
