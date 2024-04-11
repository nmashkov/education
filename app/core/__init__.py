from abc import ABC, abstractmethod
from io import StringIO
from typing import Annotated
import json

from fastapi import UploadFile, File
import pandas as pd

from routes.exception import CustomException


def encode_digit(digit: int, one: str, five: str, nine: str) -> str:
    """Вспомогательная функция для конкатенации римских цифр.

    Args:
        digit (_type_): число
        one (_type_): первый римский символ
        five (_type_): второй римский символ
        nine (_type_): третий римский символ

    Returns:
        _type_: часть римского числа
    """
    return (
        nine                     if digit == 9 else
        five + one * (digit - 5) if digit >= 5 else
        one + five               if digit == 4 else
        one * digit              
    )


def convert_arabic_to_roman(number: int) -> str:
    """Функция перевода арабских чисел в римские.

    Args:
        number (int): арабское число

    Returns:
        str: римское число
    """
    return (
        'M' * (number // 1000) +
        encode_digit((number // 100) % 10, 'C', 'D', 'CM') +
        encode_digit((number //  10) % 10, 'X', 'L', 'XC') +
        encode_digit( number         % 10, 'I', 'V', 'IX') 
    )


def convert_roman_to_arabic(number: str) -> int:
    """Функция перевода римских чисел в арабские.

    Args:
        number (str): римское число

    Returns:
        int: арабское число
    """
    trans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    values = [trans[r] for r in number]
    result =  sum(val if val >= next_val else -val
                  for val, next_val in zip(values[:-1], values[1:])
                  ) + values[-1]
    
    return result


def average_age_by_position(file: UploadFile) -> dict:
    """Функция расчёта среднего возраста сотрудников по должности."""

    # try to get df from csv, check emptiness in file
    try:
        df = pd.read_csv(file)
    except pd.errors.EmptyDataError:
        raise CustomException('Empty file.', status_code=400)
    columns = list(df.columns)
    # chech columns
    for c in columns:
        if c not in ('Имя', 'Возраст', 'Должность'):
            raise CustomException(detail='Bad columns names.',
                                  status_code=400)
    # define working df
    df = df[['Возраст', 'Должность']]
    # make mean aggregation for position 
    df_mean_age_of_pos = df.groupby('Должность').mean().sort_index(ascending=True)
    # make final dict
    d = df_mean_age_of_pos.to_dict()
    result = d['Возраст']
    
    return result


def get_actual_file_table() -> dict:
    """Получение таблицы файлов, находящиеся в проекте."""
    try:
        with open('./files/file_table.txt', 'r') as f:
            data = f.read()
            type_d = json.loads(data)
    except FileNotFoundError:
        type_d = {}
        with open('./files/file_table.txt', 'w') as f:
            f.write("{}")
    
    return type_d


def save_file(table: dict, file: Annotated[bytes, File()]):
    """Сохранение файла в папку проекта и в таблице файлов."""
    # save file in table
    with open('./files/file_table.txt', 'w') as f:
        json.dump(table, f)
    
    # save file in folder app/files/temp
    file_location = f"./files/temp/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    


"""
Задание_6.
Дан класс DataGenerator, который имеет два метода: generate(), to_file()
Метод generate генерирует данные формата list[list[int, str, float]] и записывает результат в
переменную класса data
Метод to_file сохраняет значение переменной generated_data по пути path c помощью метода
write, классов JSONWritter, CSVWritter, YAMLWritter.

Допишите реализацию методов и классов.
"""
class BaseWriter(ABC):
    """Абстрактный класс с методом write для генерации файла"""

    @abstractmethod
    def write(self, data: list[list[int, str, float]]) -> StringIO:
        """
        Записывает данные в строковый объект файла StringIO
        :param data: полученные данные
        :return: Объект StringIO с данными из data
        """
        pass


class JSONWriter(BaseWriter):
    """Потомок BaseWriter с переопределением метода write для генерации файла в json формате"""

    """Ваша реализация"""

    pass


class CSVWriter:
    """Потомок BaseWriter с переопределением метода write для генерации файла в csv формате"""

    """Ваша реализация"""

    pass


class YAMLWriter:
    """Потомок BaseWriter с переопределением метода write для генерации файла в yaml формате"""

    """Ваша реализация"""

    pass


class DataGenerator:
    def __init__(self, data: list[list[int, str, float]] = None):
        self.data: list[list[int, str, float]] = data
        self.file_id = None

    def generate(self, matrix_size) -> None:
        """Генерирует матрицу данных заданного размера."""

        data: list[list[int, str, float]] = []
        """Ваша реализация"""

        self.data = data

    def to_file(self, path: str, writer) -> None:
        """
        Метод для записи в файл данных полученных после генерации.
        Если данных нет, то вызывается кастомный Exception.
        :param path: Путь куда требуется сохранить файл
        :param writer: Одна из реализаций классов потомков от BaseWriter
        """

        """Ваша реализация"""

        pass
