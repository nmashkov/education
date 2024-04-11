from fastapi import HTTPException, APIRouter

from core.db import database
from models import UserCreate, UserReturn


router = APIRouter(tags=["Users"])
    
    
# создание роута для создания юзеров
@router.post("/users/", response_model=UserReturn)
async def create_user(user: UserCreate):
    query = ("INSERT INTO users (username, email) VALUES "
             "(:username, :email) RETURNING id")
    values = {"username": user.username, "email": user.email}
    try:
        user_id = await database.execute(query=query, values=values)
        return {**user.model_dump(), "id": user_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create user")


# маршрут для получения информации о юзере по ID
@router.get("/user/{user_id}", response_model=UserReturn)
async def get_user(user_id: int):
    query = "SELECT * FROM users WHERE id = :user_id"
    values = {"user_id": user_id}
    try:
        result = await database.fetch_one(query=query, values=values)
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail="Failed to fetch user from database")
    if result:
        return UserReturn(username=result["username"], email=result["email"])
    else:
        raise HTTPException(status_code=404, detail="User not found")


# роут для обновления информации о юзере по ID
@router.put("/user/{user_id}", response_model=UserReturn)
async def update_user(user_id: int, user: UserCreate):
    query = ("UPDATE users SET username = :username, "
             "email = :email WHERE id = :user_id")
    values = {"user_id": user_id,
              "username": user.username,
              "email": user.email}
    try:
        await database.execute(query=query, values=values)
        return {**user.model_dump(), "id": user_id}
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail="Failed to update user in database")

# роут для удаления информации о юзере по ID
@router.delete("/user/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    query = "DELETE FROM users WHERE id = :user_id RETURNING id"
    values = {"user_id": user_id}
    try:
        deleted_rows = await database.execute(query=query, values=values)
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail="Failed to delete user from database")
    if deleted_rows:
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
