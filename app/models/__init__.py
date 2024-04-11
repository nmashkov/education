from typing import Union, List, Dict
from datetime import datetime, date

from pydantic import BaseModel, Field, model_validator, validator


class ConverterRequest(BaseModel):
    number: Union[int, str]


class ConverterResponse(BaseModel):
    arabic: int
    roman: str


class User(BaseModel):
    """Модель User для BigJson."""
    name: str
    age: int = Field(gt=0, lt=100)
    adult: bool | None = None
    message: str | None = None
    
    @model_validator(mode='after')
    def validate_atts(self):
        """Функция-валидатор для определения совершеннолетия."""
        
        self.adult = True if self.age >= 18 else False
        
        return self


class Meta(BaseModel):
    """Модель Meta для модели BigJson."""
    last_modification: date
    list_of_skills: List[str] = []
    mapping: Dict[str, List[int | str]]
    
    class Config:
        json_encoders = {
            date: lambda v: v.strftime("%d/%m/%y")
        }
    
    @validator("last_modification", pre=True)
    def check_date(cls, value):
        return datetime.strptime(
            value,
            "%d/%m/%Y"
        ).date()


class BigJson(BaseModel):
    """Использует модели User и Meta."""
    user: User
    meta: Meta


# Модель User для валидации входных данных
class UserCreate(BaseModel):
    username: str
    email: str


# Модель User для валидации исходящих данных - чисто для демонстрации (обычно входная модель шире чем выходная, т.к. на вход мы просим, например, пароль, который обратно не возвращаем, и другое, что не обязательно возвращать) 
class UserReturn(BaseModel):
    username: str
    email: str
    id: int | None = None

# class UserRequest(BaseModel):
#     name: str
#     message: str
#
#
# class User(BaseModel):
#     name: str
#     age: str
#     is_adult: bool
#     message: str = None
#
#
# class UserResponse(BaseModel):
#     pass
