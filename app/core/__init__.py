from abc import ABC, abstractmethod
from io import StringIO


def encode_digit(digit, one, five, nine):
    """_summary_

    Args:
        digit (_type_): _description_
        one (_type_): _description_
        five (_type_): _description_
        nine (_type_): _description_

    Returns:
        _type_: _description_
    """
    return (
        nine                     if digit == 9 else
        five + one * (digit - 5) if digit >= 5 else
        one + five               if digit == 4 else
        one * digit              
    )


def convert_arabic_to_roman(number: int) -> str:
    """_summary_

    Args:
        number (int): _description_

    Returns:
        str: _description_
    """
    return (
        'M' * (number // 1000) +
        encode_digit((number // 100) % 10, 'C', 'D', 'CM') +
        encode_digit((number //  10) % 10, 'X', 'L', 'XC') +
        encode_digit( number         % 10, 'I', 'V', 'IX') 
    )


def convert_roman_to_arabic(number: str) -> int:
    """_summary_

    Args:
        number (str): _description_

    Returns:
        int: _description_
    """
    trans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    values = [trans[r] for r in number]
    result =  sum(val if val >= next_val else -val
                  for val, next_val in zip(values[:-1], values[1:])
                  ) + values[-1]
    
    return result


def average_age_by_position(file):
    pass


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
