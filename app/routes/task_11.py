from sqlalchemy.orm import Session
from fastapi import HTTPException, APIRouter, Depends

from core.db import SessionLocal, User
from models import User as UserScheme


router = APIRouter(tags=["Users"])


# chech db session is active
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/api/users", response_model=list[UserScheme])
def get_users(db: Session = Depends(get_db)):
    """Маршрут для получения списка пользователей."""
    
    return db.query(User).all()
  
@router.get("/api/users/{id}", response_model=UserScheme)
def get_user(id: int, db: Session = Depends(get_db)):
    """Маршрут для получения информации опользователе."""
    
    # получаем пользователя по id
    user = db.query(User).filter(User.id == id).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if user is None:  
        return HTTPException(status_code=404, detail="User not found")
    # если пользователь найден, отправляем его
    return user
  
  
@router.post("/api/users", response_model=UserScheme)
def create_user(data: UserScheme, db: Session = Depends(get_db)):
    """Маршрут для создания пользователя."""
    
    user = User(**data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
  
@router.put("/api/users", response_model=UserScheme)
def edit_user(data: UserScheme, db: Session = Depends(get_db)):
    """Маршрут для редактирования пользователя."""
    
    # получаем пользователя по id
    user_d = data.model_dump()
    user = db.query(User).filter(User.id == data.id).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if user is None:  
        return HTTPException(status_code=404, detail="User not found")
    # если пользователь найден, изменяем его данные
    # и отправляем обратно клиенту
    user.__dict__ = user_d
    # for k, v in user_d:
    #     user.__dict__[k] = v
    db.commit() # сохраняем изменения 
    db.refresh(user)
    return user
  
  
@router.delete("/api/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    """Маршрут для удаление пользователя."""
    
    # получаем пользователя по id
    user = db.query(User).filter(User.id == id).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if user is None:  
        return HTTPException(status_code=404, detail="User not found")
    # если пользователь найден, удаляем его
    db.delete(user)  # удаляем объект
    db.commit()  # сохраняем изменения
    return user
