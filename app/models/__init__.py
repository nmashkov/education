from typing import List, Dict
from datetime import datetime, date

from pydantic import BaseModel, Field, model_validator, validator


class ConverterRequest(BaseModel):
    number: int | str


class ConverterResponse(BaseModel):
    arabic: int
    roman: str


# PYDANTIC MODELS (SCHEMES) FOR ITEM, USER AND POSITION
class Item(BaseModel):
    id: int
    title: str
    description: str | None = None
    owner_id: int

    class Config:
        from_attributes = True


class Position(BaseModel):
    id: int
    pos_name: str
    description: str | None = None
    employee_id: int

    class Config:
        from_attributes = True


class User(BaseModel):
    id: int
    name: str
    age: int = Field(gt=0, lt=100)
    adult: bool | None = None
    message: str | None = None
    items: list[Item] | None = []
    positions: list[Position] | None = []

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

    @model_validator(mode='after')
    def validate_atts(self):
        """Функция-валидатор для определения совершеннолетия."""
        
        self.adult = True if self.age >= 18 else False
        
        return self


class UserTask3(BaseModel):
    """Модель User для ПЗ 3."""
    id: int
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
    user: UserTask3
    meta: Meta


class Task6(BaseModel):
    """Model for Task6."""
    file_type: str
    matrix_size: int = Field(gt=3, lt=15)
